# Contributing

Thanks for helping keep Awesome AI Tools 2026 accurate and useful.

This repository is curated. A submission may be declined even when the product is real: the goal is a focused guide, not the largest possible directory.

## Before suggesting a tool

The tool should:

- solve a clear, practical AI-related problem;
- be publicly usable or have useful public documentation;
- be actively maintained;
- have an official HTTPS product, documentation, or source link;
- offer meaningful value beyond a thin wrapper or copied interface;
- fit one of the existing categories, or justify a genuinely useful new one.

Do not submit affiliate links, URL shorteners, tracking links, pirated services, abandoned projects, or misleading claims.

## Vendor submissions

Creators and employees may submit their own product. Disclose the relationship in the issue or pull request. Affiliation does not disqualify a tool, but undisclosed promotion does.

Paid placement is not accepted. Inclusion does not imply endorsement, and placement within a category is editorial rather than sponsored.

## Preferred workflow

1. Open the **Suggest a tool** issue form.
2. Wait for confirmation that the tool fits the catalog.
3. Add one tool per pull request unless a maintainer requests a batch.
4. Edit [`data/tools.json`](data/tools.json), not the generated tables.
5. Run the generator and validation commands.

```bash
python3 scripts/generate_readme.py
python3 scripts/validate.py
```

## Data format

Each tool requires:

```json
{
  "name": "Product name",
  "url": "https://official.example/",
  "category": "existing-category-id",
  "description_en": "One neutral sentence describing the practical use.",
  "description_ru": "Нейтральное описание практического назначения.",
  "access": "Free tier",
  "source": "Closed",
  "local": false,
  "api": true
}
```

Descriptions should be factual, concise, and free of claims such as “best,” “revolutionary,” or “industry-leading.” See [`data/README.md`](data/README.md) for allowed labels.

## Corrections and removals

Open a **Catalog correction** issue for:

- broken or redirected official links;
- discontinued or abandoned tools;
- material pricing or licensing changes;
- incorrect local/API labels;
- security concerns that affect whether a tool should remain listed.

Please link to an official announcement, documentation page, repository, or pricing page when possible.

## Pull request checklist

- The official URL is used and contains no affiliate parameters.
- The description explains what the tool does, not what its marketing promises.
- English and Russian descriptions communicate the same facts.
- Access, source, local, and API labels have been checked.
- Generated README files are included.
- `python3 scripts/validate.py` passes.
