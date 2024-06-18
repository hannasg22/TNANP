"""This module contains the potentials used to solve the equations.

Their form is chosen through phenomenology to fit experimental results.
"""

import math

import get_values as get


# Potentials from gezerlis (used in the code)
def V_C(r):
    """This function contains the potential defined in the gezerlis
    8.57 exercise in order to represent the central potential of the
    deuteron system.
    
    Input:
        r : distance between proton and neutron
    Output:
        Value of the potential for r
    """
    
    return -47.0 * math.exp(-r/1.18) * 1.18 / r

def V_T(r):
    """This function contains the potential defined in the gezerlis
    8.57 exercise in order to represent the tensorial potential of the
    deuteron system.
    
    Input:
        r : distance between proton and neutron
    Output:
        Value of the potential for r
    """
    
    return -24.0 * math.exp(-r/1.7) * 1.7 / r
