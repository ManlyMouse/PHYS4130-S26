'''
    Project name: Symplectic Integrations
    Subfolder: main.py
    Author: Emma Krebs
    Final due date: 2/26/26
    Project description: 
'''


import ODE_Methods
import matplotlib.pyplot as plt


def find_key(dict, value):
    """
    Grabs the key for a given value. This is used for labeling of graphs.

    Args: 
        dict (dictionary): Dictionary for the inputs to our solvers.
        value (array of int/floats): The key's value we are searching for.
    
    Returns:
        string: Returns either the key, or if there is no key, None. 
    
    """

    for key, val in dict.items():
        if val == value:
            return key
    return None

# ------------------ Symplectic Euler Solver ------------------

# Let us create a dictionary for our possible situations.
# The key is our angular frequency value and our dampening term. The other values of initial 
# conditions, step size, and number of steps will remain the same.
situations_symplectic = {
        'w = 0.5, damp = 0': [1, 1, 0.5, 0.05, 300, 0],
        'w = 1.0, damp = 0': [1, 1, 1, 0.05, 300, 0],
        'w = 1.5, damp = 0': [1, 1, 1.5, 0.05, 300, 0],
        'w = 1.0, damp = 0.25': [1, 1, 1, 0.05, 300, 0.25],
        'w = 1.0, damp = 0.5': [1, 1, 1, 0.05, 300, 0.5]
}

# Loop through the parameters in our dictionary and plot them
for value in situations_symplectic.values():
    x_array, p_array = ODE_Methods.Symplectic_Euler(*value)
    found_key = find_key(situations_symplectic, value)
    plt.plot(x_array, p_array, label=found_key)

# Graph information
plt.axis('equal')
plt.title('Simple Harmonic Oscillator Momentum vs Position (Symplectic Euler)')
plt.xlabel('X Values')
plt.ylabel('P Values')
plt.legend()
plt.grid()
plt.show()


# -------------------- RK45 Solver ----------------------------

situations_RK45 = {
    'w = 0.5, damp = 0': [(1, 1), 0.5, 0, 0, 15, 0.05],
    'w = 1.0, damp = 0': [(1, 1), 1, 0, 0, 15, 0.05],
    'w = 1.5, damp = 0': [(1, 1), 1.5, 0, 0, 15, 0.05],
    'w = 1.0, damp = 0.25': [(1, 1), 1, 0.25, 0, 15, 0.05],
    'w = 1.0, damp = 0.5': [(1, 1), 1, 0.5, 0, 15, 0.05]
}

for value in situations_RK45.values():
    x_array, p_array, t_array = ODE_Methods.RK45_solver(*value)
    found_key = find_key(situations_RK45, value)
    plt.plot(x_array, p_array, label=found_key)

# Graph information
plt.axis('equal')
plt.title('Simple Harmonic Oscillator Momentum vs Position (Symplectic Euler)')
plt.xlabel('X Values')
plt.ylabel('P Values')
plt.legend()
plt.grid()
plt.show()

# ODE_Methods.RK45_solver()

# ------------------- Odeint Solver ---------------------------

situations_Odeint = {
    'w = 0.5, damp = 0': [(1, 1), 0.5, 0, 0, 15, 300],
    'w = 1.0, damp = 0': [(1, 1), 1, 0, 0, 15, 300],
    'w = 1.5, damp = 0': [(1, 1), 1.5, 0, 0, 15, 300],
    'w = 1.0, damp = 0.25': [(1, 1), 1, 0.25, 0, 15, 300],
    'w = 1.0, damp = 0.5': [(1, 1), 1, 0.5, 0, 15, 300]

}

for value in situations_Odeint.values():
    t_array, N_array = ODE_Methods.Odeint_solver(*value)
    found_key = find_key(situations_Odeint, value)
    plt.plot(N_array[:,0], N_array[:,1], label=found_key)

# Graph information
plt.axis('equal')
plt.title('Simple Harmonic Oscillator Momentum vs Position (Symplectic Euler)')
plt.xlabel('X Values')
plt.ylabel('P Values')
plt.legend()
plt.grid()
plt.show()

# ----------------- Considering Error -------------------------


