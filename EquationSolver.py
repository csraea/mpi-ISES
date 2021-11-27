import sys
import numpy as np
from pprint import pprint

class EquationSolver:

    # Initiates the instance for specific gamma value
    def __init__(self, gamma):

        sys.setrecursionlimit(10000)
        
        # matrix A
        self.a = np.zeros((20, 20), dtype=np.float64)
        np.fill_diagonal(self.a, gamma)
        np.fill_diagonal(self.a[:, 1:], -1)
        np.fill_diagonal(self.a[1:], -1)

        # vector b
        self.b = np.full((20, 1), gamma-2, dtype=np.float64)
        self.b[0], self.b[-1] = gamma - 1, gamma - 1

        # matrix D
        self.d = np.diag(np.diag(self.a))

        # matrix L
        self.l = np.tril(self.a, -1)

        # matrix U
        self.u = self.a - self.d - self.l

        # set default precision
        self.precision = 10**-6


    # Sets the calculation method
    def set_method(self, method, omega = 1):

        self.q = self.d if method else (self.d / omega) + self.l
        self.q_inv = np.linalg.inv(self.q)
        self.convergent = None
        self.result = None
        self.iterations = None

        return self
    

    # Checks if iterative method is convergent and computes the result
    def compute(self):

        if not self.is_convergent():
            self.result = []
            self.iterations = 0
        if self.iterations is None:
            self.result, self.iterations = self.calculate()

        return self.result, self.iterations


    # Calculates convergence of iterative method
    def is_convergent(self):

        if self.convergent is None:                                                         
            self.convergent = max(abs(np.linalg.eigvals(np.identity(20, dtype=np.float64) - (self.q_inv @ self.a)))) < 1

        return self.convergent


    # Calculate with the iterative method
    def calculate(self, xn=None, idx=0):

        if xn is None:
            xn = np.zeros((20, 1), np.float64)
        if self.is_precision_sufficient((self.a @ xn) - self.b):
            return xn.transpose(), idx
        
        return self.calculate(self.calc_it(xn), idx + 1)

    
    # Checks whether the precision of resuslt is satisfactory
    def is_precision_sufficient(self, result):

        return self.precision > (np.linalg.norm(result) / np.linalg.norm(self.b))


    # Calculates single iteration
    def calc_it(self, xn):

        return (self.q_inv @ (((self.q - self.a) @ xn) + self.b))


def str2bool(v):
    return str(v).lower() in ("yes", "true", "t", "1")

def main():
    # Create a solver class and pass a gamma value as a parameter.
    es = EquationSolver(np.float64(sys.argv[1]))

    # Set the method which is used for a computation
    # True: Jacobi method; does not require additional parameters
    # False: Gauss-Seidel method; is to be set with the optional parameter omega (defult value is 1)
    es.set_method(str2bool(sys.argv[2]), np.float64(sys.argv[3]))

    # Start the very calculation
    result, iterations = es.compute() # compute the approximation of the equation using the iterative method


    print("Method: Jacobi" if str2bool(sys.argv[2]) else "Method: Gauss-Seidel")
    print("Gamma: " + sys.argv[1])
    print("Omega: " + sys.argv[3])

    # Get information about the convergence of the iteration method
    # Retuens True if the method converges, elsewise returns False
    print("Method covergence: " + str(es.is_convergent()))

    # Print the number of iterations
    print("Iterations: " + str(iterations))

    # Print the result of an approximation
    pprint(result)


if __name__ == "__main__":
    main()