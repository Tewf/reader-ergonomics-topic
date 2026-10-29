"""Judgment quotes: an answer in checks/judgments.toml quotes, in backticks, something that is in the file it answers for.

An answer is a claim about one file, and its reason is the evidence. A reason copied from another file's answer can
name words this file does not hold, and still pass every other check. So:

- every phrase an answer quotes in backticks must occur in its file, ignoring case and runs of spaces (exact);
- an answer to a question named in `[judgment_quotes] require` must quote at least one phrase, so its reason can be
  checked at all (exact).

A question about a path is answered from the path: for a folder, each quote must be the name of an entry in it; for
two files changing together, a quote may also be the other file the question names. An answer for a path that no
longer exists is left to the standard, which drops it.

What a clean run guarantees: every quoted phrase is in the answered file as it is now. What it does not: that the
reason is right, or that the quote supports it. Reading decides that.
Exact. Time O(answers × file size).
"""
from __future__ import annotations

import re
import tomllib
from pathlib import Path

from framework.check_api import Finding

NAME = "judgment-quotes"
EXACT = True

QUOTE = re.compile(r"`([^`]+)`")
REQUIRE = ["document-mode", "logical-lines", "figures-present", "paraphrase", "name-content", "tree-shape", "co-change"]


def flat(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip().lower()


def check(root: Path, config: dict) -> list[Finding]:
    source = root / "checks" / "judgments.toml"
    if not source.is_file():
        return []
    raw = source.read_text(encoding="utf-8")
    try:
        answers = tomllib.loads(raw).get("answer", [])
    except tomllib.TOMLDecodeError as error:
        return [Finding(NAME, "checks/judgments.toml", 1, f"cannot be read as TOML: {error}")]
    require = set(config.get("judgment_quotes", {}).get("require", REQUIRE))
    findings = []
    for answer in answers:
        path, kind, reason = answer.get("path", ""), answer.get("check", ""), answer.get("answer", "")
        target = root / path
        anchor = f'check = "{kind}"\npath = "{path}"'
        line = raw[:raw.find(anchor)].count("\n") + 1 if anchor in raw else 1
        quotes = QUOTE.findall(reason)
        if target.is_dir():
            text = " | ".join(flat(entry.name) for entry in target.iterdir())
        elif target.is_file():
            text = flat(target.read_text(encoding="utf-8", errors="replace")) + " | " + flat(answer.get("question", ""))
        else:
            continue
        for quote in quotes:
            if flat(quote) not in text:
                where = "an entry of that folder" if target.is_dir() else "in that file"
                findings.append(Finding(NAME, "checks/judgments.toml", line,
                                        f"the answer for {path} ({kind}) quotes `{quote}`, which is not {where}"))
        if kind in require and reason and not quotes:
            findings.append(Finding(NAME, "checks/judgments.toml", line,
                                    f"the answer for {path} ({kind}) quotes nothing from its file: put a word or "
                                    "heading of that file in backticks, so its reason can be checked"))
    return findings
