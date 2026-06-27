from pathlib import Path

PRODUCT_NAME = "Codeloom"
PRODUCT_NAME_LOWER = "codeloom"
CLI_NAME = "codeloom"
PACKAGE_NAME = "codeloom"
PYPI_PACKAGE = "codeloom"
DESCRIPTION = "Codeloom is AI pair programming in your terminal"

ENV_PREFIX = "CODELOOM_"
LEGACY_ENV_PREFIX = "CODELOOM_"

USER_DIR_NAME = ".codeloom"
CONFIG_FILE = ".codeloom.conf.yml"
IGNORE_FILE = ".codeloomignore"
INPUT_HISTORY_FILE = ".codeloom.input.history"
CHAT_HISTORY_FILE = ".codeloom.chat.history.md"
LLM_HISTORY_EXAMPLE = ".codeloom.llm.history"
MODEL_SETTINGS_FILE = ".codeloom.model.settings.yml"
MODEL_METADATA_FILE = ".codeloom.model.metadata.json"
TAGS_CACHE_DIR_TEMPLATE = ".codeloom.tags.cache.v{version}"
OAUTH_KEYS_FILE = "oauth-keys.env"
ANALYTICS_FILE = "analytics.json"
INSTALLS_FILE = "installs.json"
VERSION_CHECK_FILE = "versioncheck"

GIT_ATTRIBUTION_NAME = "codeloom"
GIT_ATTRIBUTION_EMAIL = "codeloom@local"
COMMIT_MESSAGE_PREFIX = "codeloom: "

REPOSITORY_URL = "https://github.com/codeloom/codeloom"
ISSUES_URL = REPOSITORY_URL + "/issues/new"
DOCS_URL = REPOSITORY_URL + "#readme"
RELEASE_NOTES_URL = REPOSITORY_URL + "/releases"


def user_data_path(*parts):
    return Path.home().joinpath(USER_DIR_NAME, *parts)


def repo_file(git_root, filename):
    if git_root:
        return str(Path(git_root) / filename)
    return filename


def tags_cache_dir(version):
    return TAGS_CACHE_DIR_TEMPLATE.format(version=version)
