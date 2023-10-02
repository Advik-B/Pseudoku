import pygame
from .classes import Settings, settings as stngs


class SudokuGrid:
    def __init__(
        self,
        difficulty: int = 10,
        x: int = 0,
        y: int = 0,
        screen: pygame.Surface = None,
        settings: Settings = None,
        size: tuple[int, int] = None,
    ):
        self.matrix = [[x for x in range(9)] for y in range(9)]
        self.difficulty = difficulty
        self.screen = screen
        if not settings:
            self.settings = stngs.DEFAULT
        else:
            self.settings = settings
        self.font = settings.theme.number_font
        self.border_colour = settings.theme.complementary_colour
        self.border_width = 5
        self.set_display(x, y, size)
        self.generate_sudoku()
        print(size)

    def set_display(self, x: int, y: int, size: tuple[int, int] = None):
        self.x = x
        self.y = y
        self.width = size[0] * self.font.font_size + 2 * self.border_width
        self.height = size[1] * self.font.font_size + 2 * self.border_width
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.rect.center = (self.x, self.y)

    def draw(self):
        pygame.draw.rect(
            self.screen, self.border_colour.rgb, self.rect, self.border_width
        )

    def generate_sudoku(self):
        pass

    def update(self):
        pass

    def repos(self, x: int, y: int, size: tuple[int, int] = None):
        self.set_display(x, y, size)


if __name__ == "__main__":
    pass
