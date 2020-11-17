import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# Skriver om til dataframe:
df = pd.read_csv("Output.txt", delim_whitespace=True, \
names=["T","E_tot","E_var","M_tot","M_var","M_abs"]) # Leser av tekstfilen.
# Initialverdier:
num_spins = 2 # Antall spinn.
k = 1.0 # Boltzmann konstant.
T = 1.0 # Temperatur.
beta = 1/(k*T)
Z = 4*np.cosh(8*beta) + 12
# Energi:
E_num = np.array(df.loc[df['T'] == T]['E_tot'])[0] # Finner den numeriske verdien for E_m.
E_ana = -32*(np.sinh(8*beta)/Z) / num_spins / num_spins # Den analytiske verdien for E_m.
diff_E = np.abs(E_num-E_ana)
# Magnetisering:
M_num = np.array(df.loc[df['T'] == T]['M_tot'])[0]
M_ana = 0
diff_M = np.abs(M_num-M_ana)
# Varmekapastitet:
E_var = np.array(df.loc[df['T'] == T]['E_var'])[0]
C_num = beta * E_var**2
C_ana = beta * ((256*np.cosh(8*beta) / Z) - (-32*(np.sinh(8*beta)) / Z)**2) / (num_spins**4)
diff_C = np.abs(C_ana-C_num)
print(C_num)
print(((256*np.cosh(8*beta) / Z) - (-32*(np.sinh(8*beta)) / Z)**2) / 4)
#Susceptibilitet:
M_var = np.array(df.loc[df['T'] == T]['M_var'])[0]
Chi_num = beta * M_var**2
Chi_ana = beta * (32*np.exp(8)+128) / Z # Faar feil svar når jeg tar per spinn her?
diff_Chi = np.abs(Chi_num-Chi_ana)
# Printing:
print("The difference is {:.5f} for the mean energy." .format(diff_E))
print("The difference is {:.5f} for the mean magnetization." .format(diff_M))
print("The difference is {:.5f} for the heat capacity." .format(diff_C))
print("The difference is {:.5f} for the susceptibility." .format(diff_Chi))
# Plotting:
plt.title('Energy')
plt.plot(df['T'], df['E_tot'])
plt.plot(T, E_ana, 'o', label=f'Analytical value at T={T}')
plt.xlabel('T [K]')
plt.ylabel('Joule/n^2 [J]')
plt.legend()
plt.show()
plt.title('Magnetization')
plt.plot(df['T'], df['M_tot'])
plt.plot(T, M_ana, 'o', label=f'Analytical value at T={T}')
plt.xlabel('T')
plt.legend()
plt.show()
plt.title('Heat capacity')
plt.plot(df['T'], beta * np.array(df['E_var'])**2)
plt.plot(T, C_ana, 'o', label=f'Analytical value at T={T}')
plt.xlabel('T')
plt.legend()
plt.show()
plt.title('Susceptibility')
plt.plot(df['T'], beta * np.array(df['M_var'])**2)
plt.plot(T, Chi_ana, 'o', label=f'Analytical value at T={T}')
plt.xlabel('T')
plt.legend()
plt.show()
