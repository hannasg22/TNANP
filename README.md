# DEUTERON

## Goal of the code

Briefly explained, this code is provided to solve specifically the deuteron equations and get its eigenfunctions and eigenvalues.

In order to find the results, a particular model for the potentials is implemented. However, another option could be applied, making use of the user's preferred election.

## Theory

With the aim of better understanding what it is done in this code, let us introduce the main theoretical concepts.

### Main idea

The deuteron is the **only bound state of two nucleons** and its bound is weak, therefore it only exists in the ground state. It is formed by one proton and one neutron and the nuclear force between them has the next main properties: 
- Attractive: forms a bound state
- Short range: of order of $\sim 1fm$
- Non-central: it has a tensor component connecting different states
- Hard core: there is a range in which the potential is completely repulsive, so that the nucleons do not collapse
- Conserves parity 

All these assumptions have been made through the obtained experimental data. Furthermore, the potential describing the interaction between both particles has been contructed more precisely to fit the actual results. It can be widely analysed and it will show many different components. We instead will focus on the **two main quantities**:
- Central potential $V_C$
- Tensorial potential $V_T$

Both can also be described by diverse models. One option (the one we will use) is to define them through Yukawa potential wells:

$$ V=V_C(r)+V_T(r)\hat{S}=-47\frac{exp(r/1.18)}{r/1.18}-24\frac{exp(r/1.7)}{r/1.7}\hat{S}
$$

where $\hat{S}=\hat{S}_{12}$ is the tensor operator. The strength of the potentials is defined in MeV and the distance r in fm. This specific choice has been made to fit the model exposed in the [Gezerlis book](https://numphyspy.org) _Numerical Methods in Physics with Python_.

Now, let us derive the form of the Hamiltonian using some of the deuteron's properties. The deuteron has total isospin $T=0$ and spin parity $J^{\pi}=1^+$. As $s_p=s_n=1/2$, the total spin could in principle be $S=1,0$. At the same time, parity conservation imposes some rules for the quantum number for the orbital angular momentum $L$ (together with $J-1 < L < J+1$): since parity follows rule $\pi=(-1)^l=+1$, only $L=0$ (S-wave) and $L=2$ (D-wave) are allowed. This means that the ground state of deuteron is a mixture of these two wavefunctions (which are connected through the tensor interaction). At this point, due to the asymmetry of the whole wavefunction in a system of two fermions, we have $S=1$ for the total spin.

These results lead us from the total Hamiltonian

$$ H=-\frac{\hbar^2}{M}\frac{1}{r}\frac{d^2}{dr^2}r+\frac{\hbar^2}{M}\frac{L(L+1)}{r^2}+V_C(r)+V_T(r)S_{12}
$$

into two radial equations describing the system, which after inserting the properties and quantum numbers of the deuteron have the next form:

$$ [\frac{\hbar^2}{M}\frac{d^2}{dr^2}+E-V_C(r)]u_s=\sqrt{8}V_T(r)u_d
$$

$$ [\frac{\hbar^2}{M}(\frac{d^2}{dr^2}-\frac{6}{r^2})+E+2V_T(r)-V_C(r)]u_d=\sqrt{8}V_T(r)u_s
$$

These are exactly the equations that our code will try to solve! So, we will **get the two wavefunctions $u_s$ and $u_d$ and the energy eigenvalue** (which, by experimental data, we know it is: $E=-2.225 MeV$).

Also, we must take into account the initial and boundary conditions we expect for this kind of system:

$$u_s(0)=u_d(0)=0, \hspace{0.5cm} u_s(\infty)=u_d(\infty)=0
$$

Apart from that, we will be able to also calculate the quadrupole moment Q. This term indicates that the charge distribution is not spherically symmetric. This is why we must take into account the d-wave $L=2$ case! If we only had L=0, since its wavefunction corresponds to spherical symmetry, we would get $Q=0$. This would also represent just a central potential for the interaction of the nucleons. Nevertheless, from experimental data we know that $Q=0.286e \cdot fm^2$. Therefore, everything fits perfectly with the previously described connection between the $L=0$ and $L=2$ wavefunctions and the non-central potential.

The value of Q is obtained through its definition:

$$Q=\sqrt{\frac{16 \pi}{5}} \langle J(M=J)|\hat{Q}_{20}|J(M=J) \rangle
$$

which can be further developed as:

$$Q= e \sqrt{\frac{16 \pi}{5}} \int \psi^*(J=M=1)(\vec{r}) \frac{r^2}{4} Y_{20}(\hat{r}) \psi(J=M=1)(\vec{r})d^3r,
$$

where $\psi$ is the total wavefunction in which we have both $u_s$ and $u_d$ as a linear combination, due to the fact that our system is a mixture of these two states. When we work with this formula, we finally reach the easy form of:

$$Q=\frac{1}{20} \int dr \cdot r^2 \cdot u_d(r) [\sqrt{8}u_s(r) - u_d(r)].
$$

This is exactly the formula used in the code to obtain the result of the quarupole moment, which will also work as a proof of the correctness of the model used.

## How to use the code

Let us describe the way in which this code works and what is each module used for.

- [generate_data.py](generate_data.py): here we insert the values for our model. Precisely, we will implement: the initial conditions and boundary conditions for both $u_s$ and $u_d$. We will insert two different combinations, because we will make use of the combination of two different solutions to reach the final result obeying all conditions. Also the range of the radius will be present, and the initial guess for the energy eigenvalue. All the data implemented will be saved in [deuteron_values.jsonl](deuteron_values.jsonl).
