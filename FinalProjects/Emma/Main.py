import Storm_Functions
import numpy as np
import matplotlib as plt

n = 6
grid_size = 8**n # Fix it so we will always have a multiple of 8 for our octree
center = [grid_size/2, grid_size/2, grid_size/2] 
max_time = 10
N = 10 # Number of times time is subdivided

dt = max_time / N

t_array = np.linspace(0, max_time, N)

root = Storm_Functions.Node(center, grid_size, 0)

fig, ax = plt.subplots()
scat = ax.scatter()
ax.set_xlim(0, grid_size)
ax.set_xlim(0, grid_size)
ax.title("Storm Formation")

def update(frame):

    # Find leaves of entire tree
    leaves = Storm_Functions.get_leaves(root) # Find all the leaves for your node

    # Cache neighbors back into node so its easier to update
    for leaf in leaves:
        neighborhood = Storm_Functions.get_neighbors(leaf)
        leaf.neighbors.update(neighborhood) # Update neighbors using update on leaf.neighbors dictionary

    # Update physics (Main weather component)

    for leaf in leaves:
        print()
    
    # Refine/Subdivide. 
    # Now that physics is done updating, check if anything has become a storm cell yet
    for leaf in leaves:
        if abs(leaf.T) > 2: # Redo for more specific score value
            Storm_Functions.subdivide(leaf, n)
        # elif abs(leaf.T) <= 2:
           # Storm_Functions.collapse(leaf, n)

    # Rebuild leaf list
    leaves = Storm_Functions.get_leaves(root)

    # Now repeat for each timestep
    

