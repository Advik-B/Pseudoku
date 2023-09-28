from dataclasses import dataclass

@dataclass
class Colour:
    rgb: tuple[int, int, int]
    hex: str

    def __post_init__(self):
        self.hex = self.hex.upper()

    @staticmethod
    def from_hex(hex: str) -> "Colour":
        return Colour(tuple(int(hex.casefold()[1:][i:i + 2], 16) for i in (0, 2, 4)), hex.casefold())

    @staticmethod
    def from_rgb(rgb: tuple[int, int, int]) -> "Colour":
        return Colour(rgb, "#"+"".join(f"{c:02x}" for c in rgb))


    @staticmethod
    def from_dict(colour_dict: dict[str, str]) -> "Colour":
        return Colour.from_hex(colour_dict["hex"])

    to_hex = lambda self: self.hex
    to_rgb = lambda self: self.rgb
    to_dict = lambda self: {"hex": self.hex, "rgb": self.rgb}

    # @staticmethod
    # def from_hsv(hsv: tuple[int, int, int]) -> "Colour":
    #     h, s, v = hsv
    #     c = v * s
    #     x = c * (1 - abs((h / 60) % 2 - 1))
    #     m = v - c
    #
    #     if h < 60:
    #         r, g, b = c, x, 0
    #     elif h < 120:
    #         r, g, b = x, c, 0
    #     elif h < 180:
    #         r, g, b = 0, c, x
    #     elif h < 240:
    #         r, g, b = 0, x, c
    #     elif h < 300:
    #         r, g, b = x, 0, c
    #     elif h < 360:
    #         r, g, b = c, 0, x
    #     else:
    #         # Subtract 360 from h until it is in the range [0, 360)
    #         while h >= 360:
    #             h -= 360
    #         return Colour.from_hsv((h, s, v))
    #
    #     return Colour.from_rgb(tuple(int((c + m) * 255) for c in (r, g, b)))

    # def COMPLEMENTARY(self) -> "Colour":
    #     return Colour.from_rgb(tuple(255 - c for c in self.rgb))
    #
    # def to_hsv(self) -> tuple[int, int, int]:
    #     r, g, b = (c / 255 for c in self.rgb)
    #     c_max = max(r, g, b)
    #     c_min = min(r, g, b)
    #     delta = c_max - c_min
    #
    #     if delta == 0:
    #         h = 0
    #     elif c_max == r:
    #         h = 60 * (((g - b) / delta) % 6)
    #     elif c_max == g:
    #         h = 60 * (((b - r) / delta) + 2)
    #     elif c_max == b:
    #         h = 60 * (((r - g) / delta) + 4)
    #
    #     s = 0 if c_max == 0 else delta / c_max
    #     v = c_max
    #
    #     return h, s, v
    #
    # def TRIAD(self) -> tuple["Colour", "Colour"]:
    #     h, s, v = self.to_hsv()
    #     print(h, s, v)
    #     return Colour.from_hsv((h + 120, s, v)), Colour.from_hsv((h + 240, s, v))
