#!/bin/bash

rm -rf ./results.out
mkdir -p ./out

#          start step stop
for g in $(seq $1 $2 $3)
do
    gamma=${g//,/.}
        
    python3 ./EquationSolver.py ${gamma} True 1 > ./tmp_Jacobi.out
    python3 ./EquationSolver.py ${gamma} False $4 > ./tmp_Gauss-Seidel.out # omega

    tmp=$(grep -Po -m 1 "Iterations: \d+" ./tmp_Jacobi.out)
    JC=$(grep -Po -m 1 "\d+" <<< "${tmp}")

    tmp=$(grep -Po -m 1 "Iterations: \d+" ./tmp_Gauss-Seidel.out)
    GS=$(grep -Po -m 1 "\d+" <<< "${tmp}")

    echo "${gamma}; ${JC}; ${GS};" >> results.out

    echo "Gamma: ${gamma}"
    echo "JC:    ${JC}"
    echo "GS:    ${GS} ($4)"
    
done

# # plotting a distribution of results
python3 ./plotter.py ./results.out ./out/$1-$2-$3-results-$4.png

rm -rf ./tmp_Jacobi.out
rm -rf ./tmp_Gauss-Seidel.out