# Function to check if a queen can be placed at board[row][col]
def is_position_safe(chessboard, row, col, size):
    # Check this row on left side for any queens
    for i in range(col):
        if chessboard[row][i] == 1:
            return False  # Return False if a queen is found

    # Check upper diagonal on left side for any queens
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if chessboard[i][j] == 1:
            return False  # Return False if a queen is found

    # Check lower diagonal on left side for any queens
    for i, j in zip(range(row, size, 1), range(col, -1, -1)):
        if chessboard[i][j] == 1:
            return False  # Return False if a queen is found

    return True  # Return True if no queens are found, and it's safe to place a queen

# Function to solve the N Queen problem using backtracking
def place_queens(chessboard, col, size, solutions):
    # Base case: If all queens are placed, add the board to the solutions
    if col >= size:
        solutions.append([' '.join(str(i) for i in row) for row in chessboard])
        return

    # Try placing a queen in each row of the current column
    for i in range(size):
        if is_position_safe(chessboard, i, col, size):
            chessboard[i][col] = 1  # Place a queen at the current position

            # Recur to place the rest of the queens
            place_queens(chessboard, col + 1, size, solutions)

            # If placing queen doesn't lead to a solution, remove the queen (backtrack)
            chessboard[i][col] = 0

# Function to print all solutions
def display_solutions(all_solutions):
    for solution in all_solutions:
        for row in solution:
            print(row)  # Print each row of the board
        print()  # Print a newline after each solution

# Driver code to test the above functions
print("Enter the number of queens")
board_size = int(input())
print()
if board_size in [2,3]: print("No solution exists for {}*{} board!".format(board_size,board_size))
chessboard = [[0 for _ in range(board_size)] for _ in range(board_size)]  # Initialize the board with all zeros
all_solutions = []  # List to store all the possible solutions
place_queens(chessboard, 0, board_size, all_solutions)  # Generate all solutions
display_solutions(all_solutions)  # Print all the solutions
