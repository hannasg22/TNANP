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
    """This function analyses if the result obtained with E_guess
    matches the desired boundary conditions.

    We solve the system of equations both inwards and outwards with
    E_guess and compare the results in the midpoint called "cut".

    Inputs:
        E_guess: value of energy for which we solve the equations
    Output:
        error: difference between the results with E_guess in cut point
    """

    cut = get.range_of_radius()[1] * 0.9
    # Get the conditions from the data file
    ini_cond = get.initial_conditions()
    fin_cond = get.boundary_conditions()
    r_range1 = [get.range_of_radius()[0], cut]
    r_range2 = [get.range_of_radius()[1], cut]
    
    # Solve system for E_guess ourtwards
    sol1 = solve_ivp(lambda r, y: eq.radial_equations(r, y, E_guess),
                     r_range1, ini_cond, method='RK45', max_step=0.01)
    # Solve system for E_guess inwards
    sol2 = solve_ivp(lambda r, y: eq.radial_equations(r, y, E_guess),
                     r_range2, fin_cond, method='RK45', max_step=0.01)
     
    # Result in midpoint "cut"
    error_us = sol1.y[0][-1] - sol2.y[0][-1]
    error_vs = sol1.y[1][-1] - sol2.y[1][-1]
    error_ud = sol1.y[2][-1] - sol2.y[2][-1]
    error_vd = sol1.y[3][-1] - sol2.y[3][-1]
    
    return [error_us, error_vs, error_ud, error_vd]
