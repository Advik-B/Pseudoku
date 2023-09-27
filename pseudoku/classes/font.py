from dataclasses import dataclass
from .colour import Colour
from pygame.font import Font as PGfont


@dataclass
class Font:
    filename: str
    font_size: int
    colour: Colour
    pg_font: PGfont

    def __post_init__(self):
        self.pg_font = PGfont(self.filename, self.font_size)

    @staticmethod
    def from_dict(font_dict):
        return Font(
            filename=font_dict["filename"],
            font_size=font_dict["font_size"],
            colour=Colour.from_dict(font_dict["colour"]),
            pg_font=PGfont(font_dict["filename"], font_dict["font_size"])
        )

    def render(self, text: str, background: Colour, antialias: bool=True) -> PGfont:
        return self.pg_font.render(text, antialias, self.colour.rgb, background.rgb)
