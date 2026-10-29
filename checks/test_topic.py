"""Tests of checks/local/topic.py: each rule fails where it should and stays silent where it should not.

Run: python3 -m unittest discover -s checks
The standard's checks/ folder must be importable: set READER_ERGONOMICS_CHECKS to it, or check
reader-ergonomics out beside this repository (as CI does, under the name standard).
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
SPEC = importlib.util.spec_from_file_location("topic", REPOSITORY / "checks" / "local" / "topic.py")
topic = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(topic)

CONFIG = {"topic": {"files": ["README.md", "docs/"], "root": "README.md", "summary_words": 12, "listing_words": 3}}
TOPIC = "# {title}\n\nA short summary of this topic.\n\nBody.\n"


class TopicCheck(unittest.TestCase):
    def setUp(self) -> None:
        self.root = Path(tempfile.mkdtemp())

    def tearDown(self) -> None:
        shutil.rmtree(self.root)

    def write(self, path: str, text: str) -> None:
        (self.root / path).parent.mkdir(parents=True, exist_ok=True)
        (self.root / path).write_text(text, encoding="utf-8")

    def found(self) -> list[tuple[str, str, str]]:
        return [(finding.path, finding.kind, finding.message) for finding in topic.check(self.root, CONFIG)]

    def tree(self, depth: int) -> None:
        """A chain of folders, each README listing the next with its summary."""
        folder = ""
        for level in range(depth):
            child = f"{folder}docs{level}/" if level else "docs/"
            self.write(f"{folder}README.md" if folder else "README.md",
                       TOPIC.format(title=f"Level {level}") + f"\n| [next]({child.split('/')[-2]}/) | its summary, one line |\n")
            folder = child
        self.write(f"{folder}README.md", TOPIC.format(title="Leaf"))

    def test_a_tree_at_any_depth_passes(self) -> None:
        self.tree(5)
        self.assertEqual(self.found(), [])

    def test_a_topic_without_title_fails(self) -> None:
        self.write("README.md", "A summary with no title.\n")
        self.assertIn(("README.md", "error", "a topic opens with its title, one '# ' heading"), self.found())

    def test_a_second_title_fails(self) -> None:
        self.write("README.md", TOPIC.format(title="One") + "\n# Two\n\nMore.\n")
        self.assertIn(("README.md", "error", "a second '# ' title: a topic has one title"), self.found())

    def test_a_heading_after_the_title_is_no_summary(self) -> None:
        self.write("README.md", "# Title\n\n## Detail\n\nText.\n")
        messages = [message for _, _, message in self.found()]
        self.assertIn("no summary after the title: one to three sentences that stand for the topic", messages)

    def test_badges_are_not_the_summary(self) -> None:
        self.write("README.md", "# Title\n\n[![ci](https://x/b.svg)](https://x/c)\n\nThe summary itself.\n")
        self.assertEqual(self.found(), [])

    def test_a_long_summary_warns(self) -> None:
        self.write("README.md", "# Title\n\n" + "word " * 13 + "\n")
        self.assertEqual([kind for _, kind, _ in self.found()], ["warning"])

    def test_a_child_its_parent_does_not_list_fails(self) -> None:
        self.write("README.md", TOPIC.format(title="Root"))
        self.write("docs/README.md", TOPIC.format(title="Docs"))
        self.assertIn(("docs/README.md", "error",
                       "not listed by its containing topic README.md: a reader cannot reach it from the root"), self.found())

    def test_a_bare_link_warns(self) -> None:
        self.write("README.md", TOPIC.format(title="Root") + "\nSteps: [docs](docs/) · [other](other.md)\n")
        self.write("docs/README.md", TOPIC.format(title="Docs"))
        self.assertEqual([kind for path, kind, _ in self.found() if path == "docs/README.md"], ["warning"])

    def test_a_listing_with_its_summary_passes(self) -> None:
        self.write("README.md", TOPIC.format(title="Root") + "\n- [docs](docs/README.md): where the documents live\n")
        self.write("docs/README.md", TOPIC.format(title="Docs"))
        self.assertEqual(self.found(), [])

    def test_a_file_in_a_folder_is_listed_by_the_folder_readme(self) -> None:
        self.tree(1)
        self.write("docs/page.md", TOPIC.format(title="Page"))
        self.assertIn("docs/page.md", [path for path, kind, _ in self.found() if kind == "error"])

    def test_an_inclusion_cycle_fails(self) -> None:
        self.write("a.qmd", "{{< include b.qmd >}}\n")
        self.write("b.qmd", "{{< include a.qmd >}}\n")
        self.write("README.md", TOPIC.format(title="Root"))
        cycles = [message for _, _, message in self.found() if message.startswith("inclusion cycle")]
        self.assertEqual(cycles, ["inclusion cycle: a.qmd -> b.qmd -> a.qmd"])

    def test_an_inclusion_without_cycle_passes(self) -> None:
        self.write("index.qmd", "{{< include README.md >}}\n")
        self.write("README.md", TOPIC.format(title="Root"))
        self.assertEqual(self.found(), [])


if __name__ == "__main__":
    unittest.main()
