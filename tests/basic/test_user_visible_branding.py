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


def iter_user_visible_files():
    roots = [Path("README.md"), Path("pyproject.toml"), Path("docker"), Path("codeloom"), Path("tests")]
    for root in roots:
        if root.is_file():
            yield root
            continue
        for path in root.rglob("*"):
            if path.is_file() and path.suffix.lower() in TEXT_SUFFIXES:
                yield path


def test_user_visible_files_do_not_reference_old_brand():
    offenders = []
    for path in iter_user_visible_files():
        text = path.read_text(encoding="utf-8", errors="ignore")
        if OLD_LOWER in text or OLD_TITLE in text or OLD_UPPER in text:
            offenders.append(str(path))

    assert offenders == []
