from dataclasses import dataclass
from .colour import Colour
from .font import Font

ROBOTO = "assets/fonts/Roboto/Roboto-Regular.ttf"
DEFAULT_THEME = {
    "background_colour": {"hex": "#b796f8", "rgb": [183, 150, 248]},
    "complementary_colour": {"hex": "#aae300", "rgb": [170, 227, 0]},
    "triad_colour": {"hex": "#e33900", "rgb": [227, 57, 0]},
    "text_colour": {"hex": "#e300aa", "rgb": [227, 0, 170]},
    "number_font": {
        "filename": ROBOTO,
        "font_size": 32,
    },
    "title_font": {
        "filename": ROBOTO,
        "font_size": 64,
    },
    "subtitle_font": {
        "filename": ROBOTO,
        "font_size": 48,
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
        def _(font_dict: dict[str, str]) -> dict[str, str]:
            """
            Helper function to set the colour of a font because we dont want repeated code (or json)
            :param font_dict:
            :return:
            """
            font_dict["colour"] = theme_dict["text_colour"]
            return font_dict

        return Theme(
            background_colour=Colour.from_dict(theme_dict["background_colour"]),
            complementary_colour=Colour.from_dict(theme_dict["complementary_colour"]),
            triad_colour=Colour.from_dict(theme_dict["triad_colour"]),
            text_colour=Colour.from_dict(theme_dict["text_colour"]),
            number_font=Font.from_dict(_(theme_dict["number_font"])),
            title_font=Font.from_dict(_(theme_dict["title_font"])),
            subtitle_font=Font.from_dict(_(theme_dict["subtitle_font"])),
        )

    def to_dict(self) -> dict[str, str]:
        return {
            "background_colour": self.background_colour.to_hex(),
            "complementary_colour": self.complementary_colour.to_hex(),
            "triad_colour": self.triad_colour.to_hex(),
            "text_colour": self.text_colour.to_hex(),
            "number_font": self.number_font.to_dict(),
            "title_font": self.title_font.to_dict(),
            "subtitle_font": self.subtitle_font.to_dict(),
        }


DEFAULT = Theme.from_dict(DEFAULT_THEME)
