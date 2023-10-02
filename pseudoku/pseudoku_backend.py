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
    ):
        self.matrix = [[x for x in range(9)] for y in range(9)]
        self.difficulty = difficulty
        self.screen = screen
        if not settings:
            self.settings = stngs.DEFAULT
        self.font = settings.theme.number_font
        self.border_colour = settings.theme.complementary_colour
        self.border_width = 5
        self.x = x
        self.y = y
        self.width = 25 * self.font.font_size + 2 * self.border_width
        self.height = 25 * self.font.font_size + 2 * self.border_width
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.rect.center = (self.x, self.y)
        self.generate_sudoku()

    def draw(self):
        pygame.draw.rect(
            self.screen, self.border_colour.rgb, self.rect, self.border_width
        )

    def generate_sudoku(self):
        pass

    def update(self):
        pass


if __name__ == "__main__":
    pass
