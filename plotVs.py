"""This file will just plot the potentials from gezerlis file.

"""
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import get_values as get
import potentials as pot

# Define range of the radius
r_values = np.linspace(get.range_of_radius()[0],
                       get.range_of_radius()[1],
                       1000
                       )

# Give values to the potentials
V_C_values = [pot.V_C(r) for r in r_values]
V_T_values = [pot.V_T(r) for r in r_values]

# PLOT
sns.set(style='darkgrid')

plt.figure(figsize=(10, 6))

plt.style.use('dark_background')

plt.plot(r_values, V_C_values, label='$V_C(r)$', color='pink')
plt.plot(r_values, V_T_values, label='$V_T(r)$', color='magenta')

plt.xlabel('r', color='white')
plt.ylabel('V(r)', color='white')
plt.title('Potentials $V_C(r)$ and $V_T(r) (MeV)$ vs. $r (fm)$', color='black')
plt.legend()
plt.grid(True, color='gray')

plt.gca().spines['bottom'].set_color('black')
plt.gca().spines['left'].set_color('black')
plt.gca().tick_params(axis='x', colors='black')
plt.gca().tick_params(axis='y', colors='black')

plt.show()
