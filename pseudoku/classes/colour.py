from dataclasses import dataclass
from typing import overload, Union, Tuple
import colorsys


def hex_to_rgb(hex: str) -> tuple[int, int, int]:
    """
    The hex_to_rgb function takes a hexadecimal color code as input and returns the corresponding RGB values.

    :param hex: str: Specify the hexadecimal value of the color
    :return: A tuple of integers representing the red, green and blue values of the color respectively
    """
    return tuple(int(hex.lstrip("#")[i:i + 2], 16) for i in (0, 2, 4))


def rgb_to_hex(rgb: tuple[int, int, int]) -> str:

    """
    The rgb_to_hex function takes a tuple of three integers, representing the red, green and blue values of a color.
    It returns the hexadecimal representation of that color as a string.

    :param rgb: tuple[int: Specify the type of the parameter as a tuple of three integers representing the RGB values
    :return: A string of the hexadecimal value of the color
    """
    return "#" + "".join(hex(c)[2:].zfill(2) for c in rgb)

def _3inttotuple(x: int, y: int, z: int) -> tuple[int, int, int]:
    return (x, y, z)

@dataclass
class Colour:

    rgb: tuple[int, int, int]
    hex: str
    hsv: tuple[int, int, int]

    def __post_init__(self):
        """
        The __post_init__ function is a special function that runs after the __init__ function.
        It allows us to do some post-initialization processing, such as converting hexadecimal strings to uppercase.

        :param self: Refer to the current instance of a class
        :return: None
        """
        self.hex = self.hex.upper()


    @staticmethod
    def from_rgb(*args: Union[tuple[int, int, int], list[int, int, int], int]) -> "Colour":
        """
        The from_rgb function takes a tuple or list of three integers representing the red, green and blue values of a
        color. It returns a Colour object with the corresponding RGB, hexadecimal and HSV values.

        :param args: Union[tuple[int, int, int], list[int, int, int], int]: Specify the type of the parameter as a list or directly as three integers
        :return: A Colour object with the corresponding RGB, hexadecimal and HSV values
        """
        if len(args) == 1:
            if isinstance(args[0], (list, tuple)):
                rgb = args[0]
            else:
                raise TypeError("Invalid argument type")

        elif len(args) == 3:
            rgb = args
        else:
            raise TypeError(f"Expected 1 or 3 arguments, got {len(args)}")

        return Colour(
            rgb=rgb,
            hex=rgb_to_hex(rgb),
            hsv=colorsys.rgb_to_hsv(*rgb)
        )

    @staticmethod
    def from_hex(hex: str) -> "Colour":
        """
        The from_hex function takes a hexadecimal color code as input and returns a Colour object with the corresponding RGB, hexadecimal and HSV values.

        :param hex: str: Specify the hexadecimal value of the color
        :return: A Colour object with the corresponding RGB, hexadecimal and HSV values
        """
        return Colour.from_rgb(hex_to_rgb(hex))

    @staticmethod
    def from_hsv(*args: Union[tuple[int, int, int], list[int, int, int], int]) -> "Colour":
        """
        The from_hsv function takes a tuple or list of three integers representing the hue, saturation and value of a
        color. It returns a Colour object with the corresponding RGB, hexadecimal and HSV values.

        :param args: Union[tuple[int, int, int], list[int, int, int], int]: Specify the type of the parameter as a list or directly as three integers
        :return: A Colour object with the corresponding RGB, hexadecimal and HSV values
        """
        if len(args) == 1:
            if isinstance(args[0], (list, tuple)):
                hsv = args[0]
            else:
                raise TypeError("Invalid argument type")

        elif len(args) == 3:
            hsv = args
        else:
            raise TypeError(f"Expected 1 or 3 arguments, got {len(args)}")

        return Colour(
            rgb=colorsys.hsv_to_rgb(*hsv),
            hex=rgb_to_hex(colorsys.hsv_to_rgb(*hsv)),
            hsv=hsv
        )

    @staticmethod
    def from_dict(colour_dict: dict[str, Union[str, list[int, int, int]]]) -> "Colour":
        """
        The from_dict function takes a dictionary with keys "rgb", "hex" and "hsv" as input and returns a Colour
        object with the corresponding RGB, hexadecimal and HSV values.

        :param colour_dict: dict[str, Union[str, list[int, int, int]]]: Specify the type of the parameter as a dictionary with keys "rgb", "hex" and "hsv"
        :return: A Colour object with the corresponding RGB, hexadecimal and HSV values
        """
        try:
            return Colour(
                rgb=colour_dict["rgb"],
                hex=colour_dict["hex"],
                hsv=colour_dict["hsv"]
            )
        except KeyError as e:
            raise KeyError("Colour dictionary must contain keys 'rgb', 'hex' and 'hsv'") from e


    to_rgb = lambda self: self.rgb
    to_hex = lambda self: self.hex
    to_hsv = lambda self: self.hsv
    to_dict = lambda self: {"rgb": self.rgb, "hex": self.hex, "hsv": self.hsv}
