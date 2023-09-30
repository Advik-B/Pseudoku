from dataclasses import dataclass
from .theme import Theme, DEFAULT as DEFAULT_THEME


@dataclass
class Settings:
    width: int
    height: int
    theme: Theme
    vsync: bool
    fps: int

    # Debug info
    debug: bool = False
    version_string: str = "v0.1.0"
    version_number: tuple[int, int, int] = (0, 1, 0)

    @staticmethod
    def from_dict(settings_dict: dict[str, str]) -> "Settings":
        print(settings_dict)
        return Settings(
            width=settings_dict["width"],
            height=settings_dict["height"],
            theme=Theme.from_dict(settings_dict["theme"]),
            vsync=settings_dict["vsync"],
            fps=settings_dict["fps"],
            debug=settings_dict["debug"],
            version_string=settings_dict["version_string"],
            version_number=settings_dict["version_number"],
        )

    def __post_init__(self):
        self.width = round(self.width)
        self.height = round(self.height)
        self.vsync = bool(self.vsync)
        self.fps = round(self.fps)
        self.debug = bool(self.debug)
        self.version_string = str(self.version_string)
        self.version_number = tuple(int(i) for i in self.version_number)

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
        }


DEFAULT = Settings(
    width=800,
    height=600,
    theme=DEFAULT_THEME,
    vsync=True,
    fps=60,
    debug=True,
    version_string="vUNKNOWN",
    version_number=(0, 0, 0),
)
