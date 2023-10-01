import random


def is_valid(board, row, col, num):
    return (
        all(board[row][i] != num for i in range(9))
        and all(board[i][col] != num for i in range(9))
        and all(
            board[row // 3 * 3 + i][col // 3 * 3 + j] != num
            for i in range(3)
            for j in range(3)
        )
    )


def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True


def generate_sudoku():
    board = [[0 for _ in range(9)] for _ in range(9)]
    solve_sudoku(board)

    empty_cells = random.sample(range(81), 40)
    for idx in empty_cells:
        row, col = divmod(idx, 9)
        board[row][col] = 0

    return board


def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(board[i][j], end=" ")
        print()


def is_valid_solution(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return False
            num = board[i][j]
            board[i][j] = 0
            if not is_valid(board, i, j, num):
                return False
            board[i][j] = num
    return True


def play_sudoku():
    sudoku_board = generate_sudoku()
    print("Generated Sudoku Board:")
    print_board(sudoku_board)

    while True:
        print(
            "\nEnter row, column, and number (space-separated) to fill a cell (e.g., 3 4 7):"
        )
        try:
            row, col, num = map(int, input().split())
            if 1 <= row <= 9 and 1 <= col <= 9 and 1 <= num <= 9:
                if sudoku_board[row - 1][col - 1] == 0:
                    sudoku_board[row - 1][col - 1] = num
                    print("\nUpdated Sudoku Board:")
                    print_board(sudoku_board)
                else:
                    print("Cell is already filled. Try again.")
            else:
                print("Invalid input. Please enter valid row, column, and number.")
        except ValueError:
            print("Invalid input format. Please enter row, column, and number.")

        if is_valid_solution(sudoku_board):
            print("\nCongratulations! You solved the Sudoku puzzle.")
            break


if __name__ == "__main__":
    play_sudoku()
