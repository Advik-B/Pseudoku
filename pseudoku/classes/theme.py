from dataclasses import dataclass
from .colour import Colour
from .font import Font

@dataclass
class Theme:
    background_colour: Colour
    complementary_colour: Colour
    triad_colour: Colour
    text_colour: Colour
    number_font: Font
    title_font: Font
    subtitle_font: Font

    @staticmethod
    def from_dict(theme_dict: dict[str, str]) -> "Theme":
        return Theme(
            background_colour=Colour.from_dict(theme_dict["background_colour"]),
            complementary_colour=Colour.from_dict(theme_dict["complementary_colour"]),
            triad_colour=Colour.from_dict(theme_dict["triad_colour"]),
            text_colour=Colour.from_dict(theme_dict["text_colour"]),
            number_font=Font.from_dict(theme_dict["number_font"]),
            title_font=Font.from_dict(theme_dict["title_font"]),
            subtitle_font=Font.from_dict(theme_dict["subtitle_font"])
        )

