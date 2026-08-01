#!/usr/bin/env python3
"""Validate the public Codex skill repository without third-party packages."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXPECTED_NAME = "design-with-apple-hig"
REQUIRED_FILES = (
    "SKILL.md",
    "agents/openai.yaml",
    "references/bibliography.md",
    "references/official-source-map.md",
    "references/platform-routing.md",
    "references/review-rubric.md",
    "references/source-routing.md",
    "references/verification-loop.md",
    "scripts/fetch_apple_hig.py",
)


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def validate_frontmatter(skill_text: str) -> None:
    match = re.match(r"\A---\r?\n(.*?)\r?\n---\r?\n", skill_text, re.DOTALL)
    if not match:
        fail("SKILL.md must start with YAML frontmatter")

    fields: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if not line.strip():
            continue
        if ":" not in line:
            fail(f"Malformed frontmatter line: {line}")
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip()

    if set(fields) != {"name", "description"}:
        fail("SKILL.md frontmatter must contain only name and description")
    if fields["name"] != EXPECTED_NAME:
        fail(f"Expected skill name {EXPECTED_NAME!r}, found {fields['name']!r}")
    if not fields["description"]:
        fail("Skill description must not be empty")


def validate_links(skill_text: str) -> None:
    local_links = re.findall(r"\]\((references/[^)]+|scripts/[^)]+)\)", skill_text)
    for relative in local_links:
        if not (ROOT / relative).is_file():
            fail(f"Broken SKILL.md link: {relative}")


def main() -> None:
    missing = [path for path in REQUIRED_FILES if not (ROOT / path).is_file()]
    if missing:
        fail("Missing required files: " + ", ".join(missing))

    skill_text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    validate_frontmatter(skill_text)
    validate_links(skill_text)

    legacy = "apply-" + "apple-hig"
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        if path.suffix.lower() not in {".md", ".py", ".yaml", ".yml"}:
            continue
        if legacy in path.read_text(encoding="utf-8"):
            fail(f"Legacy skill name remains in {path.relative_to(ROOT)}")

    print(f"Repository is valid: {EXPECTED_NAME}")


if __name__ == "__main__":
    main()
