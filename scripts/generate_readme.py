#!/usr/bin/env python3
"""Generate the English and Russian catalog README files from tools.json."""

from __future__ import annotations

import argparse
import json
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "tools.json"

LOCALES = {
    "en": {
        "template": ROOT / "templates" / "README.en.template.md",
        "output": ROOT / "README.md",
        "tool": "Tool",
        "best_for": "Useful for",
        "access": "Access",
        "source": "Source",
        "local": "Local",
        "api": "API",
        "yes": "Yes",
        "no": "No",
        "source_labels": {
            "Open": "Open",
            "Mixed": "Mixed",
            "Closed": "Closed",
            "Source available": "Source available",
        },
        "access_labels": {},
    },
    "ru": {
        "template": ROOT / "templates" / "README.ru.template.md",
        "output": ROOT / "README.ru.md",
        "tool": "Инструмент",
        "best_for": "Для чего полезен",
        "access": "Доступ",
        "source": "Исходники",
        "local": "Локально",
        "api": "API",
        "yes": "Да",
        "no": "Нет",
        "source_labels": {
            "Open": "Открытые",
            "Mixed": "Смешанные",
            "Closed": "Закрытые",
            "Source available": "Исходники доступны",
        },
        "access_labels": {
            "Free": "Бесплатно",
            "Free tier": "Есть бесплатный тариф",
            "Paid": "Платно",
            "Usage-based": "Оплата за использование",
            "Open source": "Открытый код",
            "Mixed": "Смешанный",
        },
    },
}


def load_data() -> dict:
    with DATA_PATH.open(encoding="utf-8") as source:
        return json.load(source)


def format_date(value: str, locale: str) -> str:
    parsed = date.fromisoformat(value)
    if locale == "en":
        return f"{parsed.strftime('%B')} {parsed.day}, {parsed.year}"

    months = (
        "января",
        "февраля",
        "марта",
        "апреля",
        "мая",
        "июня",
        "июля",
        "августа",
        "сентября",
        "октября",
        "ноября",
        "декабря",
    )
    return f"{parsed.day} {months[parsed.month - 1]} {parsed.year}"


def escape_cell(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ").strip()


def build_catalog(data: dict, locale: str) -> tuple[str, str]:
    labels = LOCALES[locale]
    tools_by_category: dict[str, list[dict]] = {
        category["id"]: [] for category in data["categories"]
    }
    for tool in data["tools"]:
        tools_by_category[tool["category"]].append(tool)

    toc_lines = []
    sections = []
    for category in data["categories"]:
        category_id = category["id"]
        title = category[f"title_{locale}"]
        description = category[f"description_{locale}"]
        category_tools = tools_by_category[category_id]
        toc_lines.append(f"- [{title} ({len(category_tools)})](#{category_id})")

        lines = [
            f'<a id="{category_id}"></a>',
            "",
            f"### {title}",
            "",
            description,
            "",
            (
                f"| {labels['tool']} | {labels['best_for']} | {labels['access']} | "
                f"{labels['source']} | {labels['local']} | {labels['api']} |"
            ),
            "|---|---|---|---|:---:|:---:|",
        ]

        for tool in category_tools:
            access = labels["access_labels"].get(tool["access"], tool["access"])
            source = labels["source_labels"][tool["source"]]
            local = labels["yes"] if tool["local"] else labels["no"]
            api = labels["yes"] if tool["api"] else labels["no"]
            lines.append(
                "| "
                + " | ".join(
                    (
                        f"**[{escape_cell(tool['name'])}]({tool['url']})**",
                        escape_cell(tool[f"description_{locale}"]),
                        access,
                        source,
                        local,
                        api,
                    )
                )
                + " |"
            )

        sections.append("\n".join(lines))

    return "\n".join(toc_lines), "\n\n".join(sections)


def render_readme(locale: str, data: dict | None = None) -> str:
    data = data or load_data()
    locale_config = LOCALES[locale]
    template = locale_config["template"].read_text(encoding="utf-8")
    toc, catalog = build_catalog(data, locale)
    rendered = (
        template.replace("{{TOOL_COUNT}}", str(len(data["tools"])))
        .replace("{{CATEGORY_COUNT}}", str(len(data["categories"])))
        .replace("{{LAST_UPDATED}}", format_date(data["last_updated"], locale))
        .replace("{{LAST_UPDATED_BADGE}}", data["last_updated"].replace("-", "--"))
        .replace("{{TOC}}", toc)
        .replace("{{CATALOG}}", catalog)
    )
    return rendered.rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="Fail if generated README files differ from committed files.",
    )
    args = parser.parse_args()

    stale = []
    for locale, config in LOCALES.items():
        expected = render_readme(locale)
        output = config["output"]
        if args.check:
            current = output.read_text(encoding="utf-8") if output.exists() else ""
            if current != expected:
                stale.append(output.relative_to(ROOT))
            continue

        output.write_text(expected, encoding="utf-8")
        print(f"Generated {output.relative_to(ROOT)}")

    if stale:
        print("Generated files are stale:")
        for path in stale:
            print(f"- {path}")
        print("Run: python3 scripts/generate_readme.py")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
