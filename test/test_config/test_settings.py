from config.settings import get_settings


def test_settings():
    settings = get_settings()
    setting_keys = set(settings.model_dump().keys())
    expected_keys = {
        "app_name",
        "app_version",
        "debug",
        "db_host",
        "db_port",
        "db_user",
        "db_password",
        "db_name",
    }

    assert expected_keys.issubset(setting_keys)
