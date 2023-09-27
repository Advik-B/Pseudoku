from dataclasses import dataclass
from .colour import Colour

@dataclass
class Theme:
    background_colour: Colour
    text_colour: Colour