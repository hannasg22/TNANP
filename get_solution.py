"""This file contains the part in which we simply try to get the result.

"""

import numpy as np
from scipy.optimize import root_scalar, root, least_squares
from scipy.integrate import solve_ivp

import find_eigenvalue as find
import equations as eq
import get_values as get

# Try to reach the E eigenvalue
# What method should we use? root? root_scalar?

x0 = [get.energy_guess()]
sol = least_squares(find.error_E, x0)
print(f"Solution: {sol}")
