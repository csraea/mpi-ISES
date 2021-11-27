# mpi-ISES
### Iteartive Solver of Equation Systems (in the terms of NI-MPI course in Czech Technical University)

The developed solution represents a toolchain for computing the number of iterations required to solve the system of equations using Jacobi and Gauss-Seigel methods. The toolchain itself consists of the following executables:
1. `EquationSolver.py` - the very python3 script used for task-defined computation
2. `run.sh` - bash script which is the core of a very toolchain. Is used for performing the calculations in the specified range of a Gamma variable.
3. `plotter.py` - python3 script to produce the vizualization of iterations number dependence upon the Gamma value. 

#### _How to run the toolchain?_

The toolchain requires some additional command line arguments to run:
1. _start_ - the initial value of gamma
2. _step_  - represents the increase of a gamma value per each iteration
3. _stop_  - the final value of gamma to computate
4. _omega_ - omega parameter used in Gauss-Seidel method (set to 1 by default)

Example: `bash ./run.sh 2 0.01 2.2 1` (increase the gamma value from 2 by 0.01 per each iteration, until gamma reaches the value of 2.2, keeping _omega_ set to 1)

#### _How it works?_
The toolchain runs `EquationSolver.py` for each value of gamma in the specified range for both of Jacobi and Gauss-Seidel methods (omega is fixed), storing the results of each computation in temporary files. After all gammas in specified range were calculated, the script runs the visualization utility `plotter.py` which plots the number of iterations for each gamma value for both of methods.

#### _How to run EquationSolver?_
The very `EquationSolver.py` itself can be run without toolchain. Requires the following arguments:
1. _gamma_ - gamma value to calculate for
2. _method_ - `True` for Jacobi, `False` for Gauss-Seigel methods
3. _omega_ - the omega value used in Gauss_Seigel method

Example: `python3 EquationSolver.py 2.67 False 1`


