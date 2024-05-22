"""Here we will implement the secant method manually in order to apply
it to many functions. This is something we need in our problem, since
there are two eigenfunctions which must be continuous in the matching
point. Also their derivatives must me smooth.

"""

import numpy as np
import find_eigenvalue as find

def secant_method(funcs, E0, E1, tol=1e-6, max_iter=100):
    """This function takes functions and uses the secant method to find
    the energy value which gives the root for all of them.

    Inputs:
        - funcs: vector carrying all the functions we must evaluate
        - E0: first guess for the energy value
        - E1: second guess for the energy value
    Output:
        - Energy value leading all functions to zero. If there is no
          valid result, an Error comment will appear on screen
    """
    # Start the iterative process
    for _ in range(max_iter):
        # Evaluate functions with E0 and E1
        f0 = find.error_E(E0)
        f1 = find.error_E(E1)
        
        # Approximation used in the secant method
        dE = E1 - E0
        df = f1 - f0
        f_prime = df / dE
        
        # Avoid /0 division
        if np.all(f_prime == 0):
            raise ValueError("/0 divison for secant method")
        
        # New approximation of E value
        E_new = E1 - f1.sum() / f_prime.sum()
        
        # Look for convergence
        if np.abs(E_new - E1) < tol:
            return E_new
        
        # Get new values for another iteration
        E0, E1 = E1, E_new
    
    raise ValueError("This method does not find a convergent solution")
