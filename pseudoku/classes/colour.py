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

