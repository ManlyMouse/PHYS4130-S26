'''
    Project name: Symplectic Integrations
    Subfolder: ODE Methods
    Author: Emma Krebs
    Final due date: 2/26/26
    File description: This file is to be used in the main.py. It includes the main three ODE's needed for 
                    comparison of the harmonic oscillator. This inlcudes a syplectic integration, RK45, 
                    and Odeint solvers.
'''


import numpy as np
from scipy.integrate import RK45, odeint
import matplotlib.pyplot as plt


def Harmonic_deriv(t, y, w, damp):
    
    """
    Hammonic deriviation function for the other ODEs to use. Incorporates variables x and p
    as free values and returns how they change at that point in time.

    Args:
        t (int/float): Time (not used in this definition but passed to use in future ODEs).
        y (tuple): Starting position. Starting momentum. What the system looks like.
        w (int/float): Angular frequency of harmonic oscillator.
        damp (int/float): Damping term on oscillator (if there is one)

    Returns:
        tuple: Functions for how dxdt and dpdt change in time.
    """
    x, p = y

    dxdt = p
    dpdt = -(w**2)*x - damp*p

    return [dxdt, dpdt]


def Symplectic_Euler(x_0, p_0, w, h, steps, damp):

    """
    Modification of the Euler method for solving Hamiltonains. Yields better results than Euler
    by similarily using time steps but essentially flipped the order of the velocity update
    and the position update, computing the new velocity of the particle before we compute it's new position.
    In this function we use a symplectic euler method such that we calculate the new momentum before 
    the new position.

    Args:
        x_0 (int/float): Initial x position.
        p_0 (int/float): Initial momentum position.
        w (int/float): Angular frequency for harmonic oscillator.
        steps (int): Number of iterations for function.
        damp (int/float): Damping term (if there is one).

    Returns:
        tuple: x_array and p_array of harmonic oscillator for a certain time/steps.
    """

    x = x_0
    p = p_0

    x_array = [x_0]
    p_array = [p_0]

    # Iterations, update momentum first then position
    for i in range(steps):

        p = p - h*((w**2)*x + damp*p)
        x = x + h*p

        x_array.append(x)
        p_array.append(p)
    
    return x_array, p_array


def RK45_solver(y_0, w, damp, tmin, tmax, time_total):

    """
    

    Args:
        

    Returns:
        tuple: 
    """

    t = np.linspace(tmin, tmax, time_total) # Time range

    # Object that is used to generate arrays
    solver = RK45(lambda t, y_0: Harmonic_deriv(t, y_0, w, damp), tmin, y_0, tmax, max_step=0.05)

    x_array = []
    p_array = []
    t_array = []

    # Repeat until solver stops running (when it hits the tmax after n steps)
    while solver.status == 'running':
        x_array.append(solver.y[0]) # Current value for x
        p_array.append(solver.y[1]) # Current value for p
        t_array.append(solver.t) # Current time
        solver.step()

    return x_array, p_array, t_array


def Odeint_solver(y_0, w, damp, tmin, tmax, time_total):

    """
    

    Args:
        

    Returns:
        tuple: 
    """

    t = np.linspace(tmin, tmax, time_total)
    N = odeint(Harmonic_deriv, y_0, t, args=(w, damp), tfirst=True)
    
    return t, N
