import pygame
from .classes import Settings, settings as stngs
from .sudoku import Sudoku


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
        self.border_colour = settings.theme.complementary_colour
        self.num_font = settings.theme.number_font
        print(self.num_font)
        print(dir(self.num_font))
        self.border_width = 5
        self.set_display(x, y, size)
        self.generate_sudoku()
        print(size)

    def set_display(self, x: int, y: int, size: tuple[int, int] = None):
        self.x = x
        self.y = y
        self.width = size[0] * self.num_font.font_size + 2 * self.border_width
        self.height = size[1] * self.num_font.font_size + 2 * self.border_width
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.rect.center = (self.x, self.y)

    def draw(self):
        # This draws the sudoku grid normally
        pygame.draw.rect(
            self.screen, self.border_colour.rgb, self.rect, self.border_width
        )

        # Draw the 3x3 grid lines inside the sudoku grid, centered within the rectangle
        for i in range(1, 3):
            pygame.draw.line(
                self.screen,
                self.border_colour.rgb,
                (
                    self.rect.centerx - self.width // 2 + i * self.width // 3,
                    self.rect.top,
                ),
                (
                    self.rect.centerx - self.width // 2 + i * self.width // 3,
                    self.rect.bottom,
                ),
                self.border_width,
            )
            pygame.draw.line(
                self.screen,
                self.border_colour.rgb,
                (
                    self.rect.left,
                    self.rect.centery - self.height // 2 + i * self.height // 3,
                ),
                (
                    self.rect.right,
                    self.rect.centery - self.height // 2 + i * self.height // 3,
                ),
                self.border_width,
            )

        # Draw the cell borders with smaller width, centered within the rectangle
        cell_border_width = self.border_width // 3
        for i in range(1, 9):
            if i % 3 != 0:
                pygame.draw.line(
                    self.screen,
                    self.border_colour.rgb,
                    (
                        self.rect.centerx - self.width // 2 + i * self.width // 9,
                        self.rect.top,
                    ),
                    (
                        self.rect.centerx - self.width // 2 + i * self.width // 9,
                        self.rect.bottom,
                    ),
                    cell_border_width,
                )
                pygame.draw.line(
                    self.screen,
                    self.border_colour.rgb,
                    (
                        self.rect.left,
                        self.rect.centery - self.height // 2 + i * self.height // 9,
                    ),
                    (
                        self.rect.right,
                        self.rect.centery - self.height // 2 + i * self.height // 9,
                    ),
                    cell_border_width,
                )

        # Draw the numbers
        for i in range(9):
            for j in range(9):
                if self.matrix[i][j] != 0:
                    text = self.num_font.render(
                        str(self.matrix[i][j]), self.settings.theme.background_colour, True
                    )
                    text_rect = text.get_rect(
                        center=(
                            self.rect.centerx - self.width // 2 + j * self.width // 9
                            + self.width // 18,
                            self.rect.centery - self.height // 2 + i * self.height // 9
                            + self.height // 18,
                        )
                    )
                    self.screen.blit(text, text_rect)

    def generate_sudoku(self):
        pass

    def update(self):
        pass

    def repos(self, x: int, y: int, size: tuple[int, int] = None):
        self.set_display(x, y, size)


if __name__ == "__main__":
    pass
