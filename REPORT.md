# NI-MPI - Domácí úkol ZS 2021/2022
#### Author:   Oleksandr Korotetskyi
#### Date:   27.11.2021
### Iteartive Solver of Equation Systems

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

## Results
### Mandatory variants

| Variant | Iterations | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Details&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Comment |
|:--------:|:-------------:|:--------------:|:--------------------------------:|
| Jacobi a | 15            | $\gamma = 5$   |                                  |
| Jacobi b | 987           | $\gamma = 2$   |                                  |
| Jacobi c | -             | $\gamma = 0.5$ | Iteration method does not converge |
| Gauss-Seidel a | 10 | $\gamma = 5$ |  |
| Gauss-Seidel b | 495 | $\gamma = 2$ |  |
| Gauss-Seidel c | - | $\gamma = 0.5$ | Iteration method does not converge |

### Optional variants
| Variant | Iterations | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Details&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Comment |
|:-:|:-:|:-:|:-:|
| Jacobi 2.004 | 850 | $\gamma = 2.004$ |  |
| Jacobi 4 | 20 | $\gamma = 4$   |  |
| Jacobi 16 | 7 | $\gamma = 16$   |  |
| Gauss-Seidel $2.004$ | 427 | $\gamma = 2.004$ |  |
| Gauss-Seidel 4 | 13 | $\gamma = 4$ |  |
| Gauss-Seidel 16 | 6 | $\gamma = 16$ |  |
| Gauss-Seidel $\omega = 0.5$ | 1488 | $\gamma = 2$, $\omega = 0.5$ |  |
| Gauss-Seidel $\omega = 1.5$ | 161 | $\gamma = 2$, $\omega = 1.5$ |  |
| Gauss-Seidel $\omega = 2$ | - | $\gamma = 2$, $\omega = 2$ | Iteration method does not converge |

In conclusion, it appears that Gauss-Seidel method takes the smaller number of iterations to solve the system of equations comparely to Jacobi method. The decrease of _omega_ (< 1) value in the case of Gauss-Seidel method increases the number of iterations required. In contrast, the increse reduces (up to 2).

![results.png at the project directory](./results.png "plot")
