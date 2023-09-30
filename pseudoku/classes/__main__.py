from .colour import Colour

navy_blue = Colour.from_hex("#3900E3")
light_bg = Colour.from_hex("#b796f8")
light_comp = Colour.from_hex("#aae300")
light_triad = Colour.from_hex("#e33900")

print(
    f"navy_blue: {navy_blue}\n"
    f"light_bg: {light_bg}\n"
    f"light_comp: {light_comp}\n"
    f"light_triad: {light_triad}\n"
)


print(Colour.from_rgb(navy_blue.to_rgb()).to_hex())
print(Colour.from_hex(navy_blue.to_hex()).to_hex())
