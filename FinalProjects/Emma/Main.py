import Storm_Functions
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib.animation import PillowWriter
import os

n = 3
grid_size = 8**n # Fix it so we will always have a multiple of 8 for our octree
center = [grid_size/2, grid_size/2, grid_size/2] 
max_time = 10
N = 10 # Number of times time is subdivided

dt = max_time / N

t_array = np.linspace(0, max_time, N)

root = Storm_Functions.Node(center, grid_size, 0)
Storm_Functions.build_tree(root, 3)
leaves = Storm_Functions.get_leaves(root)
print(len(leaves))

leaves[len(leaves)//2].T = 100

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

    slice_z = center[2]

    slice_thickness = grid_size * 0.1

    filtered = [
    leaf for leaf in leaves
    if abs(leaf.center[2] - slice_z) < slice_thickness
]
    

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
    '''for leaf in leaves:
        if abs(leaf.T) > 2: # Redo for more specific score value
            Storm_Functions.subdivide(leaf, n)
        # elif abs(leaf.T) <= 2:
           # Storm_Functions.collapse(leaf, n)

    # Rebuild leaf list
    leaves = Storm_Functions.get_leaves(root)'''

    # Now repeat for each timestep
    return scat,

script_dir = os.path.dirname(os.path.abspath(__file__))

gif_path = os.path.join(script_dir, f"animation.gif")


ani = animation.FuncAnimation(fig, update, frames=2000, interval=300, blit=False)

ani.save(gif_path, writer=PillowWriter(fps=20), savefig_kwargs={"facecolor": "black"})
plt.show()
    

