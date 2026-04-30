import Storm_Functions
import numpy as np

n = 6
grid_size = 8**n # Fix it so we will always have a multiple of 8 for our octree
center = [grid_size/2, grid_size/2, grid_size/2] 
max_time = 10
N = 10 # Number of times time is subdivided

dt = max_time / N

t_array = np.linspace(0, max_time, N)

root = Storm_Functions.Node(center, grid_size, 0)


# Warm bubble (place somewhere lower?)

for t in range(t_array):
    print()
    # Update physics
    

    # Refine/Subdivide
     
     
    # Rebuild leaf list


    # Cache neighbors back into node
