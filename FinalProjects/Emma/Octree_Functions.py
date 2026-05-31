'''
    Title: Octree_Functions.py
    Description: Main file containing all of the functions for the octree part of the fluid dynamics/weather program. Focuses on subdividing
    and tracking the tree structure. Also updates the variables within the objects of the octree. 
'''


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

        # Calculate the neighbors after each rebuilding of leaf list. Includes six neighbors on each cell's face in 3D space.
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


def subdivide(node, max_depth):

    '''
        Takes a node and subdivides the grid into 8 more parts to create an octree. Quickens computing
        time by limiting the number of possible neighbors to calculate gradients for.

        Args:
            node (class): Object for center and grid of a region of our 3D space
            n (int): Cutoff value for a nodes depth depending on starting grid size.

        Returns:
            None: Updates the nodes directly. Doesn't return anything. 
    '''

    if node.leaf != True or node.depth >= max_depth:
        return

    node.leaf = False # It is no longer a leaf case. It has children now
    depth = node.depth + 1 # Update depth
    child_size = node.size / 2
    
    offsets = [-child_size/2, child_size/2] # Need to offset center for grid so it is in middle of box.

    child_index = 0
    for dx in offsets:
        for dy in offsets:
            for dz in offsets:
                center_x = node.center[0] + dx
                center_y = node.center[1] + dy
                center_z = node.center[2] + dz

                child = Node([center_x, center_y, center_z], child_size, depth)

                # The parents parameters will become the children's
                child.u = node.u
                child.v = node.v
                child.w = node.w
                child.omega = node.omega.copy() # Bc it is array
                child.T = node.T
                
                node.children[child_index] = child
                child_index += 1



def find_node(root, point):

    '''
        Given a point this finds out the leaf node it is in and returns that node.

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


def get_leaves(node):

    '''
        Given a node it will find all the connected leaves. If given the root, it finds all leaves in
        the entire system.

        Args:
            node (Object): Node object that you want to find the leaves of. 
        
        Returns:
            leaves (array): Array of leaf nodes.
    '''
    leaves = []

    if node.leaf == True:
        return [node]
    
    for child in node.children:
        if child != None:
            leaves.extend(get_leaves(child))

    return leaves



def get_neighbors(root, node):

    '''
        Finds neighbors for a given node's location.

        Args:
            root (Object): Root object of the space
            node (Object): Node you are trying to find neighbors for
        
        Returns:
            neighbors (Dict): Dictionary of neighbors depending on their axis and positive or negative direction.
           
    '''

    # Look for surrounding neighbors
    
    x, y, z = node.center

    # All the same distance, so use dx for dx, dy, dz
    dx = node.size * 0.51

    neighbors = {} # Dictionary of neighbors

    probes = {
    'xm': [x - dx, y, z],
    'xp': [x + dx, y, z],
    'ym': [x, y - dx, z],
    'yp': [x, y + dx, z],
    'zm': [x, y, z - dx],
    'zp': [x, y, z + dx]
    }

    for key, probe in probes.items():

        neighbor, _ = find_node(root, probe)

        if neighbor is not None:
            neighbors[key] = neighbor
        else:
            neighbors[key] = None

    return neighbors


def build_tree(node, max_depth):

    '''
        Initially builds a tree given the root node and the max depth. Focuses on 

        Args:
            node (Object): Root object of the space
            max_depth (Int): Maximum set depth for the tree
        
        Returns:
            None
    '''
          
    if node.depth >= max_depth:
        return
    
    subdivide(node, max_depth)
    
    for child in node.children:
        if child is not None:
            build_tree(child, max_depth)


def rebuild_neighbors(root):

    '''
        Rebuilds the neighbors for a given node, updating the object at the end. 

        Args:
            root (Object): Root node for the tree.

        Returns:
            leaves (Object array): All current leaves in the octree. 
    '''

    leaves = get_leaves(root)

    for leaf in leaves:
        leaf.neighbors = get_neighbors(root, leaf)

    return leaves
