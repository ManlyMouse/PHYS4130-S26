import Storm_Functions
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib.animation import PillowWriter
import os
from matplotlib.patches import Rectangle

n = 3
grid_size = 8**n # Fix it so we will always have a multiple of 8 for our octree
center = [grid_size/2, grid_size/2, grid_size/2] 
max_time = 10
N = 10 # Number of times time is subdivided
patches = []

dt = max_time / N # Step size for time
t_array = np.linspace(0, max_time, N) # Time array for storm

# 

root = Storm_Functions.Node(center, grid_size, 0)
Storm_Functions.build_tree(root, 3)
leaves = Storm_Functions.get_leaves(root)
print(len(leaves))

# Spawn a heat bubble at the center object of our leaf list. 
leaves[1].T = 100

fig, ax = plt.subplots()
scat = ax.scatter(
    [0], [0],
    c=[0],
    cmap='hot',
    vmin=0,
    vmax=1
)

ax.set_xlim(0, grid_size)
ax.set_ylim(0, grid_size)
ax.set_title("Storm Formation")

def update(frame):

    # Find leaves of entire tree
    leaves = Storm_Functions.get_leaves(root) # Find all the leaves for your node

    # Cache neighbors back into node so its easier to update
    for leaf in leaves:
        leaf.neighbors = Storm_Functions.get_neighbors(root, leaf)

    # Update physics (Main weather component)

    Storm_Functions.diffuse(leaves, alpha=0.1)

    # Take a slice of our program
    slice_z = center[2]
    slice_thickness = grid_size * 0.1

    filtered = [leaf for leaf in leaves if abs(leaf.center[2] - slice_z) < slice_thickness]

    for p in patches:
        p.remove()
    patches.clear()

    for leaf in filtered:
        x, y = leaf.center[0], leaf.center[1]
        size = leaf.size

        rect = Rectangle(
            (x - size/2, y - size/2),
            size,
            size,
            fill=False)

        ax.add_patch(rect)
        patches.append(rect)

    # Extract positions + temperature
    xs = [leaf.center[0] for leaf in filtered]
    ys = [leaf.center[1] for leaf in filtered]
    temps = np.array([leaf.T for leaf in filtered])

    if len(temps) > 0:
        tmin, tmax = temps.min(), temps.max()

        if tmax - tmin < 1e-12:
            temps = np.zeros_like(temps)
        else:
            temps = (temps - tmin) / (tmax - tmin)

    print("leaves:", len(leaves))
    print("filtered:", len(filtered))

    scat.set_offsets(np.column_stack((xs, ys)))
    scat.set_array(np.array(temps))

    print("T range:", np.min(temps), np.max(temps), "std:", np.std(temps))


    # Refine/Subdivide. 
    # Now that physics is done updating, check if anything has become a storm cell yet
    for leaf in leaves:
        if abs(leaf.T) > 0.2 and leaf.depth < n:
            Storm_Functions.subdivide(leaf, n)

    # Rebuild leaf list
    leaves = Storm_Functions.get_leaves(root)

    # Now repeat for each timestep
    return scat,

# Find file path 
script_dir = os.path.dirname(os.path.abspath(__file__))
gif_path = os.path.join(script_dir, f"animation.gif")

# Create animation and save it as a gif titled "animation"
ani = animation.FuncAnimation(fig, update, frames=200, interval=100, blit=False)
ani.save(gif_path, writer=PillowWriter(fps=20), savefig_kwargs={"facecolor": "black"})
plt.show()
    

