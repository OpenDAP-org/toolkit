# Toolkit hooks

Shared pre-commit hooks for every OpenDAP repository.

Part of [OpenDAP](https://github.com/opendap-project). This repository is open source.

## Working here

- Write everything in English: code, docs, commit messages.
- Record only information the maintainers confirmed. Do not infer specs, numbers or wording.
- Licensing follows REUSE (`REUSE.toml`, `LICENSES/`). After adding files or folders, run the `/opendap:license-check` skill.
- Every OpenDAP repository pins these hooks by tag. Changing a hook means a new tag and updating the pins; this repository runs its own hooks with `repo: local`.
- The toolkit is one repository per tool domain under `public/toolkit/` (`cli`, `hooks`, `host`, `hardware`, `verify`).
