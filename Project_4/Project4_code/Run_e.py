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
str(num_spins), str(mcs), str(init_temp), str(final_temp), str(temp_step), str(T_1)])

df1 = pd.read_csv("Energier.txt", delim_whitespace=True, \
names=["E_1"]) # Leser av tekstfilen.
Energier_1 = np.array(df1["E_1"])[1000000:]/num_spins**2

plt.hist(Energier_1, 50)
plt.savefig("Hist_1.png", dpi=95)
plt.show()

init_temp = 2.4
final_temp = 2.41
T_2 = 2.4

subprocess.run(['mpirun', '-n', str(proc), './code.x', 'Textfiles/Output_2.txt', \
str(num_spins), str(mcs), str(init_temp), str(final_temp), str(temp_step), str(T_2)])

df24 = pd.read_csv("Energier.txt", delim_whitespace=True, \
names=["E_24"]) # Leser av tekstfilen.
Energier_24 = np.array(df24["E_24"])[1000000:]/num_spins**2

plt.hist(Energier_24, 50)
plt.savefig("Hist_24.png", dpi=95)
plt.show()

print(np.var(Energier_1))
print(np.var(Energier_24))
