# AI Done Log

### 2026-06-27 | TASK-001 | Established Codeloom branding constants
- summary: Added a central branding module and wired parser description, env prefix, and key default help paths to Codeloom values.
- files: codeloom/branding.py; codeloom/args.py; tests/basic/test_branding.py
- follow_ups: Continue migrating CLI metadata and runtime paths.

### 2026-06-27 | TASK-002 | Migrated CLI and package metadata
- summary: Switched project metadata and console entrypoint to codeloom, added an SCM fallback version for source archives, and introduced a lightweight CLI path for help/version.
- files: pyproject.toml; codeloom/cli.py; tests/basic/test_cli_metadata.py
- follow_ups: Continue replacing runtime file paths and user data locations.

### 2026-06-27 | TASK-003 | Migrated user runtime paths
- summary: Switched parser defaults, analytics storage, versioncheck cache, repo-map cache, watch ignores, and main config search paths to Codeloom names.
- files: codeloom/args.py; codeloom/analytics.py; codeloom/versioncheck.py; codeloom/repomap.py; codeloom/watch.py; codeloom/main.py; tests/basic/test_runtime_paths.py
- follow_ups: Continue top-level package rename and user-visible text cleanup.

### 2026-06-27 | TASK-004 | Renamed top-level source package
- summary: Renamed the source package to codeloom, updated imports/tests/configuration mechanically, and verified the editable install exposes `codeloom.cli:main`.
- files: codeloom/; pyproject.toml; tests/basic/test_project_structure.py; tests/basic/test_cli_metadata.py
- follow_ups: Clean remaining user-visible text and add an automated acceptance script.

### 2026-06-27 | TASK-005 | Cleaned user-visible branding
- summary: Added a user-visible branding scan and verified README, pyproject, Docker, source, tests, and real CLI startup output do not show the old upstream brand.
- files: tests/basic/test_user_visible_branding.py; README.md; docker/; codeloom/; tests/
- follow_ups: Add a one-command acceptance script.

### 2026-06-27 | TASK-006 | Added acceptance self-check
- summary: Added a script that validates package structure, pyproject metadata, CLI help/version output, user-visible text, and clean temporary project runtime files.
- files: scripts/check_codeloom_acceptance.py; tests/basic/test_acceptance_script.py
- follow_ups: none

### 2026-06-27 | TASK-007 | Localized user documentation
- summary: Rewrote the README as a Chinese user guide and verified product documentation does not expose the old upstream brand.
- files: README.md; docs/ai-loop/done.md
- follow_ups: none

## Entry Template
### YYYY-MM-DD | TASK-000 | Short summary
- summary: What was delivered.
- files: path/to/file
- follow_ups: none
