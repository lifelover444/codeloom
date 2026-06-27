from pathlib import Path

from codeloom import branding
from codeloom.args import get_parser


def test_parser_defaults_use_codeloom_files(tmp_path):
    parser = get_parser([], str(tmp_path))
    args = parser.parse_args([])

    assert Path(args.model_settings_file).name == branding.MODEL_SETTINGS_FILE
    assert Path(args.model_metadata_file).name == branding.MODEL_METADATA_FILE
    assert Path(args.input_history_file).name == branding.INPUT_HISTORY_FILE
    assert Path(args.chat_history_file).name == branding.CHAT_HISTORY_FILE
    assert Path(args.codeloomignore).name == branding.IGNORE_FILE
    assert args.check_update is False


def test_runtime_user_data_paths_use_codeloom_directory():
    from codeloom.analytics import Analytics
    from codeloom import repomap
    from codeloom.repomap import RepoMap
    from codeloom.versioncheck import VERSION_CHECK_FNAME

    analytics = Analytics(permanently_disable=True)

    assert analytics.get_data_file_path() == branding.user_data_path(branding.ANALYTICS_FILE)
    assert VERSION_CHECK_FNAME == branding.user_data_path("caches", branding.VERSION_CHECK_FILE)
    assert RepoMap.TAGS_CACHE_DIR == branding.tags_cache_dir(repomap.CACHE_VERSION)
