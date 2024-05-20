"""This file contains the part in which we simply try to get the result.

"""

import numpy as np
from scipy.optimize import root_scalar
from scipy.integrate import solve_ivp

import find_eigenvalue as find
import equations as eq
import get_values as get

# Get our real boundary conditions
bound_cond = get.boundary_conditions()

# Try to reach the E eigenvalue
sol = root_scalar(find.error_E, method='secant', x0=get.energy_guess())
E_final = sol.root

print(f"El valor de E que cumple las condiciones de contorno es: {E_final}")

# Solve with the obtained E
final = solve_ivp(lambda r, y: eq.radial_equations(r, y, E_guess),
                  get.range_of_radius(), get.initial_conditions(),
                  method='RK45', max_step=0.01)
