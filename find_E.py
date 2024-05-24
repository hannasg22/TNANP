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

def error_E(E_guess, A, B, C, D):
    """This function analyses if the results obtained with E_guess
    match the desired boundary conditions.

    We solve the system of equations both forwards and backwards with
    E_guess and compare the results in the midpoint called "cut".

    Inputs:
        E_guess: value of energy for which we solve the equations
    Output:
        error: difference between the results with E_guess in cut point
    """
    print(f"E values: {E_guess}")
    
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
    print(f"r_range1: {r_range1}")
    print(f"r_range2: {r_range2}")

    # Solve system for E_guess forwards
    solA = solve_ivp(lambda r, y: eq.radial_equations(r, y, E_guess),
                     r_range1, ini_cond_A, method='RK45', max_step=0.01)
    solB = solve_ivp(lambda r, y: eq.radial_equations(r, y, E_guess),
                     r_range1, ini_cond_B, method='RK45', max_step=0.01)

    # Solve system for E_guess backwards
    solC = solve_ivp(lambda r, y: eq.radial_equations(r, y, E_guess),
                     r_range2, fin_cond_C, method='RK45', max_step=0.01)    
    solD = solve_ivp(lambda r, y: eq.radial_equations(r, y, E_guess),
                     r_range2, fin_cond_D, method='RK45', max_step=0.01)

    # Cominations of the solutions
    sol_out = A * solA.y + B * solB.y
    sol_in = C * solC.y + D * solD.y
    
    # Impose conditions of continuituy
    error_us1 = sol_out[0] - 3.0
    error_us2 = sol_in[0] - 3.0
    error_ud = sol_out[2] - sol_in[2]
    error_vd = sol_out[3] - sol_in[3]

    # Return array to make operation in secant function possible
    error = np.array([error_us1, error_us1, error_ud, error_vd])
    print(f"error: {error}")
    
    return error
