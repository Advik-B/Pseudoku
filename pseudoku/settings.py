import os

from yaml import safe_load as load, safe_dump as dump
from .classes import Settings, settings
from base64 import b64encode, b64decode
from json import dumps

KB = 1024
MB = 1024 * KB
MAX_FILE_SIZE = 1 * MB


def set_settings_in_env(settings: Settings) -> None:
    os.environ["PSUDOKU_SETTINGS"] = b64encode(
        dumps(settings.to_dict()).encode()
    ).decode()


def get_settings_from_env() -> Settings:
    return Settings.from_dict(
        load(b64decode(os.environ["PSUDOKU_SETTINGS"].encode()).decode())
    )


def load_settings() -> Settings:
    # Check if in environment
    if "PSUDOKU_SETTINGS" in os.environ:
        return get_settings_from_env()

    # Check if the file exists
    if not os.path.exists("settings.yaml"):
        # Create the file with DEFAULT settings
        save_settings(settings.DEFAULT)
        set_settings_in_env(settings.DEFAULT)
        return settings.DEFAULT

    # Check the file size first
    if filesize := os.path.getsize("settings.yaml") > MAX_FILE_SIZE:
        raise RuntimeError(
            f"settings.yaml is too large to load, maximum size is {MAX_FILE_SIZE / MB} MB, got {filesize / MB} MB)"
        )

    with open("settings.yaml", "r") as f:
        settings_dict = load(f)
        print(settings_dict)
        set_settings_in_env(Settings.from_dict(settings_dict))
        return Settings.from_dict(settings_dict)


def save_settings(settings: Settings) -> None:
    with open("settings.yaml", "w") as f:
        dump(settings.to_dict(), f)
