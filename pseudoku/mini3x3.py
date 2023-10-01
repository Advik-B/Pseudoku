from pygame.sprite import Sprite
from pygame import Surface
from pygame import draw
from pygame import Rect
from pygame import font
from .classes import Settings, Matrix


class Mini3x3(Sprite):
    def __init__(self, settings: Settings, x: int, y: int, matrix: Matrix):
        super().__init__()
        self.settings = settings
        self.x = x
        self.y = y
        self.width = settings.width // 3
        self.height = settings.height // 3
        self.rect = Rect(x, y, self.width, self.height)
        self.mini_matrix = matrix
        self.image = Surface((self.width, self.height))

    def draw(self) -> None:
        self.image.fill(self.settings.theme.background_colour.rgb)
        self.draw_grid()
        self.draw_numbers()

    def draw_grid(self) -> None:
        for i in range(1, 3):
            draw.line(
                self.image,
                self.settings.theme.triad_colour.rgb,
                (0, self.height // 3 * i),
                (self.width, self.height // 3 * i),
                1,
            )
            draw.line(
                self.image,
                self.settings.theme.triad_colour.rgb,
                (self.width // 3 * i, 0),
                (self.width // 3 * i, self.height),
                1,
            )

    def draw_numbers(self) -> None:
        for i in range(3):
            for j in range(3):
                if self.mini_matrix[i][j] == 0:
                    continue
                text = self.settings.theme.number_font.render(
                    str(self.mini_matrix[i][j]),
                    True,
                    self.settings.theme.number_font.colour,
                )

                text_rect = text.get_rect()
                text_rect.center = (
                    self.width // 3 * j + self.width // 6,
                    self.height // 3 * i + self.height // 6,
                )
                self.image.blit(text, text_rect)
