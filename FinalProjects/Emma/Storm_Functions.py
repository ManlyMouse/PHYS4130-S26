import numpy as np
import random


class Node:
    '''
        Class: Node
        Description: Object class Node that will be used to subdivided the 3D space to make generation time much faster.
        Each node contains information on the center of the subdivision, the size of the cell, and 
        an empty array of children. After it is subdivided, this children array will be updated with more nodes. Additionally,
        this cell keeps track of all the fluid dynamic variables for the region.
    '''

    def __init__(self, center, size, depth):
        self.center = center
        self.size = size
        self.depth = depth
        self.leaf = True
        self.children = [None, None, None, None, None, None, None, None] # Produces 8 children for subdivision

        # Fluid dynamic variables
        self.u = 0 # Velocity for X axis
        self.v = 0 # Velocity for Y axis
        self.w = 0 # Velocity for Z axis
        self.omega = [0, 0 , 0] # Vorticity for x-, y-, z- directions
        self.T = 0 # Temperature 

        # Calculate the neighbors after each rebuilding of leaf list. Includes six neighbors on each cell's face.
        # This is to shorten number of loops we have to go through to calculate temperature gradients.
        # Only needs to be updated if we subdivide/collapse the octree
        self.neighbors = {
            'xm': None, # all labels of m means minus direction. So this is face on the negative x side
            'xp': None, # all labels of p means positive direction. So this is face on the positive x side
            'ym': None,
            'yp': None,
            'zm': None,
            'zp': None,
        }


def subdivide(node, depth_value, center, n):
    '''
        Takes a node and subdivides the grid into 8 more parts to create an octree. Quickens computing
        time by limiting the number of possible neighbors to calculate gradients for.

        Args:
            node (class): Object for center and grid of a region of our 3D space
            depth_value (int): Cutoff value for a nodes depth depending on starting grid size.

        Returns:
            None: Updates the nodes directly. Doesn't return anything. 
    '''

    if node.depth < n:
        node.leaf = False # It is no longer a leaf case. It has children now!!!
        depth = node.depth + 1 # Update depth
        grid_value = node.size / 2
        grid = [grid_value, grid_value, grid_value]
        
        offset_center = [-grid_value/2, grid_value/2] # Need to offset center for grid.

        child_index = 0
        for dx in offset_center:
            for dy in offset_center:
                for dz in offset_center:
                    center_x = node.center[0] + dx
                    center_y = node.center[1] + dy
                    center_z = node.center[2] + dz

                    node.children[child_index] = Node([center_x, center_y, center_z], grid, depth)
                    child_index += 1

        for child in node.children:
            subdivide(child, depth_value, center, n)


def find_node(root, point):
    '''
        Given a point this finds out with leaf node it is in and returns that node.

        Args:
            root (Object): Root node that is connected to all other nodes. Can transverse to find leaves.
            point (Array): Location of neighborhood.
        
        Returns:
            node (Object): Returns node of a certain location
            value (int): Index of child node for point location
    '''

    # From the wiki, we can use the color quantization program which determines the child node 
    # via the formula 4r + 2g + b, but here instead of red, green, and blue we can use 
    # our postive and negative 3 directions. Thus
    node = root

    value = 0
    # This will loop until it finds the leaf node to extract the particles
    while node.leaf != True:
        value = 0

        if  point[0] >= node.center[0]:
            value |= 4
        if point[1] >= node.center[1]:
            value |= 2
        if point[2] >= node.center[2]:
            value |= 1
        
        # Example: Say we said yes to all three if statements. Then we have 7 and that represents
        # our positive quadrant for this center. 

        found_node = node.children[value]

        if found_node is None:
            return node, value
        node = found_node

    return node, value




