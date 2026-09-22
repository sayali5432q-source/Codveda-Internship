def print_board(board):
    for row in board:
        print(" ".join(row))
    print()


def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col] == "Q":
            return False

    i = row - 1
    j = col - 1

    while i >= 0 and j >= 0:
        if board[i][j] == "Q":
            return False
        i -= 1
        j -= 1

    i = row - 1
    j = col + 1

    while i >= 0 and j < n:
        if board[i][j] == "Q":
            return False
        i -= 1
        j += 1

    return True


def solve_n_queens(board, row, n):
    if row == n:
        print("Solution:")
        print_board(board)
        return True

    found = False

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = "Q"

            if solve_n_queens(board, row + 1, n):
                found = True

            board[row][col] = "."

    return found


n = int(input("Enter the value of N: "))

if n <= 0:
    print("Please enter a positive number.")
else:
    board = [["." for _ in range(n)] for _ in range(n)]

    if not solve_n_queens(board, 0, n):
        print("No solution exists.")