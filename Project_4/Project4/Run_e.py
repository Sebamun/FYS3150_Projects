import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import subprocess
import os

num_spins = 20 # Antall spinn.
mcs = 2000000 # Monte Carlo cycles.
proc = 1 # Antall kjerner.

init_temp = 1.0
final_temp = 1.01
temp_step = 0.1
T_1 = 1.0

subprocess.run(['mpirun', '-n', str(proc), './code.x', 'Textfiles/Output_2.txt', \
str(num_spins), str(mcs), str(init_temp), str(final_temp), str(temp_step), str(T_1), "0", "0"])

df1 = pd.read_csv("Energier.txt", delim_whitespace=True, \
names=["E_1"]) # Leser av tekstfilen.
Energier_1 = np.array(df1["E_1"])/num_spins**2


var_1_str = "$\sigma^2 = %.2e$"%(np.var(Energier_1))
fig, ax = plt.subplots()
ax.hist(Energier_1, 100, density=True, range=(-2.0, -1.90))
ax.text(0.60, 0.90, var_1_str, transform=ax.transAxes, fontsize=14,
        verticalalignment='top')
plt.savefig("Hist_1.png", dpi=200)
plt.show()


init_temp = 2.4
final_temp = 2.41
T_2 = 2.4

subprocess.run(['mpirun', '-n', str(proc), './code.x', 'Textfiles/Output_2.txt', \
str(num_spins), str(mcs), str(init_temp), str(final_temp), str(temp_step), str(T_2), "0", "0"])

df24 = pd.read_csv("Energier.txt", delim_whitespace=True, \
names=["E_24"]) # Leser av tekstfilen.
Energier_24 = np.array(df24["E_24"])/num_spins**2
var_24_str = "$\sigma^2 = %.3f$"%(np.var(Energier_24))

fig, ax = plt.subplots()
ax.hist(Energier_24, 200, density=True)
ax.text(0.80, 0.95, var_24_str, transform=ax.transAxes, fontsize=14,
        verticalalignment='top')
plt.savefig("Hist_24.png", dpi=200)
plt.show()
