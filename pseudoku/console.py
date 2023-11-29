from sudoku import Sudoku


def print_grid(sudoku):
    print("Sudoku Grid:")
    print(sudoku)


def main():
    print("Welcome to Sudoku!")
    difficulty = int(input("Enter difficulty level (0-10): "))

    sudoku = Sudoku.generate(difficulty)
    print_grid(sudoku)

    while not sudoku.is_solved():
        print(
            "\nEnter 'x y value' to set a value (e.g., '2 3 5'), 'solve' to auto-solve, 'step' for one step, "
            "or 'exit' to quit:"
        )
        user_input = input("> ")

        if user_input.lower() == "exit":
            print("Exiting...")
            return

        elif user_input.lower() == "solve":
            if sudoku.solve():
                print("Sudoku Solved!")
                print_grid(sudoku)
                return
            else:
                print("Unable to solve this Sudoku.")

        elif user_input.lower() == "step":
            move = sudoku.solve_one_step()
            if move != (-1, -1, -1):
                print(f"Solving one step: Set {move[2]} at ({move[0]+1}, {move[1]+1})")
                print_grid(sudoku)
            else:
                print("No valid move available in this step.")

        else:
            try:
                x, y, value = map(int, user_input.split())
                if 1 <= x <= 9 and 1 <= y <= 9 and 1 <= value <= 9:
                    sudoku.set(x - 1, y - 1, value - 1, value)
                    print_grid(sudoku)
                else:
                    print(
                        "Invalid input! Please enter valid coordinates (1-9) and value (1-9)."
                    )
            except ValueError:
                print(
                    "Invalid input! Please enter 'x y value', 'solve', 'step', or 'exit'."
                )
            except IndexError:
                print(
                    "Invalid input! Please enter valid coordinates (1-9) and value (1-9)."
                )


if __name__ == "__main__":
    main()
