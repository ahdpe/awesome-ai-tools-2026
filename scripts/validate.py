#!/usr/bin/env python3
"""Validate catalog data and ensure generated documentation is current."""

from __future__ import annotations

import json
import subprocess
import sys
from datetime import date
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "tools.json"
REQUIRED_TOOL_FIELDS = {
    "name",
    "url",
    "category",
    "description_en",
    "description_ru",
    "access",
    "source",
    "local",
    "api",
}
ALLOWED_ACCESS = {
    "Free",
    "Free tier",
    "Paid",
    "Usage-based",
    "Open source",
    "Mixed",
}
ALLOWED_SOURCE = {"Open", "Mixed", "Closed", "Source available"}
MINIMUM_TOOL_COUNT = 60


def validate_data() -> list[str]:
    errors: list[str] = []
    try:
        data = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"Cannot read {DATA_PATH.relative_to(ROOT)}: {exc}"]

    try:
        updated = date.fromisoformat(data["last_updated"])
        if updated > date.today():
            errors.append("last_updated cannot be in the future")
    except (KeyError, TypeError, ValueError):
        errors.append("last_updated must be an ISO date")

    categories = data.get("categories")
    tools = data.get("tools")
    if not isinstance(categories, list) or not categories:
        errors.append("categories must be a non-empty list")
        return errors
    if not isinstance(tools, list):
        errors.append("tools must be a list")
        return errors
    if len(tools) < MINIMUM_TOOL_COUNT:
        errors.append(
            f"catalog must contain at least {MINIMUM_TOOL_COUNT} tools; found {len(tools)}"
        )

    category_ids: set[str] = set()
    for index, category in enumerate(categories, start=1):
        missing = {
            "id",
            "title_en",
            "title_ru",
            "description_en",
            "description_ru",
        } - set(category)
        if missing:
            errors.append(f"category #{index} is missing: {', '.join(sorted(missing))}")
            continue
        category_id = category["id"]
        if category_id in category_ids:
            errors.append(f"duplicate category id: {category_id}")
        category_ids.add(category_id)

    names: set[str] = set()
    urls: set[str] = set()
    used_categories: set[str] = set()
    for index, tool in enumerate(tools, start=1):
        label = tool.get("name", f"tool #{index}") if isinstance(tool, dict) else f"tool #{index}"
        if not isinstance(tool, dict):
            errors.append(f"{label} must be an object")
            continue
        missing = REQUIRED_TOOL_FIELDS - set(tool)
        if missing:
            errors.append(f"{label} is missing: {', '.join(sorted(missing))}")
            continue

        normalized_name = tool["name"].strip().casefold()
        normalized_url = tool["url"].strip().rstrip("/").casefold()
        if normalized_name in names:
            errors.append(f"duplicate tool name: {tool['name']}")
        names.add(normalized_name)
        if normalized_url in urls:
            errors.append(f"duplicate tool URL: {tool['url']}")
        urls.add(normalized_url)

        parsed_url = urlparse(tool["url"])
        if parsed_url.scheme != "https" or not parsed_url.netloc:
            errors.append(f"{label} must use a valid HTTPS URL")
        if tool["category"] not in category_ids:
            errors.append(f"{label} has unknown category: {tool['category']}")
        used_categories.add(tool["category"])
        if tool["access"] not in ALLOWED_ACCESS:
            errors.append(f"{label} has invalid access value: {tool['access']}")
        if tool["source"] not in ALLOWED_SOURCE:
            errors.append(f"{label} has invalid source value: {tool['source']}")
        if not isinstance(tool["local"], bool) or not isinstance(tool["api"], bool):
            errors.append(f"{label} local and api values must be booleans")
        for field in ("description_en", "description_ru"):
            if not isinstance(tool[field], str) or len(tool[field].strip()) < 20:
                errors.append(f"{label} has an incomplete {field}")

    unused = category_ids - used_categories
    if unused:
        errors.append(f"categories without tools: {', '.join(sorted(unused))}")
    return errors


def main() -> int:
    errors = validate_data()
    if errors:
        print("Catalog validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    readme_check = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "generate_readme.py"), "--check"],
        cwd=ROOT,
        check=False,
    )
    if readme_check.returncode:
        return readme_check.returncode

    data = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    print(
        f"OK: {len(data['tools'])} tools in {len(data['categories'])} categories; "
        "README files are current."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
