"""This file contains the part in which we simply try to get the result.

"""

import numpy as np
from scipy.optimize import root_scalar, root, least_squares, fsolve
from scipy.integrate import solve_ivp

import find_ABCD as find
import equations as eq
import get_values as get

# Find solution for ABCD coefficients
def get_ABCD():
    initial_ABCD=[1., 1., 1., 1.]
    ABCD_values = fsolve(find.error_ABCD, initial_ABCD)
    return ABCD_values

print(get_ABCD())



# Try to reach the E eigenvalue
# What method should we use? root? root_scalar?
"""
sol = least_squares(find.error_E, x0)
print(f"Solution: {sol}")
"""
