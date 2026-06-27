from pathlib import Path

OLD_PACKAGE = "ai" + "der"


def test_project_uses_codeloom_top_level_package():
    assert Path("codeloom").is_dir()
    assert not Path(OLD_PACKAGE).exists()
