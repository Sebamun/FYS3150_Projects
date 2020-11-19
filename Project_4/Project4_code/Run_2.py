import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import subprocess
import os
num_spins = 20 # Antall spinn.
mcs = 1000000 # Monte Carlo cycles.
init_temp = 0.9
final_temp = 1.1
temp_step = 0.1
proc = 6 # Antall kjerner.
T_1 = 1.0
fig, axs = plt.subplots(1, 2, sharex=True, sharey=True)
subprocess.run(['mpirun', '-n', str(proc), './code.x', 'Textfiles/Output_2.txt', \
str(num_spins), str(mcs), str(init_temp), str(final_temp), str(temp_step), str(T_1)])

df = pd.read_csv("Energier", delim_whitespace=True, \
names=["E", "M"]) # Leser av tekstfilen.
mcs_array = np.linspace(0,mcs,len(np.array(df['E'])))
axs[0].plot(mcs_array, np.array(df['E'])/(num_spins**2))
axs[1].plot(mcs_array, np.array(df['M'])/(num_spins**2))

init_temp = 2.3
final_temp = 2.5
T_2 = 2.4

subprocess.run(['mpirun', '-n', str(proc), './code.x', 'Textfiles/Output_2.txt', \
str(num_spins), str(mcs), str(init_temp), str(final_temp), str(temp_step), str(T_2)])
df2 = pd.read_csv("Energier", delim_whitespace=True, \
names=["E2", "M2"]) # Leser av tekstfilen.
axs[0].plot(mcs_array, np.array(df2['E2'])/(num_spins**2))
axs[1].plot(mcs_array, np.array(df2['M2'])/(num_spins**2))
axs[0].set_xlabel('Cycles')
axs[0].set_ylabel('Energy')
axs[1].set_xlabel('Cycles')
axs[1].set_ylabel('Magnetization')
plt.show()

'''
os.remove("E_values.txt") # Removes the file (for reset purposes).
# Initialverdier:
num_spins = 20 # Antall spinn.
mcs = np.linspace(0,400000,81) # Monte Carlo cycles.
init_temp = 2.35
final_temp = 2.45
temp_step = 0.05
proc = 6 # Antall kjerner.
T_1 = 2.4#1.0 # Temper
a = open("E_values.txt", "a+")

for i in range(len(mcs)):
    # Kjoorer programmet vårt:
    subprocess.run(['mpirun', '-n', str(proc), './code.x', 'Textfiles/Output_2.txt', \
    str(num_spins), str(mcs[i]), str(init_temp), str(final_temp), str(temp_step)])
    # Skriver om til dataframe:
    df = pd.read_csv("Textfiles/Output_2.txt", delim_whitespace=True, \
    names=["T","E_tot","E_var","M_tot","M_var","M_abs"]) # Leser av tekstfilen.
    # Skriver energiverdiene til en annen fil:
    value = np.array(df.loc[df['T'] == T_1]['E_tot'])[0]
    a.write(str(value))
    a.write(' ')
a.close()

r = open("E_values.txt", "r")
for line in r:
    q = line.split()
    E = np.array(q)
    E = E.astype(np.float)
plt.plot(mcs,E)
plt.show()
'''
