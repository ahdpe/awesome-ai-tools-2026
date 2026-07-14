# Catalog data

[`tools.json`](tools.json) is the source of truth for both catalog README files.

## Top-level fields

- `last_updated`: ISO date of the latest full catalog review.
- `categories`: ordered category definitions in English and Russian.
- `tools`: ordered tool entries. Their order within a category is editorial, not a ranking.

## Tool labels

### `access`

- `Free`: usable without payment as the normal product model.
- `Free tier`: a limited no-cost plan or allowance exists.
- `Paid`: payment or a paid subscription is normally required.
- `Usage-based`: primarily charged by API or compute usage.
- `Open source`: the main tool is available as open-source software.
- `Mixed`: access depends materially on the selected model, license, or hosted service.

### `source`

- `Open`: the main implementation is distributed under an open-source license.
- `Closed`: the main implementation is proprietary.
- `Mixed`: meaningful open components exist alongside proprietary components or services.
- `Source available`: source can be inspected or self-hosted, but its license has restrictions beyond a standard open-source license.

### `local`

Use `true` only when a meaningful part of the product or its supported model workload can run on user-controlled hardware. A desktop client that only calls a hosted model is `false`.

### `api`

Use `true` when an official developer API or SDK is documented. Browser automation and unofficial reverse-engineered endpoints do not count.

## Updating the catalog

After changing `tools.json`, regenerate and validate:

```bash
python3 scripts/generate_readme.py
python3 scripts/validate.py
```
