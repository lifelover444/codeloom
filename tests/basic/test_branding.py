from pathlib import Path

from codeloom import branding
from codeloom.args import get_parser

OLD_BRAND = "ai" + "der"


def test_branding_defines_codeloom_public_surface():
    assert branding.PRODUCT_NAME == "Codeloom"
    assert branding.CLI_NAME == "codeloom"
    assert branding.PACKAGE_NAME == "codeloom"
    assert branding.ENV_PREFIX == "CODELOOM_"
    assert branding.CONFIG_FILE == ".codeloom.conf.yml"
    assert branding.IGNORE_FILE == ".codeloomignore"
    assert branding.INPUT_HISTORY_FILE == ".codeloom.input.history"
    assert branding.CHAT_HISTORY_FILE == ".codeloom.chat.history.md"
    assert branding.MODEL_SETTINGS_FILE == ".codeloom.model.settings.yml"
    assert branding.MODEL_METADATA_FILE == ".codeloom.model.metadata.json"
    assert branding.user_data_path("caches", "versioncheck") == (
        Path.home() / ".codeloom" / "caches" / "versioncheck"
    )


def test_parser_uses_codeloom_help_and_env_prefix():
    parser = get_parser([], None)
    parser.parse_known_args([])
    help_text = parser.format_help()

    assert parser.description == branding.DESCRIPTION
    model_action = next(action for action in parser._actions if "--model" in action.option_strings)
    assert model_action.env_var == "CODELOOM_MODEL"
    assert "CODELOOM_MODEL" in help_text
    assert ".codeloom.conf.yml" in help_text
    assert ".codeloomignore" in help_text
    assert "codeloom --shell-completions bash" in help_text
    assert OLD_BRAND not in help_text.lower()
