import itertools
import pygame
import random

# Define constants
WINDOW_SIZE = 540
GRID_SIZE = 9
CELL_SIZE = WINDOW_SIZE // GRID_SIZE

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)

class Cell:
    def __init__(self, row, col, value=0):
        self.row = row
        self.col = col
        self.value = value
        self.editable = value == 0

    def draw(self, screen):
        font = pygame.font.Font(None, 36)
        if self.value != 0:
            text = font.render(str(self.value), True, BLACK)
        else:
            text = font.render("", True, BLACK)
        screen.blit(text, (self.col * CELL_SIZE + 15, self.row * CELL_SIZE + 15))


class SudokuGrid:
    def __init__(self):
        self.grid_ = [[Cell(row, col) for col in range(GRID_SIZE)] for row in range(GRID_SIZE)]
        self.grid_ = self.generate_sudoku()

    def generate_sudoku(self):
        grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        self.solve(grid)

        # Remove random cells to create the puzzle
        for _ in range(30):
            row, col = random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)
            grid[row][col] = 0

        print(grid)
        return grid

    def solve(self, grid):
        for row, col in itertools.product(range(GRID_SIZE), range(GRID_SIZE)):
            if grid[row][col] == 0:
                for num in range(1, GRID_SIZE + 1):
                    if self.is_valid(grid, row, col, num):
                        grid[row][col] = num

                        if self.solve(grid):
                            return True

                        grid[row][col] = 0

                return False

        return True

    def draw(self, screen):
        for i in range(GRID_SIZE + 1):
            pygame.draw.line(screen, BLACK, (0, i * CELL_SIZE), (WINDOW_SIZE, i * CELL_SIZE), 2)
            pygame.draw.line(screen, BLACK, (i * CELL_SIZE, 0), (i * CELL_SIZE, WINDOW_SIZE), 2)

        for row in self.grid_:
            for cell in row:
                cell.draw(screen)  # Corrected to call the Cell's draw method

    def is_valid(self, grid, row, col, num):
        for i in range(GRID_SIZE):
            if grid[row][i] == num or grid[i][col] == num:
                return False

        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        return all(
            grid[i + start_row][j + start_col] != num
            for i, j in itertools.product(range(3), range(3))
        )


class SudokuGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
        pygame.display.set_caption('Sudoku')
        self.clock = pygame.time.Clock()
        self.sudoku_grid = SudokuGrid()
        self.running = True

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # Clear the screen
            self.screen.fill(WHITE)

            # Draw the Sudoku grid
            self.sudoku_grid.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(30)

        pygame.quit()


if __name__ == "__main__":
    game = SudokuGame()
    game.run()
