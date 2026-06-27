#!/usr/bin/env python
import argparse
import os
import shutil
import subprocess
import sys
import tempfile
import tomllib
from pathlib import Path


OLD_LOWER = "ai" + "der"
OLD_TITLE = "Ai" + "der"
OLD_UPPER = "AI" + "DER"
TEXT_SUFFIXES = {
    "",
    ".cfg",
    ".css",
    ".html",
    ".in",
    ".ini",
    ".js",
    ".json",
    ".md",
    ".ps1",
    ".py",
    ".rst",
    ".scss",
    ".sh",
    ".toml",
    ".txt",
    ".yaml",
    ".yml",
}


def run(cmd, cwd=None):
    return subprocess.run(
        cmd,
        cwd=cwd,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )


def fail(message):
    print(f"FAIL: {message}")
    return False


def contains_old_brand(text):
    return OLD_LOWER in text or OLD_TITLE in text or OLD_UPPER in text


def iter_text_files(root):
    for path in root.rglob("*"):
        if path.is_file() and path.suffix.lower() in TEXT_SUFFIXES:
            yield path


def check_structure(repo_root):
    if not (repo_root / "codeloom").is_dir():
        return fail("missing codeloom/ source package")
    if (repo_root / OLD_LOWER).exists():
        return fail("old source package directory still exists")
    return True


def check_pyproject(repo_root):
    with open(repo_root / "pyproject.toml", "rb") as fh:
        metadata = tomllib.load(fh)

    project = metadata["project"]
    scripts = project["scripts"]
    package_include = metadata["tool"]["setuptools"]["packages"]["find"]["include"]
    scm = metadata["tool"]["setuptools_scm"]

    checks = [
        (project["name"] == "codeloom", "project name is not codeloom"),
        (scripts == {"codeloom": "codeloom.cli:main"}, "console script is not codeloom-only"),
        (package_include == ["codeloom*"], "package include is not scoped to Codeloom"),
        (scm["write_to"] == "codeloom/_version.py", "setuptools_scm write_to is not codeloom"),
    ]
    for ok, message in checks:
        if not ok:
            return fail(message)
    return True


def check_text_scan(repo_root):
    roots = [
        repo_root / "README.md",
        repo_root / "pyproject.toml",
        repo_root / "docker",
        repo_root / "codeloom",
        repo_root / "tests",
    ]
    offenders = []
    for root in roots:
        paths = [root] if root.is_file() else list(iter_text_files(root))
        for path in paths:
            text = path.read_text(encoding="utf-8", errors="ignore")
            if contains_old_brand(text):
                offenders.append(str(path.relative_to(repo_root)))
    if offenders:
        return fail("old brand found in user-visible files: " + ", ".join(offenders[:10]))
    return True


def check_cli(command):
    version = run([command, "--version"])
    if version.returncode != 0:
        return fail("--version failed:\n" + version.stdout)
    if not version.stdout.startswith("codeloom "):
        return fail("--version did not start with codeloom")
    if contains_old_brand(version.stdout):
        return fail("--version output contains old brand")

    help_result = run([command, "--help"])
    if help_result.returncode != 0:
        return fail("--help failed:\n" + help_result.stdout)
    if contains_old_brand(help_result.stdout):
        return fail("--help output contains old brand")
    if "Codeloom" not in help_result.stdout or "CODELOOM_" not in help_result.stdout:
        return fail("--help output is missing Codeloom branding")
    return True


def check_temp_project(command):
    tmp = Path(tempfile.mkdtemp(prefix="codeloom-acceptance-"))
    try:
        if shutil.which("git"):
            run(["git", "init"], cwd=tmp)
        result = run(
            [
                command,
                "--exit",
                "--no-check-update",
                "--analytics-disable",
                "--no-show-release-notes",
                "--no-gitignore",
                "--no-show-model-warnings",
                "--no-git",
                "--model",
                "deepseek/deepseek-chat",
                "--api-key",
                "deepseek=test-key",
            ],
            cwd=tmp,
        )
        if result.returncode != 0:
            return fail("temporary project run failed:\n" + result.stdout)
        if contains_old_brand(result.stdout):
            return fail("temporary project output contains old brand")

        generated = [path.name for path in tmp.iterdir()]
        old_generated = [name for name in generated if OLD_LOWER in name.lower()]
        if old_generated:
            return fail("temporary project generated old-brand files: " + ", ".join(old_generated))
        codeloom_files = [name for name in generated if name.startswith(".codeloom")]
        if not codeloom_files:
            return fail("temporary project did not generate any .codeloom files")
        return True
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def main(argv=None):
    parser = argparse.ArgumentParser(description="Validate the Codeloom wrapper experience.")
    parser.add_argument("--repo-root", default=Path(__file__).resolve().parents[1], type=Path)
    parser.add_argument("--command", default=os.environ.get("CODELOOM_COMMAND", "codeloom"))
    parser.add_argument("--skip-runtime", action="store_true")
    args = parser.parse_args(argv)

    repo_root = args.repo_root.resolve()
    checks = [
        ("structure", check_structure(repo_root)),
        ("pyproject", check_pyproject(repo_root)),
        ("text scan", check_text_scan(repo_root)),
        ("cli", check_cli(args.command)),
    ]
    if not args.skip_runtime:
        checks.append(("temporary project", check_temp_project(args.command)))

    failed = [name for name, ok in checks if not ok]
    if failed:
        print("Failed checks: " + ", ".join(failed))
        return 1

    print("All Codeloom acceptance checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
