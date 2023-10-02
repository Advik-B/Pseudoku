from dataclasses import dataclass
from .theme import Theme, DEFAULT as DEFAULT_THEME
from typing import Any


@dataclass
class Settings:
    width: int
    height: int
    theme: Theme
    vsync: bool
    fps: int
    resizable: bool
    full_screen: bool

    # Debug info
    debug: bool = False
    version_string: str = "v0.1.0"
    version_number: tuple[int, int, int] = (0, 1, 0)

    size: tuple[int, int] = None

    @staticmethod
    def from_dict(settings_dict: dict[str, str]) -> "Settings":
        return Settings(
            width=settings_dict["width"],
            height=settings_dict["height"],
            theme=Theme.from_dict(settings_dict["theme"]),
            vsync=settings_dict["vsync"],
            fps=settings_dict["fps"],
            debug=settings_dict["debug"],
            version_string=settings_dict["version_string"],
            version_number=settings_dict["version_number"],
            size=(settings_dict["width"], settings_dict["height"]),
            resizable=settings_dict["resizable"],
            full_screen=settings_dict["fullscreen"],
        )

    def __post_init__(self):
        self.width = round(self.width)
        self.height = round(self.height)
        self.vsync = bool(self.vsync)
        self.fps = round(self.fps)
        self.debug = bool(self.debug)
        self.version_string = str(self.version_string)
        self.version_number = tuple(int(i) for i in self.version_number)

        self.size = (self.width, self.height)
        self.full_screen = False if self.resizable else bool(self.full_screen)

    def to_dict(self) -> dict[str, str]:
        return {
            "width": self.width,
            "height": self.height,
            "theme": self.theme.to_dict(),
            "vsync": self.vsync,
            "fps": self.fps,
            "debug": self.debug,
            "version_string": self.version_string,
            "version_number": self.version_number,
            "resizable": self.resizable,
            "fullscreen": self.full_screen,
        }

    def _replace(self, key: str, value: Any) -> None:
        self.__dict__[key] = value


DEFAULT = Settings(
    width=1200,
    height=860,
    theme=DEFAULT_THEME,
    vsync=True,
    fps=60,
    debug=True,
    version_string="vUNKNOWN",
    version_number=(0, 0, 0),
    resizable=True,
    full_screen=False,
)
