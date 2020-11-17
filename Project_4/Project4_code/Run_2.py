import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import subprocess
import os
os.remove("E_values.txt") # Removes the file (for reset purposes).
# Initialverdier:
num_spins = 20 # Antall spinn.
mcs = np.linspace(0,50000,200) # Monte Carlo cycles.
init_temp = 0.95
final_temp = 1.05
temp_step = 0.05
proc = 6 # Antall kjerner.
T_1 = 1.0 # Temper
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
