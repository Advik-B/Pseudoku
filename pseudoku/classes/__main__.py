from .colour import Colour

navy_blue = Colour.from_hex("#3900E3")
light_bg = Colour.from_hex("#b796f8")
light_comp = Colour.from_hex("#aae300")
light_triad = Colour.from_hex("#e33900")

def test_rgb_to_hex():
    assert Colour.from_rgb((57, 0, 227)).hex == "#3900E3"
    assert light_bg.hex == "#b796f8"
    assert light_comp.hex == "#aae300"
    assert light_triad.hex == "#e33900"


print(navy_blue)
print(light_comp)
print(light_bg)
print(light_triad)

