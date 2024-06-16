"""This file plots the eigenfunctions calculated with the proper energy
value and ABCD variables. We extract the results through get_values.py
by taking the results saved in values_ABCDE.jsonl data file.
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import get_values as get
import get_graph as graph

wf_final = graph.plot_functions(get.eigenvalue(), get.ABCD()[0],
                                get.ABCD()[1], get.ABCD()[2],
                                get.ABCD()[3])

# Get the values for r, us and ud
us_values_out = wf_final[0]
us_values_in = wf_final[1]
ud_values_out = wf_final[2]
ud_values_in = wf_final[3]
r_values_out = wf_final[4]
r_values_in = wf_final[5]

# Reverse order for arrays created inwards
r_in_reverse = r_values_in[::-1]
us_in_reverse = us_values_in[::-1]
ud_in_reverse = ud_values_in[::-1]

# Unify all the results to generate the image
r_values = np.concatenate((r_values_out, r_in_reverse[50:]))
us_values = np.concatenate((us_values_out, us_in_reverse[50:]))
ud_values = np.concatenate((ud_values_out, ud_in_reverse[50:]))

# Graphic settings
sns.set(style='darkgrid')

plt.figure(figsize=(10, 6))


plt.plot(r_values, us_values, label='$u_s(r)$', color='hotpink')
plt.plot(r_values, ud_values, label='$u_d(r)$', color='mediumvioletred')

plt.xlabel('r (fm)', color='black')
plt.title('Eigenfunctions $u_s(r)$ and $u_d(r)$ vs. $r (fm)$', color='black')
plt.legend()
plt.grid(True, color='gray')

plt.gca().spines['bottom'].set_color('black')
plt.gca().spines['left'].set_color('black')
plt.gca().tick_params(axis='x', colors='black')
plt.gca().tick_params(axis='y', colors='black')

plt.show()
