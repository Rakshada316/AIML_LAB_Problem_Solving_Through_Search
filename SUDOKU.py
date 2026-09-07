# Sudoku Solver using CSP and Backtracking

board = []

print("Enter Sudoku puzzle row by row.")
print("Use 0 for empty cells.")

for i in range(9):
    row = list(map(int, input(f"Row {i + 1}: ").split()))
    board.append(row)


def find_empty_cell():
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return row, col

    return None


# Check whether placing a number is valid
def is_safe(row, col, number):

    # Check row
    for j in range(9):
        if board[row][j] == number:
            return False

    # Check column
    for i in range(9):
        if board[i][col] == number:
            return False

    # Check 3x3 box
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3

    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == number:
                return False

    return True


# CSP Backtracking
def solve_sudoku():

    # Find an empty cell
    empty = find_empty_cell()

    # No empty cell means Sudoku is solved
    if empty is None:
        return True

    row, col = empty

    # Try numbers 1 to 9
    for number in range(1, 10):

        # Check constraints
        if is_safe(row, col, number):

            # Assign number
            board[row][col] = number

            # Recursively solve
            if solve_sudoku():
                return True

            # Backtrack
            board[row][col] = 0

    return False


# Solve Sudoku
if solve_sudoku():

    print("\n--- Sudoku Solution ---")

    for row in board:
        print(*row)

else:
    print("\nNo solution exists.")