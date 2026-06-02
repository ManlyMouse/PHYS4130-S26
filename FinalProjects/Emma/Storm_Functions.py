'''
    Title: Storm_Functions.py
    Description: Main file containing all of the functions for the physics and weather part of the program. 
    Focuses on solving the navier stokes equation and updating the variables with diffusion, advect, and more.
'''

import random 
import numpy as np


def diffuse(leaves, alpha=0.1):

    
    new_T = {}
    
    for node in leaves:
        neighbor_temps = []

        # Use the cached neighbors instead of looping through all leaves
        for key in ['xm', 'xp', 'ym', 'yp', 'zm', 'zp']:
            nb = node.neighbors.get(key)
            if nb:
                neighbor_temps.append(nb.T)
        
        if neighbor_temps:
            avg = sum(neighbor_temps) / len(neighbor_temps)
            new_T[id(node)] = node.T + alpha * (avg - node.T)
        else:
            new_T[id(node)] = node.T

    for node in leaves:
        node.T = new_T[id(node)]


def diffuse_conservative(leaves, alpha=0.02):
    delta_heat = {id(node): 0.0 for node in leaves}

    for node in leaves:
        V_node = node.size**3

        for key in ['xm', 'xp', 'ym', 'yp', 'ym', 'yp', 'zm', 'zp']:
            nb = node.neighbors.get(key)
            if nb is None:
                continue

            V_nb = nb.size**3

            dT = nb.T - node.T

            # heat exchanged between cells
            heat_flux = alpha * dT * min(V_node, V_nb)

            delta_heat[id(node)] += heat_flux
            delta_heat[id(nb)] -= heat_flux

    for node in leaves:
        V_node = node.size**3
        node.T += delta_heat[id(node)] / V_node
        