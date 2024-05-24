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
import get_graph as graph

# Find solution for ABCD coefficients
def get_ABCD():
    initial_ABCD=[1., 1., 1., 1.]
    ABCD_values = root(find.error_ABCD, initial_ABCD)
    return ABCD_values.x

A_fin = get_ABCD()[0]
B_fin = get_ABCD()[1]
C_fin = get_ABCD()[2]
D_fin = get_ABCD()[3]

print(get_ABCD())

E_final = root_scalar(find.error_E, args=(A_fin, B_fin, C_fin, D_fin),
                      method='secant', x0=get.energy_guess(),
                      x1=get.energy_guess()+1.0)

E_use = E_final.root
print(E_use)

wf_final = graph.plot_functions(E_use, A_fin, B_fin, C_fin, D_fin)

r_values_out = wf_final[4]
r_values_in = wf_final[5]
us_values_out = wf_final[0]
us_values_in = wf_final[1]
ud_values_out = wf_final[2]
ud_values_in = wf_final[3]

# Graph of functions
plt.figure()
plt.plot(r_values_out, us_values_out, label='us(r)')
plt.plot(r_values_out, ud_values_out, label='ud(r)')
plt.plot(r_values_in, us_values_in, label='us(r)')
plt.plot(r_values_in, ud_values_in, label='ud(r)')
plt.axhline(y=E_use, color='r', linestyle='--',
            label='Binding energy E (MeV)')
plt.xlabel('r (fm)')
plt.ylabel('u(r)')
plt.title('Eigenfunctions vs. ditance r')
plt.legend()
plt.grid(True)
plt.show()
