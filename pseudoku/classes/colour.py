from dataclasses import dataclass
from typing import overload, Union, Tuple
import colorsys


@dataclass
class Colour:
    rgb: tuple[int, int, int]
    hex: str
    hsv: tuple[int, int, int]

    def __post_init__(self):
        self.hex = self.hex.upper()

    @staticmethod
    def from_hex(hex: str) -> "Colour":
        rgb = tuple(int(hex[i:i + 2], 16) for i in (1, 3, 5))
        return Colour(rgb, hex, Colour.rgb_to_hsv(rgb))

    @staticmethod
    def from_rgb(*args: Union[Tuple[int, int, int], int]) -> "Colour":
        """
        :param args: Either a tuple of 3 ints (r, g, b) or 3 ints (r, g, b)
        :return: A Colour object
        """

        if len(args) == 1 and isinstance(args[0], tuple) and len(args[0]) == 3:
            rgb = args[0]
        elif len(args) == 3:
            rgb = args

        else:
            raise TypeError("Invalid arguments, expected tuple[int, int, int] or 3 ints (r, g, b)")

        return Colour(rgb, "#" + "".join(f"{int(c):02x}" for c in rgb), colorsys.rgb_to_hsv(*rgb))


    @staticmethod
    def from_hsv(*args: Union[Tuple[int, int, int], int]) -> "Colour":
        if len(args) == 1 and isinstance(args[0], tuple) and len(args[0]) == 3:
            h, s, v = args[0]
            return Colour.from_rgb(colorsys.hsv_to_rgb(h, s, v))
        elif len(args) == 3:
            h, s, v = args
            return Colour.from_rgb(colorsys.hsv_to_rgb(h, s, v))
        else:
            raise TypeError("Invalid arguments, expected tuple[int, int, int] or 3 ints (h, s, v)")

    @staticmethod
    def from_dict(colour_dict: dict[str, str]) -> "Colour":
        return Colour.from_hex(colour_dict["hex"])

    def get_complementary(self) -> "Colour":
        return Colour.from_hsv((self.hsv[0] + 180) % 360, self.hsv[1], self.hsv[2])

    def get_triad(self) -> tuple["Colour", "Colour"]:
        return Colour.from_hsv((self.hsv[0] + 120) % 360, self.hsv[1], self.hsv[2]), Colour.from_hsv(
            (self.hsv[0] + 240) % 360, self.hsv[1], self.hsv[2])

    def get_analogous(self) -> tuple["Colour", "Colour"]:
        return Colour.from_hsv((self.hsv[0] + 30) % 360, self.hsv[1], self.hsv[2]), Colour.from_hsv(
            (self.hsv[0] + 330) % 360, self.hsv[1], self.hsv[2])

    def get_split_complementary(self) -> tuple["Colour", "Colour"]:
        return Colour.from_hsv((self.hsv[0] + 150) % 360, self.hsv[1], self.hsv[2]), Colour.from_hsv(
            (self.hsv[0] + 210) % 360, self.hsv[1], self.hsv[2])

    to_rgb = lambda self: self.rgb
    to_dict = lambda self: {"hex": self.hex, "rgb": self.rgb, "hsv": self.hsv}
    to_hsv = lambda self: self.hsv
    to_hex = lambda self: self.hex
