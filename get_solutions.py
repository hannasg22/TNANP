"""This file contains the part in which we simply try to get the result
for the energy.

"""

import numpy as np
from scipy.optimize import root_scalar, root, least_squares, fsolve
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import seaborn as sns

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

# Graph with seaborn
sns.set(style='darkgrid')

plt.figure(figsize=(10, 6))

plt.style.use('dark_background')

plt.plot(r_values_out, us_values_out, label='$u_s(r)$', color='pink')
plt.plot(r_values_in, us_values_in, color='pink')
plt.plot(r_values_out, ud_values_out, label='$u_d(r)$', color='magenta')
plt.plot(r_values_in, ud_values_in, color='magenta')

plt.xlabel('r', color='white')
plt.ylabel('V(r)', color='white')
plt.title('Eigenfunctions $u_s(r)$ and $u_d(r)$ vs. $r (fm)$', color='black')
plt.legend()
plt.grid(True, color='gray')

plt.gca().spines['bottom'].set_color('black')
plt.gca().spines['left'].set_color('black')
plt.gca().tick_params(axis='x', colors='black')
plt.gca().tick_params(axis='y', colors='black')

plt.show()
