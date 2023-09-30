from yaml import safe_load, dump
from classes import Settings
import os

KB = 1024
MB = 1024 * KB
MAX_FILE_SIZE = 1 * MB


def load_settings() -> Settings:
    # Check if the file exists
    if not os.path.exists("settings.yaml"):
        # Create the file with DEFAULT settings
        save_settings(Settings.DEFAULT)
        return Settings.DEFAULT

    # Check the file size first
    if filesize := os.path.getsize("settings.yaml") > MAX_FILE_SIZE:
        raise RuntimeError(
            f"settings.yaml is too large to load, maximum size is {MAX_FILE_SIZE / MB} MB, got {filesize / MB} MB)"
        )

    with open("settings.yaml", "r") as f:
        settings_dict = safe_load(f)
    return Settings.from_dict(settings_dict)


def save_settings(settings: Settings) -> None:
    with open("settings.yaml", "w") as f:
        dump(settings, f)
