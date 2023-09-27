from .colour import Colour

blurple = Colour.from_hex("#5865F2")
greyple = Colour.from_hex("#99AAB5")
print(blurple, greyple)

blurple = Colour.from_rgb((88, 101, 242))
greyple = Colour.from_rgb((153, 170, 181))

print(blurple, greyple)