from .colour import Colour

navy_blue = Colour.from_hex("#3900E3")
light_bg = Colour.from_hex("#b796f8")
light_comp = Colour.from_hex("#aae300")
light_triad = Colour.from_hex("#e33900")

def test_rgb_to_hex():
    assert Colour.from_rgb((57, 0, 227)).to_hex() == "#3900E3".upper()
    assert Colour.from_rgb((183, 150, 248)).to_hex() == "#b796f8".upper()
    assert Colour.from_rgb((170, 227, 0)).to_hex() == "#aae300".upper()
    assert Colour.from_rgb((227, 57, 0)).to_hex() == "#e33900".upper()

def test_hex_to_rgb():
    assert Colour.from_hex("#3900E3").to_rgb() == (57, 0, 227)
    assert Colour.from_hex("#b796f8").to_rgb() == (183, 150, 248)
    assert Colour.from_hex("#aae300").to_rgb() == (170, 227, 0)
    assert Colour.from_hex("#e33900").to_rgb() == (227, 57, 0)

def test_p():
    print(navy_blue)
    print(light_comp)
    print(light_bg)
    print(light_triad)

if __name__ == "__main__":
    test_rgb_to_hex()
    test_hex_to_rgb()
    test_p()
    print("All tests passed!")

