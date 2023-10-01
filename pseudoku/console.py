import random


def solve_sudoku(board, iterations=1):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if ai_is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board, iterations + 1):
                            return True
                        board[row][col] = 0
                return False

    print(f"Solved in {iterations} iterations")
    return True


def calculate_empty_cells(difficulty):
    if 1 <= difficulty <= 3:
        return random.randint(48, 54)
    elif 4 <= difficulty <= 6:
        return random.randint(36, 47)
    elif 7 <= difficulty <= 8:
        return random.randint(27, 35)
    elif difficulty == 9:
        return random.randint(18, 26)
    elif difficulty == 10:
        return random.randint(9, 17)
    else:
        return random.randint(36, 54)


def generate_sudoku(difficulty):
    board = [[0 for _ in range(9)] for _ in range(9)]
    solve_sudoku(board)

    empty_cells = calculate_empty_cells(difficulty)
    empty_cells = min(empty_cells, 81)
    empty_positions = random.sample(range(81), empty_cells)

    for idx in empty_positions:
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
            if not ai_is_valid(board, i, j, num):
                return False
            board[i][j] = num
    return True


def play_sudoku():
    print("Choose the difficulty level (1 to 10, where 1 is easy and 10 is hardest):")
    try:
        difficulty = int(input("Enter the difficulty level: "))
        if not (1 <= difficulty <= 10):
            print("Invalid difficulty level. Using default difficulty (medium).")
            difficulty = 5
    except ValueError:
        print("Invalid input. Using default difficulty (medium).")
        difficulty = 5

    sudoku_board = generate_sudoku(difficulty)
    print(f"\nGenerated Sudoku Board (Difficulty Level: {difficulty}):")
    print_board(sudoku_board)

    while True:
        print("\nEnter 'q' to quit or 's' to solve with AI:")
        choice = input().strip().lower()

        if choice == "q":
            break
        elif choice == "s":
            solve_with_ai(sudoku_board)
        else:
            print("Invalid choice. Please try again.")


def ai_is_valid(board, row, col, num):
    return (
        all(board[row][i] != num for i in range(9))
        and all(board[i][col] != num for i in range(9))
        and all(
            board[row // 3 * 3 + i][col // 3 * 3 + j] != num
            for i in range(3)
            for j in range(3)
        )
    )


def ai_solver(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if ai_is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return  # Puzzle is solved, exit the function
                        board[row][col] = 0


def solve_with_ai(board):
    print(board)
    ai_solver(board)
    print("Sudoku puzzle solved:")
    print_board(board)
    print(board)
    quit()


if __name__ == "__main__":
    play_sudoku()
