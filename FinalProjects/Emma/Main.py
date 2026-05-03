import Storm_Functions
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib.animation import PillowWriter
import os
from matplotlib.patches import Rectangle

n_array = [3, 4, 5]
leaf_count_array = []
total_heat_array = []
slice_heat_array = []
time_array_total = []

for n in n_array:

    grid_size = 512 # Fix it so we will always have a multiple of 8 for our octree
    center = [grid_size/2, grid_size/2, grid_size/2] 
    max_time = 10
    N = 10 # Number of times time is subdivided
    res = 512
    patches = []
    leaf_count = []
    time_array = []
    recorded_frames = []
    total_heat = []
    slice_heat = []

    dt = max_time / N # Step size for time
    t_array = np.linspace(0, max_time, N) # Time array for storm

    root = Storm_Functions.Node(center, grid_size, 0)
    Storm_Functions.build_tree(root, 2)

    hot_node, _ = Storm_Functions.find_node(root, center)
    hot_node.T = 100

    # Create scatter diagram
    fig, ax = plt.subplots()

    # Switched from scatter to 
    heatmap = ax.imshow(np.zeros((res, res)), # Data for our slice
                        extent=[0, grid_size, 0, grid_size], # Range we are plotting on
                        origin='lower',
                        cmap='hot', # for coloring,
                        interpolation='bicubic') # For blur, see source on different possibilities)

    ax.set_xlim(0, grid_size)
    ax.set_ylim(0, grid_size)
    ax.set_title("Storm Formation")
    heatmap.set_clim(0, 1)

    def update(frame):

        # Check time
        t = dt*frame

        # Find leaves of entire tree
        leaves = Storm_Functions.get_leaves(root) # Find all the leaves for your node

        # Cache neighbors back into node so its easier to update
        for leaf in leaves:
            leaf.neighbors = Storm_Functions.get_neighbors(root, leaf)

        # Update physics (Main weather component)

        Storm_Functions.diffuse(leaves, alpha=0.1)

        # Take a slice of our program. Only want xy frame at z's center
        slice_z = center[2]
        slice_thickness = grid_size * 0.1

        # Filter everything for our program
        filtered = [leaf for leaf in leaves if abs(leaf.center[2] - slice_z) < slice_thickness]

        # Reset our patches for each iteration 
        for p in patches:
            p.remove()
        patches.clear()

        grid = np.zeros((res, res)) # Total temperature
        count = np.zeros((res, res)) # How many leaves are contributing to a pixel

        # For every node that is a leaf in our filtered slice, create a rectangle to track the octree
        for leaf in filtered:
            x, y = leaf.center[0], leaf.center[1]
            T = leaf.T
            size = leaf.size
            weight = leaf.size**2 # Bigger leaves are more impactful

            # Convert our components into our new grid to be plotted
            # Convert leaf physical bounds to our grid so its cells instead of points
            i_start = int((x - size/2) / grid_size * res)
            i_end   = int((x + size/2) / grid_size * res)
            j_start = int((y - size/2) / grid_size * res)
            j_end   = int((y + size/2) / grid_size * res)

            # Ensure indices stay within the grid boundaries
            i_start, i_end = max(0, i_start), min(res, i_end)
            j_start, j_end = max(0, j_start), min(res, j_end)

            # Fill the entire cell area instead of just one point
            if i_start < i_end and j_start < j_end:
                grid[j_start:j_end, i_start:i_end] += T * weight
                count[j_start:j_end, i_start:i_end] += weight

            # Create rectangle to be used by matplotlib patches
            rect = Rectangle(
                (x - size/2, y - size/2),
                size,
                size,
                fill=False,
                edgecolor='white',
                linewidth=0.3,
                alpha=0.3)

            ax.add_patch(rect)
            patches.append(rect)

        mask = count > 0 # Grab a mask of all the pixels that have more than one leaf
        grid[mask] /= count[mask] # Average it out  

        # Normalize our grid of temperatures
        if np.max(grid) > 0:
            grid = grid / np.max(grid)

        grid = np.sqrt(grid) # Boost contrast
        heatmap.set_data(grid) # Give heatmap our data

        # Refine/Subdivide. 
        # Now that physics is done updating, check if anything has become a storm cell yet
        for leaf in leaves:
            if abs(leaf.T) > 0.4 and leaf.depth < n: # Replace this with your test
                Storm_Functions.subdivide(leaf, n)

        # Rebuild leaf list
        leaves = Storm_Functions.get_leaves(root)
        print(len(leaves))

        if frame not in recorded_frames:
            leaf_count.append(len(leaves))
            time_array.append(t)
            total_heat.append(sum(leaf.T * leaf.size** 3 for leaf in leaves))
            slice_heat.append(sum(leaf.T * leaf.size**2 for leaf in filtered))
            recorded_frames.append(frame)

        # Now repeat for each timestep
        return heatmap

    # Find file path 
    script_dir = os.path.dirname(os.path.abspath(__file__))
    gif_path = os.path.join(script_dir, f"animation_{n}.gif")

    # Create animation and save it as a gif titled "animation"
    ani = animation.FuncAnimation(fig, update, frames=300, interval=100, blit=False)
    ani.save(gif_path, writer=PillowWriter(fps=20), savefig_kwargs={"facecolor": "black"})
    plt.show()

    time_array_total.append(time_array)
    total_heat_array.append(total_heat)
    slice_heat_array.append(slice_heat)
    leaf_count_array.append(leaf_count)

fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()
fig3, ax3 = plt.subplots()

for time, leaf, total, slice, sub in zip(time_array_total, leaf_count_array, total_heat_array, slice_heat_array, n_array):

    leaf = np.array(leaf)
    total = np.array(total)
    slice = np.array(slice)

    leaf_norm = leaf / leaf[0]
    total_norm = total / total[0]
    slice_norm = slice / np.max(slice)

    ax1.plot(time, leaf_norm, label=f"Depth: {sub}")
    ax2.plot(time, total_norm, label=f"Depth: {sub}")
    ax3.plot(time, slice_norm, label=f"Depth: {sub}")

ax1.set_xlabel("Time")
ax1.set_ylabel("Leaf Count")
ax1.set_title("Leaf Count vs Time")
ax1.set_yscale('log')

ax2.set_xlabel("Time")
ax2.set_ylabel("Total Heat")
ax2.set_title("Total Heat vs Time")

ax3.set_xlabel("Time")
ax3.set_ylabel("Slice Heat")
ax3.set_title("Slice Heat vs Time")

ax1.legend()
ax2.legend()
ax3.legend()
plt.show()
