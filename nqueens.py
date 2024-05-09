# Function to check if placing a queen at position (row, col) is safe
def is_safe(row, col):
    # Check if there is a queen in the same row or column
    for i in range(N):
        if chessboard[row][i] == 1 or chessboard[i][col] == 1:
            return False
    # Check diagonals
    for i in range(N):
        for j in range(N):
            if (i + j == row + col) or (i - j == row - col):
                if chessboard[i][j] == 1:
                    return False
    return True

# Function to solve N Queens problem using backtracking
def solve_n_queens(num_queens):
    # Base case: if all queens are placed, return True
    if num_queens == 0:
        return True
    # Try placing a queen in each row
    for row in range(N):
        for col in range(N):
            # Check if it's safe to place a queen at (row, col)
            if is_safe(row, col) and chessboard[row][col] != 1:
                # Place the queen at (row, col)
                chessboard[row][col] = 1
                # Recur to place rest of the queens
                if solve_n_queens(num_queens - 1):
                    return True
                # If placing queen at (row, col) doesn't lead to a solution, backtrack
                chessboard[row][col] = 0
    return False

# Get input for number of queens
print("Enter the number of queens")
num_queens = int(input())

# Initialize the chessboard
chessboard = [[0] * num_queens for _ in range(num_queens)]

# Set the number of queens globally
N = num_queens

# Call the function to solve N Queens problem
if solve_n_queens(num_queens):
    # Print the solution
    for row in chessboard:
        print(row)
else:
    print("No solution exists for {} queens".format(num_queens))



'''
# Function to check if placing a queen at position (row, col) is safe
def is_safe(row, col):
    # Check each position in the same row and column for a queen
    for i in range(N):
        if chessboard[row][i] == 1 or chessboard[i][col] == 1:
            return False  # Return False if a queen is found in the same row or column
    # Check diagonals for a queen
    for i in range(N):
        for j in range(N):
            # Check if the position is on a diagonal of the current position (row, col)
            if (i + j == row + col) or (i - j == row - col):
                if chessboard[i][j] == 1:
                    return False  # Return False if a queen is found on a diagonal
    return True  # Return True if no queens are found in the same row, column, or diagonal

# Function to solve the N Queens problem using backtracking
def solve_n_queens(num_queens):
    # If all queens are placed, the problem is solved
    if num_queens == 0:
        return True
    # Try placing a queen in each cell of the board
    for row in range(N):
        for col in range(N):
            # Check if placing a queen at (row, col) is safe
            if is_safe(row, col) and board[row][col] != 1:
                chessboard[row][col] = 1  # Place the queen at (row, col)
                # Recursively attempt to place the rest of the queens
                if solve_n_queens(num_queens - 1):
                    return True  # If successful, return True
                chessboard[row][col] = 0  # If not, remove the queen and backtrack
    return False  # If no valid placement is found, return False

# Prompt the user to enter the number of queens
print("Enter the number of queens")
num_queens = int(input())  # Read the number of queens from the user

# Initialize the chessboard with all zeros (no queens placed)
chessboard = [[0] * num_queens for _ in range(num_queens)]

# Set the global variable N to the number of queens
N = num_queens

# Attempt to solve the N Queens problem
if solve_n_queens(num_queens):
    # If a solution is found, print the chessboard with queens placed
    for row in chessboard:
        print(row)
else:
    # If no solution exists, inform the user
    print("No solution exists for {} queens".format(num_queens))
'''
