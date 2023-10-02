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
        self.border_colour = settings.theme.triad_colour
        self.border_width = 2
        self.x = x
        self.y = y
        self.width = 9 * self.font.font_size + 2 * self.border_width
        self.height = 9 * self.font.font_size + 2 * self.border_width
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.rect.center = (self.x, self.y)
        self.generate_sudoku()

    def draw(self):
        pygame.draw.rect(self.screen, self.border_colour, self.rect, self.border_width)
        for i in range(9):
            for j in range(9):
                if self.matrix[i][j] != 0:
                    text = self.font.render(
                        str(self.matrix[i][j]), self.border_colour, self.border_colour
                    )
                    text_rect = text.get_rect()
                    text_rect.center = (
                        self.x + (j + 0.5) * self.font.font_size,
                        self.y + (i + 0.5) * self.font.font_size,
                    )
                    self.screen.blit(text, text_rect)

    def generate_sudoku(self):
        pass

    def update(self):
        pass


if __name__ == "__main__":
    pass
