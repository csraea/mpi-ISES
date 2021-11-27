import sys

import matplotlib.pyplot as plt
import csv
import pandas as pd
import numpy as np
from matplotlib.ticker import AutoMinorLocator
from matplotlib import gridspec



import warnings
from pandas.core.common import SettingWithCopyWarning
warnings.simplefilter(action="ignore", category=SettingWithCopyWarning)

plt.style.use("seaborn")
fig, ax = plt.subplots(1, figsize=(40,15))


#read 4th column of csv file
gamma = []         # an empty list to store the gamma value
jc = []            # an empty list to store the number of iterations (Jacobi)
gs = []            # an empty list to store the number of iterations (Gauss-Seidel)
with open(sys.argv[1], 'r') as rf:
    reader = csv.reader(rf, delimiter=';')
    for row in reader:
      gamma.append(np.float64(row[0]))
      jc.append(round(np.float64(row[1])))
      gs.append(round(np.float64(row[2])))

plt.plot(gamma, jc, label="Jacobi", color="red")
plt.plot(gamma, gs, label="Gauss-Seidel", color="blue")

plt.legend(fontsize=24)

plt.title("Number of iterations depending on Gamma", fontsize=28)

plt.xticks(gamma, gamma, fontsize=8)
plt.yticks(gs + jc, gs + jc, fontsize=8)

plt.xlabel("Gamma", fontsize=24)
plt.ylabel("Iterations", fontsize=24)

# print(times)

# plt.show()

plt.savefig(sys.argv[2])