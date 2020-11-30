import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import subprocess
import os
num_spins = 20 # Antall spinn.
mcs = 3e5 # Monte Carlo cycles.
proc = 1 # Antall kjerner.

#Simulation for T=1.0, uniform spins
init_temp = 1.0
final_temp = 1.01
temp_step = 0.1
T_1 = 1.0

subprocess.run(['mpirun', '-n', str(proc), './code.x', 'Textfiles/Output_2.txt', \
str(num_spins), str(mcs), str(init_temp), str(final_temp), str(temp_step), str(T_1), "1", "1"])

df1_uni = pd.read_csv("E_M.txt", delim_whitespace=True, \
names=["E_1", "M_1", "n_flips"]) # Leser av tekstfilen.
mcs_array = np.linspace(0,mcs,len(np.array(df1_uni['E_1'])))

E_exp_1_uni = np.array(df1_uni['E_1'])/(num_spins**2)
M_exp_1_uni = np.array(df1_uni['M_1'])/(num_spins**2)
n_flips_1_uni = np.array(df1_uni['n_flips'])


#Simulation for T=1.0, random spins
subprocess.run(['mpirun', '-n', str(proc), './code.x', 'Textfiles/Output_2.txt', \
str(num_spins), str(mcs), str(init_temp), str(final_temp), str(temp_step), str(T_1), "0", "1"])

df1_rand = pd.read_csv("E_M.txt", delim_whitespace=True, \
names=["E_1", "M_1", "n_flips"]) # Leser av tekstfilen.
mcs_array = np.linspace(0,mcs,len(np.array(df1_rand['E_1'])))

E_exp_1_rand = np.array(df1_rand['E_1'])/(num_spins**2)
M_exp_1_rand = np.array(df1_rand['M_1'])/(num_spins**2)
n_flips_1_rand = np.array(df1_rand['n_flips'])

#Simulation for T=2.4
init_temp = 2.4
final_temp = 2.41
T_2 = 2.4

subprocess.run(['mpirun', '-n', str(proc), './code.x', 'Textfiles/Output_2.txt', \
str(num_spins), str(mcs), str(init_temp), str(final_temp), str(temp_step), str(T_2), "1", "1"])
df24_uni = pd.read_csv("E_M.txt", delim_whitespace=True, \
names=["E_24", "M_24", "n_flips"]) # Leser av tekstfilen.

E_exp_24_uni = (np.array(df24_uni["E_24"]).astype(np.float))/num_spins**2#np.array(df24["E_24"])/(num_spins**2)
M_exp_24_uni = np.array(df24_uni["M_24"]).astype(np.float)/num_spins**2
n_flips_24_uni = np.array(df24_uni['n_flips'])

#Simulation for T=2.4, random spins
subprocess.run(['mpirun', '-n', str(proc), './code.x', 'Textfiles/Output_2.txt', str(num_spins), str(mcs), str(init_temp), str(final_temp), str(temp_step), str(T_2), "0", "1"])

df24_rand = pd.read_csv("E_M.txt", delim_whitespace=True, names=["E_24", "M_24", "n_flips"]) # Leser av tekstfilen.
E_exp_24_rand = np.array(df24_rand['E_24'])/(num_spins**2)
M_exp_24_rand = np.array(df24_rand['M_24']).astype(np.float)/(num_spins**2)
n_flips_24_rand = np.array(df24_rand['n_flips'])


fig, axs = plt.subplots(1, 2)
axs[0].plot(mcs_array, E_exp_1_uni, label='T=1.0, Uni')
axs[1].plot(mcs_array, M_exp_1_uni, label='T=1.0, Uni')
axs[0].plot(mcs_array, E_exp_24_uni, label='T=2.4, Uni')
axs[1].plot(mcs_array, M_exp_24_uni, label='T=2.4, Uni')
axs[0].plot(mcs_array, E_exp_1_rand, "--", label='T=1.0, Rand')
axs[1].plot(mcs_array, M_exp_1_rand, "--", label='T=1.0, Rand')
axs[0].plot(mcs_array, E_exp_24_rand, "--", label='T=2.4, Rand')
axs[1].plot(mcs_array, M_exp_24_rand,"--" , label='T=2.4, Rand')
axs[0].set_xlabel('MCC')
axs[0].set_ylabel('J')
axs[1].set_xlabel('MCC')
axs[1].set_ylabel('$<|M|>$')
axs[0].grid(True)
axs[1].grid(True)
axs[1].set_title("Mean absolute magnetization")
axs[0].set_title("Mean energy")
plt.legend()
fig.tight_layout()
plt.savefig("Uni_vs_rand.png", dpi=95)
plt.show()

plt.plot(mcs_array, n_flips_1_uni, label='Uniformly initialized')
plt.plot(mcs_array, n_flips_1_rand,"--", label='Randomly initialized')
plt.title("Number of total accepted flips, T=1.0, L=20")
plt.xlabel("MCC")
plt.ylabel("N")
plt.legend()
plt.grid(True)
plt.savefig("n_flips_1.png", dpi=200)
plt.show()
plt.plot(mcs_array, n_flips_24_uni, label='Uniformly initialized')
plt.plot(mcs_array, n_flips_24_rand,"--", label='Randomly initialized')
plt.title("Number of total accepted flips, T=2.4, L=20")
plt.xlabel("MCC")
plt.ylabel("N")
plt.grid(True)
plt.legend()
plt.savefig("n_flips_24.png", dpi=200)
plt.show()
