from dataclasses import dataclass
from typing import overload

@dataclass
class Colour:
    rgb: tuple[int, int, int]
    hex: str
    hsv: tuple[int, int, int]

    def __post_init__(self):
        self.hex = self.hex.upper()

    @staticmethod
    def from_hex(hex: str) -> "Colour":
        rgb = tuple(int(hex.casefold()[1:][i:i + 2], 16) for i in (0, 2, 4))
        return Colour(rgb, hex, Colour.rgb_to_hsv(rgb))

    @staticmethod
    def from_rgb(rgb: tuple[int, int, int]) -> "Colour":
        return Colour(rgb, "#"+"".join(f"{c:02x}" for c in rgb), Colour.rgb_to_hsv(rgb))


    @staticmethod
    def from_dict(colour_dict: dict[str, str]) -> "Colour":
        return Colour.from_hex(colour_dict["hex"])

    @staticmethod
    def from_hsv(hsv: tuple[int, int, int]) -> "Colour":
        return Colour.from_rgb(Colour.hsv_to_rgb(hsv))

    @staticmethod
    @overload
    def from_hsv(h: int, s: int, v: int) -> "Colour":
        return Colour.from_hsv((h, s, v))

    @staticmethod
    def rgb_to_hsv(rgb: tuple[int, int, int]) -> tuple[int, int, int]:
        """
        Convert RGB to HSV
        :param rgb:
        :return:
        """
        r, g, b = rgb
        r, g, b = r / 255.0, g / 255.0, b / 255.0

        max_val = max(r, g, b)
        min_val = min(r, g, b)
        delta = max_val - min_val

        # Calculate Hue
        if delta == 0:
            h = 0
        elif max_val == r:
            h = ((g - b) / delta) % 6
        elif max_val == g:
            h = (b - r) / delta + 2
        else:
            h = (r - g) / delta + 4

        h = int(h * 60)
        if h < 0:
            h += 360

        # Calculate Saturation
        s = 0 if max_val == 0 else int((delta / max_val) * 100)

        # Calculate Value
        v = int(max_val * 100)

        return h, s, v


    @staticmethod
    def hsv_to_rgb(hsv: tuple[int, int, int]) -> tuple[int, int, int]:
        h, s, v = hsv
        h /= 360.0
        s /= 100.0
        v /= 100.0

        i = int(h * 6)
        f = (h * 6) - i
        p = v * (1 - s)
        q = v * (1 - f * s)
        t = v * (1 - (1 - f) * s)

        if i % 6 == 0:
            r, g, b = v, t, p
        elif i % 6 == 1:
            r, g, b = q, v, p
        elif i % 6 == 2:
            r, g, b = p, v, t
        elif i % 6 == 3:
            r, g, b = p, q, v
        elif i % 6 == 4:
            r, g, b = t, p, v
        else:
            r, g, b = v, p, q

        r = int(r * 255)
        g = int(g * 255)
        b = int(b * 255)

        return r, g, b

    to_rgb = lambda self: self.rgb
    to_dict = lambda self: {"hex": self.hex, "rgb": self.rgb, "hsv": self.hsv}
    to_hsv = lambda self: self.hsv
    to_hex = lambda self: self.hex


    def get_complementary(self) -> "Colour":
        return Colour.from_hsv((self.hsv[0] + 180) % 360, self.hsv[1], self.hsv[2])

    def get_triad(self) -> tuple["Colour", "Colour"]:
        return Colour.from_hsv((self.hsv[0] + 120) % 360, self.hsv[1], self.hsv[2]), Colour.from_hsv((self.hsv[0] + 240) % 360, self.hsv[1], self.hsv[2])

    def get_analogous(self) -> tuple["Colour", "Colour"]:
        return Colour.from_hsv((self.hsv[0] + 30) % 360, self.hsv[1], self.hsv[2]), Colour.from_hsv((self.hsv[0] + 330) % 360, self.hsv[1], self.hsv[2])

    def get_split_complementary(self) -> tuple["Colour", "Colour"]:
        return Colour.from_hsv((self.hsv[0] + 150) % 360, self.hsv[1], self.hsv[2]), Colour.from_hsv((self.hsv[0] + 210) % 360, self.hsv[1], self.hsv[2])
    