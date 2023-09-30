from dataclasses import dataclass
from .colour import Colour
from .font import Font

DEFAULT_THEME = {
    "background_colour": "#3900E3",
    "complementary_colour": "#aae300",
    "triad_colour": "#e33900",
    "text_colour": "#b796f8",
    "number_font": {
        "filename": "assets/fonts/Roboto/RobotoMono-Regular.ttf",
        "font_size": 32,
        "colour": "#b796f8",
    },
    "title_font": {
        "filename": "assets/fonts/Roboto/RobotoMono-Regular.ttf",
        "font_size": 64,
        "colour": "#b796f8",
    },
    "subtitle_font": {
        "filename": "assets/fonts/Roboto/RobotoMono-Regular.ttf",
        "font_size": 48,
        "colour": "#b796f8",
    },
}


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
            subtitle_font=Font.from_dict(theme_dict["subtitle_font"]),
        )

    @staticmethod
    @property
    def DEFAULT() -> "Theme":
        return Theme(
            background_colour=Colour.from_hex(DEFAULT_THEME["background_colour"]),
            complementary_colour=Colour.from_hex(DEFAULT_THEME["complementary_colour"]),
            triad_colour=Colour.from_hex(DEFAULT_THEME["triad_colour"]),
            text_colour=Colour.from_hex(DEFAULT_THEME["text_colour"]),
            number_font=Font.from_dict(DEFAULT_THEME["number_font"]),
            title_font=Font.from_dict(DEFAULT_THEME["title_font"]),
            subtitle_font=Font.from_dict(DEFAULT_THEME["subtitle_font"]),
        )
