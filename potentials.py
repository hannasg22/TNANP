"""This module contains the potentials used to solve our equations.

Parameters needed in the potentials modelled through squarewells:
    r0: r value for the range of the square well potential (units: fm)
    V0 : depth of the potential (units: MeV)
These have been chosen due to experimental data.
"""
import math

import get_values as get


# Potentials from gezerlis (the ones used in the code)
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

# Potentials modelled with squarewells
def V_c_squarewell(r):
    """This function calculates the value of the central part of the
    potential.         

    Input:
        r : distance between proton and neutron
    Output:
        Value of the central potential for a certain r
    """

    # Inserting values for central potential
    V0_c = get.central_V()[0]
    r0_c = get.central_V()[1]
    if r <= r0_c:
        return -V0_c
    else:
        return 0.0

def V_t_squarewell(r):
    """This function calculates the value of the tensorial part of the
    potential for distinct values of r.

    Input:
        r : distance between proton and neutron
    Output:
        Value of the tensor potential for a certain r
    """

    # Inserting values for tensor potential
    V0_t = get.tensorial_V()[0]
    r0_t = get.tensorial_V()[1]
    if r <= r0_t:
        return -V0_t
    else:
        return 0.0
