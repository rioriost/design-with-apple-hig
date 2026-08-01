#!/usr/bin/env python3
"""Fetch one current Apple HIG topic from Apple's official DocC JSON endpoint."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from typing import Any


HIG_PREFIX = "https://developer.apple.com/design/human-interface-guidelines/"
DOCC_PREFIX = "https://developer.apple.com/tutorials/data/design/human-interface-guidelines/"
SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def parse_slug(value: str) -> str:
    value = value.strip()
    if "://" not in value:
        slug = value.strip("/").lower()
    else:
        parsed = urllib.parse.urlparse(value)
        if parsed.scheme != "https" or parsed.netloc != "developer.apple.com":
            raise ValueError("URL must use https://developer.apple.com")
        prefix = "/design/human-interface-guidelines/"
        if not parsed.path.startswith(prefix):
            raise ValueError("URL must be an Apple Human Interface Guidelines topic")
        slug = parsed.path[len(prefix) :].strip("/").lower()
    if not SLUG_RE.fullmatch(slug):
        raise ValueError("topic must be a single lowercase Apple HIG slug")
    return slug


def fetch_json(url: str, timeout: float) -> dict[str, Any]:
    request = urllib.request.Request(
        url,
        headers={
            "Accept": "application/json",
            "User-Agent": "design-with-apple-hig/2.0 (+official-source-reader)",
        },
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        if response.status != 200:
            raise RuntimeError(f"Apple returned HTTP {response.status}")
        return json.load(response)


def inline_text(node: Any, references: dict[str, Any]) -> str:
    if node is None:
        return ""
    if isinstance(node, list):
        return "".join(inline_text(item, references) for item in node)
    if isinstance(node, str):
        return node
    if not isinstance(node, dict):
        return ""
    if isinstance(node.get("text"), str):
        return node["text"]
    if node.get("type") == "reference":
        title = node.get("overridingTitle")
        if isinstance(title, str):
            return title
        ref = references.get(node.get("identifier", ""), {})
        if isinstance(ref, dict) and isinstance(ref.get("title"), str):
            return ref["title"]
        return ""
    for key in ("inlineContent", "content"):
        if key in node:
            return inline_text(node[key], references)
    return ""


def render_blocks(blocks: Any, references: dict[str, Any], out: list[str]) -> None:
    if not isinstance(blocks, list):
        return
    for block in blocks:
        if not isinstance(block, dict):
            continue
        kind = block.get("type")
        if kind == "heading":
            level = min(max(int(block.get("level", 2)), 1), 6)
            text = str(block.get("text", "")).strip()
            if text:
                out.append(f"{'#' * level} {text}")
        elif kind == "paragraph":
            text = inline_text(block.get("inlineContent", []), references).strip()
            if text:
                out.append(text)
        elif kind in ("unorderedList", "orderedList"):
            ordered = kind == "orderedList"
            for index, item in enumerate(block.get("items", []), start=1):
                text = inline_text(item, references).strip()
                if text:
                    marker = f"{index}." if ordered else "-"
                    out.append(f"{marker} {text}")
        elif kind == "codeListing":
            code = block.get("code", [])
            if isinstance(code, list):
                out.append("```\n" + "\n".join(str(line) for line in code) + "\n```")
        elif kind == "table":
            for row in block.get("rows", []):
                cells = [inline_text(cell, references).strip() for cell in row]
                if any(cells):
                    out.append(" | ".join(cells))
        elif kind == "row":
            for column in block.get("columns", []):
                render_blocks(column.get("content", []), references, out)
        elif kind == "links":
            continue
        else:
            nested = block.get("content")
            if isinstance(nested, list):
                render_blocks(nested, references, out)


def build_result(slug: str, data: dict[str, Any]) -> dict[str, Any]:
    metadata = data.get("metadata", {}) if isinstance(data.get("metadata"), dict) else {}
    custom = metadata.get("customMetadata", {}) if isinstance(metadata.get("customMetadata"), dict) else {}
    references = data.get("references", {}) if isinstance(data.get("references"), dict) else {}
    rendered: list[str] = []
    render_blocks(data.get("primaryContentSections", []), references, rendered)
    return {
        "title": metadata.get("title", slug),
        "slug": slug,
        "source_url": HIG_PREFIX + slug,
        "docc_url": DOCC_PREFIX + slug + ".json",
        "retrieved_at_utc": dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat(),
        "supported_platforms": custom.get("supported-platforms"),
        "alert_date": custom.get("alert-date"),
        "alert_text": custom.get("alert-text"),
        "available_locales": metadata.get("availableLocales") or metadata.get("availableLanguages"),
        "content": "\n\n".join(rendered).strip(),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Read one current Apple HIG topic from Apple's official DocC JSON."
    )
    parser.add_argument("topic", help="HIG slug or canonical Apple HIG topic URL")
    parser.add_argument("--format", choices=("markdown", "json"), default="markdown")
    parser.add_argument("--metadata-only", action="store_true")
    parser.add_argument("--timeout", type=float, default=20.0)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        slug = parse_slug(args.topic)
        data = fetch_json(DOCC_PREFIX + slug + ".json", args.timeout)
        result = build_result(slug, data)
    except (ValueError, urllib.error.URLError, TimeoutError, RuntimeError, json.JSONDecodeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    if args.metadata_only:
        result = {key: value for key, value in result.items() if key != "content"}

    if args.format == "json" or args.metadata_only:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"# {result['title']}")
        print(f"\n- Source: {result['source_url']}")
        print(f"- Retrieved: {result['retrieved_at_utc']}")
        if result.get("supported_platforms"):
            print(f"- Platforms: {result['supported_platforms']}")
        if result.get("alert_date") or result.get("alert_text"):
            print(f"- Update: {result.get('alert_date') or 'unspecified'} — {result.get('alert_text') or ''}")
        if result.get("content"):
            print("\n" + result["content"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
