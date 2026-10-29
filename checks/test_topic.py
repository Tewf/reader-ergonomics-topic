"""Tests of checks/local/topic.py: each rule fails where it should and stays silent where it should not.

Run: python3 -m unittest discover -s checks
The standard's checks/ folder must be importable: set READER_ERGONOMICS_CHECKS to it, or check
reader-ergonomics out beside this repository (as CI does, under the name standard).
"""
import importlib.util
import os
import random
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


class Base(unittest.TestCase):
    """A temporary repository, and the helpers every test class shares; no tests of its own."""
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


class TopicCheck(Base):
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

    def test_a_byline_may_stand_before_a_labelled_abstract(self) -> None:
        self.write("README.md", "# A result\n\nFirst Author, Institution.\n\n**Abstract.** What is proved, in one sentence.\n\nBody.\n")
        self.assertEqual(self.found(), [])

    def test_an_abstract_heading_holds_the_summary(self) -> None:
        self.write("README.md", "# A finding\n\nFirst Author.\n\n## Abstract\n\nWhat was found, in one sentence.\n")
        self.assertEqual(self.found(), [])

    def test_an_abstract_heading_with_nothing_under_it_is_no_summary(self) -> None:
        self.write("README.md", "# A finding\n\n## Abstract\n\n## Methods\n\nText.\n")
        self.assertIn("no summary", " ".join(message for _, _, message in self.found()))

    def test_a_labelled_summary_is_measured_without_its_label(self) -> None:
        self.write("README.md", "# A result\n\nAuthor.\n\n**Abstract.** " + "word " * 13 + "\n")
        self.assertEqual([kind for _, kind, _ in self.found()], ["warning"])

    def test_a_typed_child_may_be_listed_by_its_type_name(self) -> None:
        config = {"topic": dict(CONFIG["topic"], typed=["frame.md"])}
        self.write("README.md", TOPIC.format(title="Root") + "\n- [docs](docs/README.md): where the documents live\n")
        self.write("docs/README.md", TOPIC.format(title="Docs") + "\nSteps: [frame](frame.md) · [other](other.md)\n")
        self.write("docs/frame.md", TOPIC.format(title="Frame"))
        self.write("docs/other.md", TOPIC.format(title="Other"))
        found = [(f.path, f.kind) for f in topic.check(self.root, config)]
        self.assertEqual(found, [("docs/other.md", "warning")])


class ErrorPaths(Base):
    """Inputs a careless check would crash on, or pass silently."""

    def test_an_empty_topic_fails_without_crashing(self) -> None:
        self.write("README.md", "")
        self.assertIn(("README.md", "error", "a topic opens with its title, one '# ' heading"), self.found())

    def test_front_matter_alone_is_no_title(self) -> None:
        self.write("README.md", "---\ntitle: x\n---\n")
        self.assertIn("a topic opens with its title", " ".join(message for _, _, message in self.found()))

    def test_bytes_that_are_not_utf8_are_read_not_skipped(self) -> None:
        (self.root / "README.md").write_bytes(b"# Title\n\nA summary \xff\xfe of the topic.\n")
        self.assertEqual(self.found(), [])

    def test_no_declared_topics_means_no_findings(self) -> None:
        self.write("README.md", "no title")
        self.assertEqual(topic.check(self.root, {"topic": {"files": []}}), [])

    def test_a_topic_with_no_readme_above_has_no_containing_topic(self) -> None:
        config = {"topic": dict(CONFIG["topic"], files=["docs/"])}
        self.write("docs/page.md", TOPIC.format(title="Page"))
        messages = [finding.message for finding in topic.check(self.root, config)]
        self.assertTrue(any(message.startswith("no containing topic") for message in messages))

    def test_an_address_or_anchor_is_not_a_listing(self) -> None:
        self.write("README.md", TOPIC.format(title="Root") + "\n[docs](https://example.org/docs/README.md) and [here](#docs)\n")
        self.write("docs/README.md", TOPIC.format(title="Docs"))
        self.assertIn("docs/README.md", [path for path, kind, _ in self.found() if kind == "error"])

    def test_an_inclusion_of_a_missing_file_is_not_a_cycle(self) -> None:
        self.write("README.md", TOPIC.format(title="Root"))
        self.write("index.qmd", "{{< include missing.md >}}\n")
        self.assertEqual(self.found(), [])

    def test_a_file_that_includes_itself_is_a_cycle(self) -> None:
        self.write("README.md", TOPIC.format(title="Root"))
        self.write("a.qmd", "{{< include a.qmd >}}\n")
        self.assertIn("inclusion cycle: a.qmd -> a.qmd", [message for _, _, message in self.found()])


class Announced(Base):
    """A file declared of a shape links that shape's file."""

    def config(self) -> dict:
        return {"topic": dict(CONFIG["topic"], shapes={"decision-record": ["docs/0*.md"]})}

    def setup_tree(self, record: str) -> None:
        self.write("README.md", TOPIC.format(title="Root") + "\n- [docs](docs/README.md): where the records live\n")
        self.write("docs/README.md", TOPIC.format(title="Docs") + "\n- [one](0001-one.md): the first record, in full\n")
        self.write("docs/0001-one.md", record)

    def test_a_record_that_links_its_shape_passes(self) -> None:
        self.setup_tree(TOPIC.format(title="0001 One") + "\nShape: [decision record](../shapes/decision-record.md).\n")
        self.assertEqual([f.message for f in topic.check(self.root, self.config())], [])

    def test_a_record_that_does_not_announce_its_shape_fails(self) -> None:
        self.setup_tree(TOPIC.format(title="0001 One"))
        messages = [f.message for f in topic.check(self.root, self.config())]
        self.assertEqual(len(messages), 1)
        self.assertTrue(messages[0].startswith("declared a decision-record but does not link shapes/decision-record.md"))

    def test_a_link_inside_code_is_not_an_announcement(self) -> None:
        self.setup_tree(TOPIC.format(title="0001 One") + "\n`[decision record](../shapes/decision-record.md)`\n")
        self.assertEqual(len(topic.check(self.root, self.config())), 1)


def random_tree(root: Path, rng: random.Random) -> list[str]:
    """A tree of topics in folders and files, each listed by its parent with a summary; returns every topic path."""
    paths = []

    def grow(folder: str, depth: int) -> None:
        readme = f"{folder}/README.md" if folder else "README.md"
        lines = [TOPIC.format(title=f"Topic {len(paths)}")]
        paths.append(readme)
        for index in range(rng.randint(1 if depth < 2 else 0, 3) if depth < 6 else 0):
            if rng.random() < 0.5:
                child = f"{folder}/sub{index}" if folder else f"docs{index}"
                lines.append(f"- [child {index}]({child.split('/')[-1]}/): a summary of child {index}")
                grow(child, depth + 1)
            else:
                name = f"page{index}.md"
                page = f"{folder}/{name}" if folder else name
                (root / page).parent.mkdir(parents=True, exist_ok=True)
                (root / page).write_text(TOPIC.format(title=f"Page {index}"), encoding="utf-8")
                paths.append(page)
                lines.append(f"- [page {index}]({name}): a summary of page {index}")
        (root / readme).parent.mkdir(parents=True, exist_ok=True)
        (root / readme).write_text("\n".join(lines) + "\n", encoding="utf-8")

    grow("", 0)
    return paths


class Properties(unittest.TestCase):
    """Invariants on random trees: a sound tree passes; one break gives exactly one finding, where it is."""

    SEEDS = range(100)
    ALL = {"topic": {"files": ["README.md", "docs0/", "docs1/", "docs2/", "page0.md", "page1.md", "page2.md"],
                     "root": "README.md", "summary_words": 12, "listing_words": 3}}

    def each_tree(self):
        for seed in self.SEEDS:
            root = Path(tempfile.mkdtemp())
            try:
                rng = random.Random(seed)
                yield seed, root, rng, random_tree(root, rng)
            finally:
                shutil.rmtree(root)

    def test_a_sound_tree_of_any_shape_passes(self) -> None:
        for seed, root, _, paths in self.each_tree():
            with self.subTest(seed=seed, topics=len(paths)):
                self.assertEqual(topic.check(root, self.ALL), [])

    def test_removing_one_listing_breaks_exactly_that_topic(self) -> None:
        for seed, root, rng, paths in self.each_tree():
            if len(paths) < 2:
                continue
            victim = rng.choice(paths[1:])
            parent = topic.containing(victim, set(paths))
            text = (root / parent).read_text(encoding="utf-8")
            target = victim.rsplit("/", 2)[-2] + "/" if victim.endswith("README.md") else victim.rsplit("/", 1)[-1]
            kept = [line for line in text.splitlines() if f"]({target})" not in line]
            (root / parent).write_text("\n".join(kept) + "\n", encoding="utf-8")
            with self.subTest(seed=seed, victim=victim):
                found = [(f.path, f.kind) for f in topic.check(root, self.ALL)]
                self.assertEqual(found, [(victim, "error")])

    def test_a_heading_in_place_of_one_summary_breaks_exactly_that_topic(self) -> None:
        for seed, root, rng, paths in self.each_tree():
            victim = rng.choice(paths)
            text = (root / victim).read_text(encoding="utf-8")
            (root / victim).write_text(text.replace("A short summary of this topic.", "## Detail", 1), encoding="utf-8")
            with self.subTest(seed=seed, victim=victim):
                found = [(f.path, f.kind) for f in topic.check(root, self.ALL)]
                self.assertEqual(found, [(victim, "error")])

    def test_one_inclusion_cycle_is_reported_once(self) -> None:
        for seed, root, rng, paths in self.each_tree():
            ring = rng.sample(paths, min(len(paths), rng.randint(1, 4)))
            for here, there in zip(ring, ring[1:] + ring[:1]):
                rel = os.path.relpath(there, os.path.dirname(here) or ".")
                with (root / here).open("a", encoding="utf-8") as handle:
                    handle.write("\n{{< include " + rel + " >}}\n")
            with self.subTest(seed=seed, ring=ring):
                cycles = [f.message for f in topic.check(root, self.ALL) if f.message.startswith("inclusion cycle")]
                self.assertEqual(len(cycles), 1)
                self.assertEqual(set(cycles[0].removeprefix("inclusion cycle: ").split(" -> ")), set(ring))


if __name__ == "__main__":
    unittest.main()
