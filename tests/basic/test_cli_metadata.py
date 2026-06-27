import tomllib

import pytest

from codeloom import branding
from codeloom.args import get_parser


def test_pyproject_exposes_only_codeloom_console_script():
    with open("pyproject.toml", "rb") as pyproject:
        metadata = tomllib.load(pyproject)

    project = metadata["project"]
    scripts = project["scripts"]

    assert project["name"] == branding.PACKAGE_NAME
    assert project["description"] == branding.DESCRIPTION
    assert "codeloom" in scripts
    assert scripts["codeloom"] == "codeloom.cli:main"


def test_top_level_source_package_is_codeloom():
    with open("pyproject.toml", "rb") as pyproject:
        metadata = tomllib.load(pyproject)

    assert metadata["tool"]["setuptools"]["packages"]["find"]["include"] == ["codeloom*"]
    assert metadata["tool"]["setuptools_scm"]["write_to"] == "codeloom/_version.py"


def test_pyproject_has_scm_fallback_version_for_source_archives():
    with open("pyproject.toml", "rb") as pyproject:
        metadata = tomllib.load(pyproject)

    assert metadata["tool"]["setuptools_scm"]["fallback_version"] == "0.1.0"


def test_version_output_uses_codeloom_program_name(capsys):
    parser = get_parser([], None)
    parser.prog = branding.CLI_NAME

    with pytest.raises(SystemExit):
        parser.parse_args(["--version"])

    assert capsys.readouterr().out.startswith("codeloom ")


def test_lightweight_cli_version_does_not_import_runtime_stack(capsys):
    from codeloom.cli import main

    with pytest.raises(SystemExit):
        main(["--version"])

    assert capsys.readouterr().out.startswith("codeloom ")
