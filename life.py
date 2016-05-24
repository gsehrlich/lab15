import numpy as np
from _run_life import run_life

# The size of the board
n = 40

# Fill the board randomly (but with a known seed for repeatability)
np.random.seed(1)
board = [[np.random.randint(0, 2) for i in range(n)] for j in range(n)]

def is_neighbor(i1, j1, i2, j2):
    """Return True if (i1, j1) is a neighbor of (i2, j2)"""
    if abs(i1 - i2) <= 1 and abs(j1 - j2) <= 1 and (
        i1 != i2 or j1 != j2):
        return True
    else:
        return False

def get_n_alive_neighbors(board, i, j):
    """Return the number of neighbors of (i, j) that are alive"""
    n_alive_neighbors = 0
    # Go through all the positions on the board and add up how many
    # alive ones there are, but only if they're neighbors
    for i_neighbor in range(n):
        for j_neighbor in range(n):
                neighbor_val = board[i_neighbor][j_neighbor]
                if is_neighbor(i, j, i_neighbor, j_neighbor):
                    n_alive_neighbors += neighbor_val

    return n_alive_neighbors

def update_v0(board):
    """Calculate the next board from the current board"""
    # Create the board at t+1 and zero-fill it
    next_board = [[0 for i in range(n)] for j in range(n)]

    # Figure out what to do to each cell
    for i in range(n):
        for j in range(n):
            n_alive_neighbors = get_n_alive_neighbors(board, i, j)

            # Apply live/die rules
            if board[i][j] == 1:
                if n_alive_neighbors in (2, 3):
                    next_board[i][j] = 1
                else:
                    next_board[i][j] = 0

            if board[i][j] == 0:
                if n_alive_neighbors == 3:
                    next_board[i][j] = 1
                else:
                    next_board[i][j] = 0

    # Copy the next board into the current board
    for i in range(n):
        for j in range(n):
            board[i][j] = next_board[i][j]

def update_v1(board):
    pass # WRITE CODE HERE

# CHANGE THIS WHEN YOU'VE FINISHED update_v1
update = update_v0

if __name__ == '__main__':
    run_life(board, update, n_steps=20, plot=True)