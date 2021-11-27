# mpi-ISES
### Iteartive Solver of Equation Systems (in the terms of NI-MPI course in Czech Technical University)

The developed solution represents a toolchain for computing the number of iterations required to solve the system of equations using Jacobi and Gauss-Seigel methods. The toolchain itself consists of the following executables:

EquationSolver.py - the very python3 script used for task-defined computation
run.sh - bash script which is the core of a very toolchain. Is used for performing the calculations in the specified range of a Gamma variable.
plotter.py - python3 script to produce the vizualization of iterations number dependence upon the Gamma value.
How to run the toolchain?
The toolchain requires some additional command line arguments to run:

start - the initial value of gamma
step - represents the increase of a gamma value per each iteration
stop - the final value of gamma to computate
omega - omega parameter used in Gauss-Seidel method (set to 1 by default)
Example: bash ./run.sh 2 0.01 2.2 1 (increase the gamma value from 2 by 0.01 per each iteration, until gamma reaches the value of 2.2, keeping omega set to 1)

How it works?
The toolchain runs EquationSolver.py for each value of gamma in the specified range for both of Jacobi and Gauss-Seidel methods (omega is fixed), storing the results of each computation in temporary files. After all gammas in specified range were calculated, the script runs the visualization utility plotter.py which plots the number of iterations for each gamma value for both of methods.

How to run EquationSolver?
The very EquationSolver.py itself can be run without toolchain. Requires the following arguments:

gamma - gamma value to calculate for
method - True for Jacobi, False for Gauss-Seigel methods
omega - the omega value used in Gauss_Seigel method
Example: python3 EquationSolver.py 2.67 False 1

