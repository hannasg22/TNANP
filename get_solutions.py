"""This file contains the part in which we simply try to get the results
for the energy and the A,B,C,D variables.

"""

import numpy as np
from scipy.optimize import root_scalar, root
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import seaborn as sns
import jsonlines

import find_results as find
import equations as eq
import get_values as get
import get_graph as graph

# Find solution for ABCD coefficients
def get_ABCD():
    initial_ABCD=[1., 1., 1., 1.]
    ABCD_values = root(find.error_ABCD, initial_ABCD)
    return ABCD_values.x

A_get, B_get, C_get, D_get = get_ABCD()

E_final = root_scalar(find.error_E, args=(A_get, B_get, C_get, D_get),
                      method='secant', x0=get.energy_guess(),
                      x1=get.energy_guess()+1.0)

E_use = E_final.root
print(E_use)

# Save values in JSONLines file
with jsonlines.open('values_ABCDE.jsonl', mode='a') as file:
    file.write({"A": A_get, "B": B_get, "C": C_get, "D": D_get,
                "E": E_use})

print("Values A, B, C, D y E_use saved in values_ABCDE.jsonl")

"""
wf_final = graph.plot_functions(E_use, get_ABCD()[0], get_ABCD()[1],
                                get_ABCD()[2], get_ABCD()[3])


# Get the values for r, us and ud
r_values_out = wf_final[4]
r_values_in = wf_final[5]
us_values_out = wf_final[0]
us_values_in = wf_final[1]
ud_values_out = wf_final[2]
ud_values_in = wf_final[3]

# Reverse order for arrays created inwards
r_in_reverse = r_values_in[::-1]
us_in_reverse = us_values_in[::-1]
ud_in_reverse = ud_values_in[::-1]

# Unify all the results FOR THE IMAGE
r_values = np.concatenate((r_values_out, r_in_reverse[50:]))
us_values = np.concatenate((us_values_out, us_in_reverse[50:]))
ud_values = np.concatenate((ud_values_out, ud_in_reverse[50:]))

# Graphic settings
sns.set(style='darkgrid')

plt.figure(figsize=(10, 6))

plt.style.use('dark_background')

plt.plot(r_values, us_values, label='$u_s(r)$', color='pink')
plt.plot(r_values, ud_values, label='$u_d(r)$', color='magenta')

plt.xlabel('r', color='white')
plt.title('Eigenfunctions $u_s(r)$ and $u_d(r)$ vs. $r (fm)$', color='black')
plt.legend()
plt.grid(True, color='gray')

plt.gca().spines['bottom'].set_color('black')
plt.gca().spines['left'].set_color('black')
plt.gca().tick_params(axis='x', colors='black')
plt.gca().tick_params(axis='y', colors='black')

plt.show()
"""
