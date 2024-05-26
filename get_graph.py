"""In this file we have the function to plot easily the final results of
the eigenfunctions with the obtained proper energy eigenvalue and A, B,
C and D variables.
"""

from scipy.integrate import solve_ivp
import numpy as np

import get_values as get
import equations as eq


def plot_functions(energy, a, b, c, d):
    """This function solves the equations with the proper values of E
    and the other coefficients.

    Outputs:
        The values of the eigenfunctions outwards and inwards, as well
        as the radius values.
    """

    # Define the midpoint
    cut = get.range_of_radius()[1] * 0.36

    # Get initial conditions from the data file
    ini_cond_A = get.initial_conditions_A()
    ini_cond_B = get.initial_conditions_B()

    # Get boundary conditions from data file
    fin_cond_C = get.boundary_conditions_C()
    fin_cond_D = get.boundary_conditions_D()
    
    # Ranges for the forward and backward integration
    r_range1 = [get.range_of_radius()[0], cut]
    r_range2 = [get.range_of_radius()[1], cut]

    # Solve system for E_guess forwards
    solA = solve_ivp(lambda r, y: eq.radial_equations(r, y, energy),
                     r_range1, ini_cond_A, method='RK45', max_step=0.01)
    solB = solve_ivp(lambda r, y: eq.radial_equations(r, y, energy),
                     r_range1, ini_cond_B, method='RK45', max_step=0.01)

    # Solve system for E_guess backwards
    solC = solve_ivp(lambda r, y: eq.radial_equations(r, y, energy),
                     r_range2, fin_cond_C, method='RK45', max_step=0.01)    
    solD = solve_ivp(lambda r, y: eq.radial_equations(r, y, energy),
                     r_range2, fin_cond_D, method='RK45', max_step=0.01)

    r_out = solA.t
    r_in = solC.t
    # Combinations of the solutions
    us_out = a * solA.y[0] + b * solB.y[0]
    us_in = c * solC.y[0] + d * solD.y[0]
    ud_out = a * solA.y[2] + b * solB.y[2]
    ud_in = c * solC.y[2] + d * solD.y[2]

    return [us_out, us_in, ud_out, ud_in, r_out, r_in]
