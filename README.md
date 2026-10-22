# Toolkit hooks

Shared [pre-commit](https://pre-commit.com) hooks for every OpenDAP repository. Everything runs locally; there is no CI.

Part of the [OpenDAP](https://github.com/opendap-project) Developer Toolkit, which lives in the workspace under `public/toolkit/` as one repository per tool domain.

## Hooks

| ID | What it checks |
|---|---|
| `kicad-erc` | ERC on changed KiCad schematics |
| `kicad-drc` | DRC on changed KiCad boards |
| `no-fab-outputs` | No generated fab outputs (Gerbers, drill files, packages) are committed |
| `no-stray-files` | No PDFs, and no HTML outside `renders/web/` |

Use them from a repository's `.pre-commit-config.yaml`, pinned to a tag:

```yaml
  - repo: https://github.com/opendap-project/toolkit-hooks
    rev: v0.3.0
    hooks:
      - id: no-stray-files
```

## Layout

- `.pre-commit-hooks.yaml` — hook definitions
- `hooks/` — the hook scripts

## License

This repository follows the [REUSE](https://reuse.software) layout: license texts live in `LICENSES/` and `REUSE.toml` maps each path to its license.

- Default: **GNU GPL v3.0 or later** (`GPL-3.0-or-later`)
- Markdown files: **Creative Commons Attribution-ShareAlike 4.0** (`CC-BY-SA-4.0`)

Copyright © 2026 The OpenDAP Project.
