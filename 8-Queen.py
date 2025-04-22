# Size of the chessboard (N x N)
N = 8

# This function attempts to solve the N-Queens problem starting from the given column
def solveNQueens(board, col):
	# If all queens are placed, print the board and return True
	if col == N:
		printBoard(board)  # Print board nicely instead of raw list
		return True

	# Try placing a queen in all rows one by one in the current column
	for i in range(N):
		# Check if placing a queen at (i, col) is safe
		if isSafe(board, i, col):
			# Place the queen
			board[i][col] = 1

			# Recur to place the rest of the queens
			if solveNQueens(board, col + 1):
				return True  # If success, no need to continue

			# Backtrack: remove the queen if placing at (i, col) leads to no solution
			board[i][col] = 0

	# If queen cannot be placed in any row in this column, return False
	return False

# This function checks if a queen can be safely placed at board[row][col]
def isSafe(board, row, col):
	# Check the row on the left side
	for x in range(col):
		if board[row][x] == 1:
			return False

	# Check the upper-left diagonal
	for x, y in zip(range(row, -1, -1), range(col, -1, -1)):
		if board[x][y] == 1:
			return False

	# Check the lower-left diagonal
	for x, y in zip(range(row, N, 1), range(col, -1, -1)):
		if board[x][y] == 1:
			return False

	# If all checks pass, the position is safe
	return True

# Helper function to print the board in a clean format
def printBoard(board):
	for row in board:
		print(" ".join("Q" if cell == 1 else "." for cell in row))
	print()

# Create an empty N x N board filled with 0s (no queens placed)
board = [[0 for x in range(N)] for y in range(N)]

# Try to solve the N-Queens problem starting from column 0
if not solveNQueens(board, 0):
	print("No solution found")
