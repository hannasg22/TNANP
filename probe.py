import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import least_squares
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
    E = E_guess[0]
    print(f"Running error_E with E_guess: {E}")

    # Define the midpoint
    cut = get.range_of_radius()[1] * 0.9
    print(f"cut: {cut}")

    # Get the conditions from the data file
    ini_cond = get.initial_conditions()
    fin_cond = get.boundary_conditions()
    print(f"Initial conditions: {ini_cond}")
    print(f"Boundary conditions: {fin_cond}")

    # Ranges for the forward and backward integration
    r_range1 = [get.range_of_radius()[0], cut]
    r_range2 = [get.range_of_radius()[1], cut]
    print(f"r_range1: {r_range1}")
    print(f"r_range2: {r_range2}")

    # Solve system for E_guess forwards
    sol1 = solve_ivp(lambda r, y: eq.radial_equations(r, y, E),
                     r_range1, ini_cond, method='RK45', max_step=0.01)
    # Solve system for E_guess backwards
    sol2 = solve_ivp(lambda r, y: eq.radial_equations(r, y, E),
                     r_range2, fin_cond, method='RK45', max_step=0.01)
    
    # Print solutions to check shapes and values
    print(f"sol1.t: {sol1.t}")
    print(f"sol1.y: {sol1.y}")
    print(f"sol2.t: {sol2.t}")
    print(f"sol2.y: {sol2.y}")

    # Result in midpoint "cut" for us, vs, ud, vd
    error_us = sol1.y[0][-1] - sol2.y[0][-1]
    error_vs = sol1.y[1][-1] - sol2.y[1][-1]
    error_ud = sol1.y[2][-1] - sol2.y[2][-1]
    error_vd = sol1.y[3][-1] - sol2.y[3][-1]

    error = [error_us, error_vs, error_ud, error_vd]
    print(f"error: {error}")
    
    return error

# Supongamos que get.energy_guess() devuelve una lista de valores iniciales para la energía
def get_energy_guess():
    return [1.0]  # least_squares esperará una lista de valores iniciales

# Ejemplo de cómo se utilizaría en least_squares
x0 = get_energy_guess()
sol = least_squares(error_E, x0)
print(f"Solution: {sol}")