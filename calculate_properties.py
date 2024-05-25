"""This file calculates de normalized wavefunctions so that we can get
the probability for ud, root-mean-square radius and quadrupole moment.

"""

import numpy as np
from scipy.optimize import root_scalar, root
from scipy.integrate import solve_ivp

import find_results as find
import equations as eq
import get_values as get
import get_graph as graph

def normalize():
    """This function will normalize our function to later get the proper
    results for the probabilities, quadrupole moment, etc.

    Output:
        Normalization constant
    """
    # Take values from data file
    A, B, C, D = get.ABCD()
    E = get.eigenvalue()
    
    # Solve system with proper variables
    wavefs = graph.plot_functions(E, A, B, C, D)

    # Get all values
    r_values_out = wavefs[4]
    r_values_in = wavefs[5]
    us_values_out = wavefs[0]
    us_values_in = wavefs[1]
    ud_values_out = wavefs[2]
    ud_values_in = wavefs[3]

    # Reverse order for arrays created inwards
    r_in_reverse = r_values_in[::-1]
    us_in_reverse = us_values_in[::-1]
    ud_in_reverse = ud_values_in[::-1]

    # Unify all the results FOR NORMALIZATION
    r_values = np.concatenate((r_values_out, r_in_reverse))
    us_values = np.concatenate((us_values_out, us_in_reverse))
    ud_values = np.concatenate((ud_values_out, ud_in_reverse))

    # Total wavefunction
    psi = us_values + ud_values

    # Normalize function
    norm = np.sqrt(np.trapz(psi**2, r_values))

    return norm

def ud_probability():
    """This function will calculate the probability of ud wavefunction.

    Output:
        ud probability
    """
    # Take values from data file
    A, B, C, D = get.ABCD()
    E = get.eigenvalue()

    # Solve system with proper E value
    wavefs = graph.plot_functions(E, A, B, C, D)
    
    # Get necessary values
    r_values_out = wavefs[4]
    r_values_in = wavefs[5]
    ud_values_out = wavefs[2]
    ud_values_in = wavefs[3]

    # Reverse order for arrays created inwards
    r_in_reverse = r_values_in[::-1]
    ud_in_reverse = ud_values_in[::-1]

    # Unify all the results
    r_values = np.concatenate((r_values_out, r_in_reverse))
    ud_values = np.concatenate((ud_values_out, ud_in_reverse))

    ud_normlzd = ud_values / normalize()

    P_ud = np.trapz(ud_normlzd**2, r_values)

    return P_ud

print(ud_probability())

