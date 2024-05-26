"""This file contains the part in which we simply try to get the results
for the energy and the A,B,C,D variables.
"""

import numpy as np
from scipy.optimize import root_scalar, root
import jsonlines

import find_results as find
import get_values as get
import get_graph as graph


# Find solution for ABCD coefficients
def get_ABCD():
    """This function takes initial guesses for A, B, C and D and solves
    the system through a root finding method to reach variables which
    obey the continuity conditions we require.

    Output:
        Proper result for A, B, C and D
    """
    
    initial_ABCD=[1., 1., 1., 1.]
    ABCD_values = root(find.error_ABCD, initial_ABCD)
    return ABCD_values.x

A_get, B_get, C_get, D_get = get_ABCD()

# Calculate E value with the last continuity condition
E_final = root_scalar(find.error_E, args=(A_get, B_get, C_get, D_get),
                      method='secant', x0=get.energy_guess(),
                      x1=get.energy_guess()+1.0)

# Check that the energy is the expected one
E_use = E_final.root
print(E_use)

# Save values in JSONLines file
with jsonlines.open('values_ABCDE.jsonl', mode='w') as file:
    file.write({"A": A_get, "B": B_get, "C": C_get, "D": D_get,
                "E": E_use})

print("Values A, B, C, D and E saved in values_ABCDE.jsonl")
