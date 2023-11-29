import random


class Sudoku:
    def __init__(self, grid: list[list[int]]):
        self.grid = grid

    def best_move(self) -> tuple[int, int, int]:
        for row in range(9):
            for col in range(9):
                if self.grid[row][col] == 0:
                    for num in range(1, 10):
                        if self.is_valid_move(row, col, num):
                            return row, col, num
        return -1, -1, -1  # Return if no move is possible

    def is_valid_move(self, row: int, col: int, num: int) -> bool:
        return (
            self.is_valid_row(row, num)
            and self.is_valid_column(col, num)
            and self.is_valid_square(row - row % 3, col - col % 3, num)
        )

    def solve_one_step(self) -> tuple[int, int, int]:
        if not self.is_solved():
            row, col, num = self.best_move()
            if row != -1 and col != -1 and num != -1:
                self.grid[row][col] = num
                return row, col, num
        return -1, -1, -1  # Return if no move was made

    def is_valid_row(self, row: int, num: int) -> bool:
        return num not in self.grid[row]

    def is_valid_column(self, col: int, num: int) -> bool:
        return all(self.grid[row][col] != num for row in range(9))

    def is_valid_square(self, start_row: int, start_col: int, num: int) -> bool:
        for row in range(3):
            for col in range(3):
                if self.grid[row + start_row][col + start_col] == num:
                    return False
        return True

    def is_solved(self) -> bool:
        for row in range(9):
            for col in range(9):
                if self.grid[row][col] == 0:
                    return False
        return True

    def is_solvable(self) -> bool:
        return self.solve()

    def solve(self) -> bool:
        row, col, num = self.best_move()
        if row == -1 and col == -1 and num == -1:
            return True  # Puzzle solved
        for num in range(1, 10):
            if self.is_valid_move(row, col, num):
                self.grid[row][col] = num
                if self.solve():
                    return True
                self.grid[row][col] = 0  # Backtrack if the solution was not found
        return False

    def solve_step(self) -> bool:
        if not self.is_solved():
            row, col, num = self.best_move()
            if row != -1 and col != -1 and num != -1:
                self.grid[row][col] = num
                return True
        return False

    def at(self, x: int, y: int, index: int) -> int:
        return self.grid[3 * y + index // 3][3 * x + index % 3]

    def set(self, x: int, y: int, index: int, value: int) -> None:
        self.grid[3 * y + index // 3][3 * x + index % 3] = value

    def get_grid(self) -> list[list[int]]:
        return self.grid

    def score(self) -> int:
        # Example scoring: count the number of filled cells
        count = sum(1 for row in self.grid for cell in row if cell != 0)
        return count

    def __str__(self) -> str:
        # . if empty, number if filled
        # Also add a border around each 3x3 grid
        result = ""
        for row in range(9):
            if row % 3 == 0:
                result += "-------------------------\n"
            for col in range(9):
                if col % 3 == 0:
                    result += "| "
                result += f"{self.grid[row][col]} "
            result += "|\n"
        result += "-------------------------"
        return result

    @staticmethod
    def from_grid(grid: list[list[int]]) -> "Sudoku":
        return Sudoku(grid)

    @staticmethod
    def generate(difficulty: int = 0) -> "Sudoku":
        def solve_sudoku(sudoku):
            row, col, num = sudoku.best_move()
            if row == -1 and col == -1 and num == -1:
                return True  # Puzzle solved
            for num in range(1, 10):
                if sudoku.is_valid_move(row, col, num):
                    sudoku.grid[row][col] = num
                    if solve_sudoku(sudoku):
                        return True
                    sudoku.grid[row][col] = 0  # Backtrack if the solution was not found
            return False

        def remove_cells(sudoku, num_cells):
            cells = [(i, j) for i in range(9) for j in range(9)]
            random.shuffle(cells)
            for i, j in cells:
                if sudoku.grid[i][j] != 0:
                    value = sudoku.grid[i][j]
                    sudoku.grid[i][j] = 0
                    temp_sudoku = Sudoku.from_grid([row[:] for row in sudoku.grid])
                    solutions = 0
                    solve_sudoku(temp_sudoku)
                    if temp_sudoku.is_solved():
                        solutions += 1
                    if solutions != 1 or not sudoku.is_solvable():
                        sudoku.grid[i][j] = value
                    else:
                        num_cells -= 1
                        if num_cells == 0:
                            return

        empty_grid = [[0 for _ in range(9)] for _ in range(9)]
        sudoku = Sudoku(empty_grid)
        solve_sudoku(sudoku)
        remove_cells(
            sudoku, max(30, difficulty * 5)
        )  # Adjust the number of cells to remove based on difficulty
        return sudoku
