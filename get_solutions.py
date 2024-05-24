"""This file contains the part in which we simply try to get the result
for the energy.

"""

import numpy as np
from scipy.optimize import root_scalar, root, least_squares, fsolve
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

import find_results as find
import equations as eq
import get_values as get

# Find solution for ABCD coefficients
def get_ABCD():
    initial_ABCD=[1., 1., 1., 1.]
    ABCD_values = root(find.error_ABCD, initial_ABCD)
    return ABCD_values.x

A_fin = get_ABCD()[0]
B_fin = get_ABCD()[1]
C_fin = get_ABCD()[2]
D_fin = get_ABCD()[3]

E_final = root_scalar(find.error_E, args=(A_fin, B_fin, C_fin, D_fin),
                      method='secant', x0=get.energy_guess(),
                      x1=get.energy_guess()+1.0)

E_use = E_final.root
print(E_use)
