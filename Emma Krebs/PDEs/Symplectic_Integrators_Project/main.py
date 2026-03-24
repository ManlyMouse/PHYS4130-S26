'''
    Project name: Symplectic Integrations
    Subfolder: main.py
    Author: Emma Krebs
    Final due date: 2/26/26
    Project description: 
'''


import ODE_Methods
import matplotlib.pyplot as plt

# ------------------ Symplectic Euler Solver ------------------

# Let us create a dictionary for out possible situations
situations = {
        'w = 0.5': [1, 1, 0.5, 0.05, 300, 0]
}


for value in situations.values():
    print(*value)
    x_array, p_array = ODE_Methods.Symplectic_Euler(*value)

# -------------------- Rk45 Solver ----------------------------

ODE_Methods.RK45_solver()

# ------------------- Odeint Solver ---------------------------

ODE_Methods.Odeint_solver()