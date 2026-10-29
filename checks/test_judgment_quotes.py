"""Tests of checks/local/judgment_quotes.py: a reason must quote its own file, and only its own file.

Run: python3 -m unittest discover -s checks (see test_topic.py for where the standard's checks come from).
"""
import importlib.util
import os
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve()
REPOSITORY = HERE.parents[1]
CANDIDATES = [os.environ.get("READER_ERGONOMICS_CHECKS", ""),
              REPOSITORY.parent / "standard" / "checks", REPOSITORY.parent / "reader-ergonomics" / "checks"]
sys.path.insert(0, str(next(Path(c) for c in CANDIDATES if c and (Path(c) / "framework").is_dir())))
SPEC = importlib.util.spec_from_file_location("judgment_quotes", REPOSITORY / "checks" / "local" / "judgment_quotes.py")
quotes = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(quotes)


def entry(check: str, path: str, answer: str) -> str:
    return f'[[answer]]\ncheck = "{check}"\npath = "{path}"\nquestion = "q"\nfile = "x"\nanswer = "{answer}"\n'


class JudgmentQuotes(unittest.TestCase):
    def setUp(self) -> None:
        self.root = Path(tempfile.mkdtemp())
        (self.root / "checks").mkdir()
        (self.root / "a.md").write_text("# Against\n\n## Null results for the typed format\n\nText.\n", encoding="utf-8")
        (self.root / "b.md").write_text("# Frame\n\n## What the field calls it\n\nText.\n", encoding="utf-8")

    def tearDown(self) -> None:
        shutil.rmtree(self.root)

    def run_on(self, *entries: str) -> list[str]:
        (self.root / "checks" / "judgments.toml").write_text("\n".join(entries), encoding="utf-8")
        return [finding.message for finding in quotes.check(self.root, {})]

    def test_a_quote_from_its_own_file_passes(self) -> None:
        self.assertEqual(self.run_on(entry("document-mode", "a.md", "Reference: under `Null results for the typed format`.")), [])

    def test_case_and_spacing_do_not_matter(self) -> None:
        self.assertEqual(self.run_on(entry("document-mode", "a.md", "Reference: `null  RESULTS for the typed format`.")), [])

    def test_a_reason_copied_from_another_file_fails(self) -> None:
        found = self.run_on(entry("document-mode", "a.md", "Reference: under `What the field calls it`."))
        self.assertEqual(found, ["the answer for a.md (document-mode) quotes `What the field calls it`, which is not in that file"])

    def test_a_content_answer_with_no_quote_fails(self) -> None:
        found = self.run_on(entry("logical-lines", "b.md", "One role. It stays whole."))
        self.assertTrue(found and found[0].startswith("the answer for b.md (logical-lines) quotes nothing"))

    def test_a_path_question_needs_a_quote_too(self) -> None:
        found = self.run_on(entry("co-change", "a.md", "They change together by design."))
        self.assertTrue(found and found[0].startswith("the answer for a.md (co-change) quotes nothing"))

    def test_a_folder_answer_quotes_an_entry_of_the_folder(self) -> None:
        (self.root / "box").mkdir()
        (self.root / "box" / "one.py").write_text("x", encoding="utf-8")
        self.assertEqual(self.run_on(entry("tree-shape", "box", "It stays: it holds `one.py`.")), [])
        found = self.run_on(entry("tree-shape", "box", "It stays: it holds `two.py`."))
        self.assertEqual(found, ["the answer for box (tree-shape) quotes `two.py`, which is not an entry of that folder"])

    def test_a_co_change_answer_may_quote_the_other_file_the_question_names(self) -> None:
        text = '[[answer]]\ncheck = "co-change"\npath = "a.md"\nquestion = "changed together with b.md in 3 commits"\nfile = "x"\nanswer = "By design: `b.md` tests it."\n'
        self.assertEqual(self.run_on(text), [])

    def test_a_missing_path_is_left_alone(self) -> None:
        self.assertEqual(self.run_on(entry("document-mode", "gone.md", "Reference: `anything`.")), [])

    def test_no_answers_file_means_no_findings(self) -> None:
        self.assertEqual(quotes.check(self.root, {}), [])

    def test_a_broken_answers_file_is_reported_not_crashed_on(self) -> None:
        (self.root / "checks" / "judgments.toml").write_text("[[answer]\nbroken", encoding="utf-8")
        found = [finding.message for finding in quotes.check(self.root, {})]
        self.assertTrue(found and found[0].startswith("cannot be read as TOML"))


if __name__ == "__main__":
    unittest.main()
