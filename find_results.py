"""We define the root finding process to achieve the proper A, B, C and
D coefficients which will lead us later to the proper E value.

We take 'radial_equations' function from equations.py, which contains
the system we must solve. We then solve it inside the 'error_ABCD'
function through an integration method for the inserted coefficients.

So, to carry out the integration we make use of the next SciPy function:
    - integrate.solve_ivp --> solves the system with the inserted E
"""

import numpy as np
from scipy.integrate import solve_ivp

import equations as eq
import get_values as get

def error_ABCD(coeffs):
    """This function find the values of A, B, C and D that for the first
    E guess value will obey 3 boundary conditions.

    We solve the system of equations both forwards and backwards with
    E_guess and compare the results in the midpoint called "cut".

    Inputs:
        coeffs: list with [A, B, C, D] coefficients
    Output:
        error: difference between the results with A, B, C and D in
               'cut' point
    """
    A, B, C, D = coeffs
    E_guess = get.energy_guess()

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
    solA = solve_ivp(lambda r, y: eq.radial_equations(r, y, E_guess),
                     r_range1, ini_cond_A, method='RK45', max_step=0.01)
    solB = solve_ivp(lambda r, y: eq.radial_equations(r, y, E_guess),
                     r_range1, ini_cond_B, method='RK45', max_step=0.01)

    # Solve system for E_guess backwards
    solC = solve_ivp(lambda r, y: eq.radial_equations(r, y, E_guess),
                     r_range2, fin_cond_C, method='RK45', max_step=0.01)    
    solD = solve_ivp(lambda r, y: eq.radial_equations(r, y, E_guess),
                     r_range2, fin_cond_D, method='RK45', max_step=0.01)

    # Combinations of the solutions
    sol_out = A * solA.y + B * solB.y
    sol_in = C * solC.y + D * solD.y
    
    # Impose conditions of continuituy
    error_us1 = sol_out[0][-1] - 3.0
    error_us2 = sol_in[0][-1] - 3.0
    error_ud = sol_out[2][-1] - sol_in[2][-1]
    error_vd = sol_out[3][-1] - sol_in[3][-1]

    # Return list to make operation in fsolve function possible
    error = [error_us1, error_us2, error_ud, error_vd]
    print(f"error: {error}")
    
    return error

def error_E(E_guess, A, B, C, D):
    """This function will finally find the energy eigenvalue after
    finding A, B, C and D coefficients. The proper E value will be found
    by imposing the last continuity condition left.

    Inputs:
        E_guess: first guess for the eigenvalue
        ABCD: proper coefficients for which we must solve the last
              condition
    Output:
        Error function for the las continuity condition we must find
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
    solA = solve_ivp(lambda r, y: eq.radial_equations(r, y, E_guess),
                     r_range1, ini_cond_A, method='RK45', max_step=0.01)
    solB = solve_ivp(lambda r, y: eq.radial_equations(r, y, E_guess),
                     r_range1, ini_cond_B, method='RK45', max_step=0.01)

    # Solve system for E_guess backwards
    solC = solve_ivp(lambda r, y: eq.radial_equations(r, y, E_guess),
                     r_range2, fin_cond_C, method='RK45', max_step=0.01)    
    solD = solve_ivp(lambda r, y: eq.radial_equations(r, y, E_guess),
                     r_range2, fin_cond_D, method='RK45', max_step=0.01)

    # Combinations of the solutions
    sol_out = A * solA.y + B * solB.y
    sol_in = C * solC.y + D * solD.y

    error_vs = sol_out[1][-1] - sol_in[1][-1]

    return error_vs
