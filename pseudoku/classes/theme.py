from dataclasses import dataclass
from .colour import Colour
from .font import Font

ROBOTO = "assets/fonts/Roboto/Roboto-Regular.ttf"
DEFAULT_THEME = {
    "background_colour": "#b796f8",
    "complementary_colour": "#aae300",
    "triad_colour": "#e33900",
    "text_colour": "#e300aa",
    "number_font": {
        "filename": None,
        "font_size": 32,
    },
    "title_font": {
        "filename": None,
        "font_size": 64,
    },
    "subtitle_font": {
        "filename": None,
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
        def _(font_dict: dict[str, str], theme_dict: dict) -> dict[str, str]:
            """
            Helper function to set the colour of a font because we dont want repeated code (or json)
            :param font_dict: The font dict to convert
            :param ftype: The type of font to convert, either "n" for number, "t" for title, or "s" for subtitle
            """

            font_dict["colour"] = theme_dict["text_colour"]
            return font_dict

        def __(colour_hex: str) -> Colour:
            """
            Helper function to set the rgb of a colour because we dont want repeated code (or json)
            :param colour_hex: The hex of the colour to convert
            :return: Colour
            """
            return Colour.from_hex(colour_hex)

        print(theme_dict["complementary_colour"])
        print(theme_dict["triad_colour"])
        print(theme_dict["text_colour"])

        return Theme(
            background_colour=Colour.from_hex(theme_dict["background_colour"]),
            complementary_colour=Colour.from_hex(theme_dict["complementary_colour"]),
            triad_colour=Colour.from_hex(theme_dict["triad_colour"]),
            text_colour=Colour.from_hex(theme_dict["text_colour"]),
            number_font=Font.from_dict(_(theme_dict["number_font"], theme_dict)),
            title_font=Font.from_dict(_(theme_dict["title_font"], theme_dict)),
            subtitle_font=Font.from_dict(_(theme_dict["subtitle_font"], theme_dict)),
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

    def load_fonts(self):
        """
        Load the fonts, use this after pygame.init() has been called
        :return:
        """
        self.number_font.init()
        self.title_font.init()
        self.subtitle_font.init()


DEFAULT = Theme.from_dict(DEFAULT_THEME)
