# DEUTERON

## Goal of the code

Bfriefly explained, this code is provided to solve specifically the deuteron equations and get its eigenfunctions and eigenvalues.

In order to find the results, an specific model for the potentials is implemented. But another option could be applied, making use of the user's preferred election.

## Theory

With the aim of better understanding what it is done in this code, let us introduce the main theoretical concept.

### Main idea

The deuteron is the **only bound state of two nucleons** and its bound is weak, therefore it only exists in the ground state. It is formed by one proton and one neutron and the nuclear force between them has the next properties (the most important ones for the goal of this project): attractive (to form the bound state), short range (of order of $\sim 1fm$ ) and non-central (so it has a tensor component). 

All these assumptions have been made through the obtained experimental data. Furthermore, the potential describing the interaction between both particles has been contructed more precisely to fit the actual results. It can be widely analysed and it will show many different components. We instead will focus on the **two main quantities**:
- Central potential $V_C$
- Tensorial potential $V_T$

These can also be described by different models. One option, the one we will use, is defining both components through a **square well potential**:

$$ V(r < r_0)=-V_0, \hspace{0.5cm} V(r \geq r_0)=0.
$$

where $V_0$ and $r_0$ are defined again from experimental data. This will be the exact form of the central potential component $V_C$.

On the other hand, the tensor interaction has the form:

$$ (\vec{\tau_1}\cdot \vec{\tau_2})V_T(r)S_{12}
$$

where the first dot product relates the isospin components of the system, $S_{12}$ is the tensor operator and $V_T(r)$ is the model potential used for this tensor interaction (in our case, a square well potential). The exact form of $S_{12}$ is:

$$ S_{12}=2[3\frac{(\vec{S} \cdot \vec{r} )}{r^2}-\vec{S}^2]
$$

Now, let us derive the form of the Hamiltonian using deuteron's properties. The deuteron has total isospin $T=0$ and spin parity $J^{\pi}=1^+$. Spin could in principle be $S=1,0$. Parity conservation imposes some rules for orbital angular momentum quantum number $L$ (together with $J-1 < L < J+1$): since parity follows rule $\pi=(-1)^l=+1$, we will only have $L=0$ (S-wave) and $L=2$ (D-wave). This means that the ground state of deuteron is a mixture of the wavefunctions of those two waves (which are connected through the tensor interaction). At this point, due to the asymmetry of the whole wavefunction in a system of two fermions, we have $S=1$ for the total spin.

These results lead us from the total Hamiltonian

$$ H=-\frac{\hbar^2}{M}\frac{1}{r}\frac{d^2}{dr^2}r+\frac{\hbar^2}{M}\frac{L^2}{r^2}+V_C(r)+V_T(r)S_{12}
$$

into two radial equations describing the system, which after inserting the properties and quantum numbers of the deuteron have the next form:

$$ [\frac{\hbar^2}{M}\frac{d^2}{dr^2}+E-V_C(r)]u_s=\sqrt{8}V_T(r)u_d
$$

$$ [\frac{\hbar^2}{M}(\frac{d^2}{dr^2}-\frac{6}{r^2})+E+2V_T(r)-V_C(r)]u_d=\sqrt{8}V_T(r)u_s
$$

These are exactly the equations that our code will solve! So, we will **get the two wavefunctions u<sub>S</sub> and u<sub>D</sub> and the binding energy** (by experimental data we know it is: $E_B=2.225 MeV$).

### Further details
