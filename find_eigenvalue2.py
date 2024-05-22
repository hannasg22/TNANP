"""We define the root finding process to achieve the proper eigenvalue.

We take 'radial_equations' function from equations.py, which contains
the system we must solve. We then solve it inside the 'error_E' function
through an integration method for the inserted energy value.

So, to carry out the integration we make use of the next SciPy function:
    - integrate.solve_ivp --> solves the system with the inserted E
"""

import numpy as np
from scipy.integrate import solve_ivp

import potentials as pot
import equations as eq
import get_values as get


def error_E(E_guess):
    """This function analyses if the results obtained with E_guess
    match the desired boundary conditions.

    We solve the system of equations both forwards and backwards with
    E_guess and compare the results in the midpoint called "cut".

    Inputs:
        E_guess: value of energy for which we solve the equations
    Output:
        error: difference between the results with E_guess in cut point
    """
    E_insert = E_guess
    print(f"E values: {E_insert}")
    
    # Define the midpoint
    cut = get.range_of_radius()[1] * 0.36

    # Get the conditions from the data file
    ini_cond = get.initial_conditions()
    fin_cond = get.boundary_conditions()
    
    # Ranges for the forward and backward integration
    r_range1 = [get.range_of_radius()[0], cut]
    r_range2 = [get.range_of_radius()[1], cut]
    print(f"r_range1: {r_range1}")
    print(f"r_range2: {r_range2}")

    # Solve system for E_guess forwards
    sol1 = solve_ivp(lambda r, y: eq.radial_equations(r, y, E_insert),
                     r_range1, ini_cond, method='RK45', max_step=0.01)
    # Solve system for E_guess backwards
    sol2 = solve_ivp(lambda r, y: eq.radial_equations(r, y, E_insert),
                     r_range2, fin_cond, method='RK45', max_step=0.01)

    # Result in midpoint "cut" for us, vs, ud, vd
    error_us = sol1.y[0][-1] - sol2.y[0][-1]
    error_vs = sol1.y[1][-1] - sol2.y[1][-1]
    error_ud = sol1.y[2][-1] - sol2.y[2][-1]
    error_vd = sol1.y[3][-1] - sol2.y[3][-1]

    error = [error_us, error_vs, error_ud, error_vd]
    print(f"error: {error}")
    
    return error
