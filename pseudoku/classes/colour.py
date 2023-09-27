from dataclasses import dataclass

@dataclass
class Colour:
    rgb: tuple[int, int, int]
    hex: str

    @staticmethod
    def from_hex(hex: str) -> "Colour":
        return Colour(tuple(int(hex.casefold()[1:][i:i + 2], 16) for i in (0, 2, 4)), hex.casefold())

    @staticmethod
    def from_rgb(rgb: tuple[int, int, int]) -> "Colour":
        return Colour(rgb, "#"+"".join(f"{c:02x}" for c in rgb))


    @staticmethod
    def from_dict(colour_dict: dict[str, str]) -> "Colour":
        return Colour.from_hex(colour_dict["hex"])
