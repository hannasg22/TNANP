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
import get_solutions as solut

def normalize():
    """This function will normalize our function to later get the proper
    results for the probabilities, quadrupole moment, etc.

    Output:
        Normalization constant
    """
    # Calculate proper E value
    E_get = root_scalar(find.error_E, args=(solut.get_ABCD()[0],
                                            solut.get_ABCD()[1],
                                            solut.get_ABCD()[2],
                                            solut.get_ABCD()[3]),
                        method='secant', x0=get.energy_guess(),
                        x1=get.energy_guess()+1.0)
    E_fin = E_get.root

    # Solve system with proper E value
    wavefs = graph.plot_functions(E_fin,
                                  solut.get_ABCD()[0],
                                  solut.get_ABCD()[1],
                                  solut.get_ABCD()[2],
                                  solut.get_ABCD()[3])
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
    # Calculate proper E value
    E_get = root_scalar(find.error_E, args=(solut.get_ABCD()[0],
                                            solut.get_ABCD()[1],
                                            solut.get_ABCD()[2],
                                            solut.get_ABCD()[3]),
                        method='secant', x0=get.energy_guess(),
                        x1=get.energy_guess()+1.0)
    E_fin = E_get.root

    # Solve system with proper E value
    wavefs = graph.plot_functions(E_fin,
                                  solut.get_ABCD()[0],
                                  solut.get_ABCD()[1],
                                  solut.get_ABCD()[2],
                                  solut.get_ABCD()[3])
    # Get all values
    r_values_out = wavefs[4]
    r_values_in = wavefs[5]
    ud_values_out = wavefs[2]
    ud_values_in = wavefs[3]

    # Reverse order for arrays created inwards
    r_in_reverse = r_values_in[::-1]
    ud_in_reverse = ud_values_in[::-1]

    # Unify all the results FOR NORMALIZATION
    r_values = np.concatenate((r_values_out, r_in_reverse))
    ud_values = np.concatenate((ud_values_out, ud_in_reverse))

    ud_normlzd = normalize() * ud_values

    P_ud = np.trapz(ud_normlzd**2, r_values)

    return P_ud

print(ud_probability())

