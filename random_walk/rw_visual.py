import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making new walks as long as the program is active.
flag = True
while flag:
    # Make a random walk.
    rw = RandomWalk(10_000)

    rw.fill_walk()

    # Plot the points in the walk
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(15, 9))
    point_number = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_number, cmap=plt.cm.Blues,
               edgecolor='none', s=5)

    # Emphasize the first and last points.
    ax.scatter(0, 0, c='green', edgecolor='none', s=50)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none',
               s=50)

    # Remove the axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input('Make another walk? (y/n): ')
    if keep_running == 'n':
        flag = False
else:
    print('Exiting simulation.')
