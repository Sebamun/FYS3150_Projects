import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import subprocess
import os
num_spins = 20 # Antall spinn.
mcs = 1000000 # Monte Carlo cycles.
proc = 1 # Antall kjerner.

#Simulation for T=1.0
init_temp = 1.0
final_temp = 1.01
temp_step = 0.1
T_1 = 1.0

subprocess.run(['mpirun', '-n', str(proc), './code.x', 'Textfiles/Output_2.txt', \
str(num_spins), str(mcs), str(init_temp), str(final_temp), str(temp_step), str(T_1)])

df1 = pd.read_csv("E_M.txt", delim_whitespace=True, \
names=["E_1", "M_1"]) # Leser av tekstfilen.
mcs_array = np.linspace(0,mcs,len(np.array(df1['E_1'])))

E_exp_1 = np.array(df1['E_1'])/(num_spins**2)
M_exp_1 = np.array(df1['M_1'])/(num_spins**2)

fig, axs = plt.subplots(1, 2, sharex=True, sharey=True)
axs[0].plot(mcs_array, E_exp_1, label='Energy, T=1.0')
axs[1].plot(mcs_array, M_exp_1, label='Magnetization, T=1.0')


#Simulation for T=2.4
init_temp = 2.3
final_temp = 2.5
T_2 = 2.4

subprocess.run(['mpirun', '-n', str(proc), './code.x', 'Textfiles/Output_2.txt', \
str(num_spins), str(mcs), str(init_temp), str(final_temp), str(temp_step), str(T_2)])
df24 = pd.read_csv("E_M.txt", delim_whitespace=True, \
names=["E_24", "M_24"]) # Leser av tekstfilen.

E_exp_24 = (np.array(df24["E_24"]).astype(np.float))/num_spins**2#np.array(df24["E_24"])/(num_spins**2)
M_exp_24 = np.array(df24["M_24"]).astype(np.float)/num_spins**2

axs[0].plot(mcs_array, E_exp_24 , label='Energy, T=2.4')
axs[1].plot(mcs_array, M_exp_24, label='Magnetization, T=2.4')
axs[0].set_xlabel('Cycles')
axs[0].set_ylabel('Energy')
axs[1].set_xlabel('Cycles')
axs[1].set_ylabel('Magnetization')
plt.legend()
plt.show()
