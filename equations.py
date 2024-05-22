"""This module contains the code with the system of the deuteron
equations.

Important information about units of measurements:
    Units used:
        - Distances: fm
        - Mass: MeV / c**2
        - Energy: MeV
    We will define the Planck constant with the next dimensions:
        h_bar * c = 197.327 MeV * fm
"""

import numpy as np
import potentials as pot


def radial_equations(r, y, E):
    """This function defines from our 2 2nd order ODEs  a system of 4
    1st order ODEs, generated to solve the problem.

    We have two eigenfunctions 'us' and 'ud' representing the l=0 s-wave
    and l=2 d-wave. These are the functions we want to reach.

    We define:
        dus: 1st derivative of us (defined as vs)
        dvs: 2nd derivative of us (1st derivative of vs)
        We do similarly for ud, defining dud and dvd

    Inputs:
        r: distance between both nucleoons
        E: energy value
        y: vector with the variables [us, vs, ud, vd]
    """
    # Definition of parameters
    h_bar = 197.327 # Reduced Planck constant
    M = 938.918 # Reduced mass of deuteron
    
    us, vs, ud, vd = y
    # The 1st derivatives of us and ud
    dus = vs
    dud = vd
    # The 2nd derivatives of eigenfunctions us and ud
    dvs = (M / (h_bar**2)) * (ud * np.sqrt(8) * pot.V_T(r)
                              + us * (pot.V_C(r) - E))
    dvd = (M / (h_bar**2)) * (us * np.sqrt(8) * pot.V_T(r)
                              + ud * ((6.0 * h_bar**2) / (M * r**2) - E
                                      - 2.0 * pot.V_T(r) + pot.V_C(r)))
    return [dus, dvs, dud, dvd]
