# Contributing to Codeloom

## Development Setup

```bash
python -m pip install -e . --no-deps
python -m pytest tests/basic/test_acceptance_script.py tests/basic/test_user_visible_branding.py tests/basic/test_cli_metadata.py tests/basic/test_project_structure.py tests/basic/test_branding.py tests/basic/test_runtime_paths.py -q
```

## Acceptance

Before handing off changes that affect packaging, paths, CLI output, or documentation, run:

```bash
python scripts/check_codeloom_acceptance.py
```

Keep user-facing paths and text aligned with the Codeloom conventions in `README.md`.
