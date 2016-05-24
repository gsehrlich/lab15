import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def run_life(board, update, n_steps=20, plot=False):
    if plot:
        fig = plt.figure()
        im = plt.imshow(board, interpolation='nearest')
        plt.title("The Game of Life")
        plt.axis('off')
        is_first_step = [True]
        def update_im(dt, im):
            update(board)
            im.set_data(board)
        anim = FuncAnimation(fig, update_im, frames=n_steps, fargs=(im,),
            init_func=lambda: None, interval=50, blit=False, repeat=False)
        plt.show()

    else:
        for t in range(n_steps):
            update_fn(board)