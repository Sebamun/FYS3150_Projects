import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import subprocess
# Initialverdier:
num_spins = 2 # Antall spinn.
init_temp = 1
final_temp = 4
temp_step = 0.01
proc = 6
T_0 = 0

def compare_energies(mcs_array):
    d_E_array = np.zeros(len(mcs_array))
    d_M_array = np.zeros(len(mcs_array))
    for i, mcs in enumerate(mcs_array, 0):
        # Kjoorer programmet vårt:
        subprocess.run(['mpirun', '-n', str(proc), './code.x', 'Textfiles/Output_1.txt', \
        str(num_spins), str(mcs), str(init_temp), str(final_temp), str(temp_step), str(T_0), "0", "1"])
        # Skriver om til dataframe:
        df = pd.read_csv("Textfiles/Output_1.txt", delim_whitespace=True, \
        names=["T","E_tot","E_var","M_tot","M_var","M_abs"]) # Leser av tekstfilen.
        E = np.array(df["E_tot"])
        T = np.array(df["T"])
        M_abs = np.array(df["M_abs"])
        beta = 1/(T)
        Z = 4*np.cosh(8*beta) + 12
        E_ana = -32*(np.sinh(8*beta)/Z) / num_spins / num_spins
        diff_E_mean = np.sum(np.abs(E-E_ana))/len(E)
        d_E_array[i] = diff_E_mean

        M_ana = 8 * (2 + np.exp(8 * beta )) / Z / num_spins**2
        diff_M_mean = np.sum(np.abs(M_abs-M_ana))/len(M_abs)
        d_M_array[i] = diff_M_mean

    fig, axs = plt.subplots(1,2)
    axs[0].plot(mcs_array, d_E_array)
    axs[0].set_ylabel("$J$")
    axs[0].grid(True)
    axs[1].plot(mcs_array, d_M_array)
    axs[1].set_xlabel("MCC")
    axs[1].set_ylabel("$< |M| >$")
    axs[1].grid(True)
    fig.tight_layout()
    plt.suptitle('Mean difference between analytical and numerical values', y=1.0)
    plt.savefig("Diff_vs_mcs.png", dpi=200)
    plt.show()

mcs_array = np.array([5e2, 1e3, 2e3, 3e3, 4e3, 5e3, 6e3, 8e3, 9e3, 1e4, 2e4, 3e4, 5e4, 6e4, 7e4, 8e4, 9e4, 1e5])
compare_energies(mcs_array)

mcs = 500000 # Monte Carlo cycles.

# Kjoorer programmet vårt:
subprocess.run(['mpirun', '-n', str(proc), './code.x', 'Textfiles/Output_1.txt', \
str(num_spins), str(mcs), str(init_temp), str(final_temp), str(temp_step), str(T_0), "0"])
# Skriver om til dataframe:
df = pd.read_csv("Textfiles/Output_1.txt", delim_whitespace=True, \
names=["T","E_tot","E_var","M_tot","M_var","M_abs"]) # Leser av tekstfilen.

E = np.array(df["E_tot"])
T = np.array(df["T"])
E_var = np.array(df["E_var"])
M_tot = np.array(df["M_tot"])
M_var = np.array(df["M_var"])
M_abs = np.array(df["M_abs"])

# Initialverdier for analytiske beregninger:
k = 1.0 # Boltzmann konstant.
beta = 1/(k*T)
Z = 4*np.cosh(8*beta) + 12

E_ana = -32*(np.sinh(8*beta)/Z) / num_spins / num_spins # Den analytiske verdien for E_m.
diff_E_mean = np.sum(np.abs(E-E_ana))/len(E)
# Magnetisering:
M_ana = 8 * (2 + np.exp(8 * beta )) / Z / num_spins**2
diff_M_mean = np.sum(np.abs(M_abs-M_ana))/len(M_abs)
# Varmekapastitet:
C_num = E_var / num_spins**2 # * beta
C_ana = 1024 * beta * (3 * np.cosh(8 * beta) + 1) / T / Z**2  / num_spins**2
diff_C_mean = np.sum(np.abs(C_ana-C_num))/len(C_num)
#Susceptibilitet:
Chi_num =  M_var  / num_spins**2
Chi_ana = (32 * beta * ( 1 + np.exp(8 * beta)) / Z - 64 * beta * ( 2 + np.exp( 8 * beta ))**2 / Z**2)  / num_spins**2
diff_Chi_mean = np.sum(np.abs(Chi_num-Chi_ana))/len(Chi_num)
# Printing:
print("The mean difference is {:.5f} for the mean energy is:" .format(diff_E_mean))
print("The mean difference is {:.5f} for the mean magnetization is:" .format(diff_M_mean))
print("The mean difference is {:.5f} for the heat capacity is:" .format(diff_C_mean))
print("The mean difference is {:.5f} for the susceptibility is:" .format(diff_Chi_mean))
# Plotting:

fig, axs = plt.subplots(2, 2)
axs[0,0].set_title('Energy')
axs[0,0].plot(T, E) #, label='Numerical value')
axs[0,0].plot(T, E_ana, '--') #, label=f'Analytical value')
axs[0,0].set_xlabel('T [K]')
axs[0,0].set_ylabel('J')
axs[0,0].legend()
axs[0,0].grid(True)

axs[0,1].set_title('Magnetization')
axs[0,1].plot(T, M_abs, label='Numerical value')
axs[0,1].plot(T, M_ana, '--', label=f'Analytical value')
axs[0,1].set_xlabel('T [K]')
axs[0,1].set_ylabel('M')
axs[0,1].legend(loc='lower left')
axs[0,1].grid(True)

axs[1,0].set_title('Heat capacity')
axs[1,0].plot(T, C_num) #, label='Numerical value')
axs[1,0].plot(T, C_ana, '--') #, label=f'Analytical value')
axs[1,0].set_xlabel('T [K]')
axs[1,0].set_ylabel('$J/K$')
axs[1,0].legend()
axs[1,0].grid(True)

axs[1,1].set_title('Susceptibility')
axs[1,1].plot(T, Chi_num) #, label='Numerical value')
axs[1,1].plot(T, Chi_ana, '--') #, label=f'Analytical value')
axs[1,1].set_xlabel('T [K]')
axs[1,1].set_ylabel('$1/J$')
axs[1,1].legend()
fig.tight_layout()
axs[1,1].grid(True)
plt.savefig('Exp_values_2x2_5e5.png', dpi=200)
plt.show()
