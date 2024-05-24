"""This file contains the part in which we simply try to get the result.

"""

import numpy as np
from scipy.optimize import root_scalar, root, least_squares, solvef
from scipy.integrate import solve_ivp

import find_E as find
import equations as eq
import get_values as get
import secant as sec


initial_ABCD=[1., 1., 1., 1.]
ABCD_values = solvef(find.error_E, initial_ABCD)
print(ABCD_values)

# Try to reach the E eigenvalue
# What method should we use? root? root_scalar?
"""
sol = least_squares(find.error_E, x0)
print(f"Solution: {sol}")
"""
