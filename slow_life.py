import numpy as np
import pyglet

n = 100

# fill the board randomly (but with a known seed for repeatability)
np.random.seed(1)
board = [[np.random.randint(0, 2) for i in range(n)] for j in range(n)]

"""
# the smarter way to do it
def get_nbhd(i, j, board):
    "Return the list of coordinates of neighbors of i, j"
    return [(i + di, j + dj) for di in (-1, 0, 1) for dj in (-1, 0, 1)
        if di != or dj != 0]
"""

def is_neighbor(i1, j1, i2, j2):
    if i1 == i2 and abs(j1 - j2) == 1:
        return True
    elif j1 == j2 and abs(i1 - i2) == 1:
        return True
    else:
        return False

def live_or_die(board):
    fate_board = [[0]*n]*n # zero-fill another board of same size

    # go through the whole board, cell by cell
    for i in range(n):
        for j in range(n):
            n_alive_neighbors = 0
            # go through all the positions on the board and add up how many
            # alive ones there are, but only if they're neighbors
            for i_neighbor in range(n):
                for j_neighbor in range(n):
                    neighbor_val = board[i_neighbor][j_neighbor]
                    if is_neighbor(i, j, i_neighbor, j_neighbor):
                        n_alive_neighbors += neighbor_val

            # determine whether cell lives or dies
            if board[i][j] == 1:
                if n_alive_neighbors in (2, 3):
                    fate_board[i][j] == 1
                else:
                    fate_board[i][j] == 0

            if board[i][j] == 0:
                if n_alive_neighbors == 3:
                    fate_board[i][j] == 1
                else:
                    fate_board[i][j] == 0

    return fate_board

def do_life(n_steps=100, plot=False):
    if plot:

        pyglet.app.run()
        plot(board)

    for t in range(n_steps):
        fate_board = live_or_die(board)
        # update the board
        for i in range(n):
            for j in range(n):
                board[i][j] = fate_board[i][j]

        if plot:
            plot(board)

def plot(board):
    raise NotImplementedError

if __name__ == '__main__':
    do_life()