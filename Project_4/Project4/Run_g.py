import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import subprocess

# Initialverdier:
mcs = 1800000  # Monte Carlo cycles.
init_temp = 2.27
final_temp = 2.30
temp_step = 0.001
proc = 6
T_1 = 0

df = {}
E_var = {}
T = {}
E = {}
M_abs = {}
C_num = {}
M_var = {}
Chi_num = {}
L = [40, 60, 80, 100] #Antall spinn
def plot_C(T, C_num, num_spins):
    plt.plot(T, C_num, label="L=%i"%(num_spins))

max_T = np.zeros(len(L))
for i, num_spins in enumerate(L, 0):
    # Kjoorer programmet vårt:
    subprocess.run(['mpirun', '-n', str(proc), './code.x', "Textfiles/Output_%i.txt" % (num_spins),
                    str(num_spins), str(mcs), str(init_temp), str(final_temp), str(temp_step), str(T_1), '1', '0'])
    df["df_%i" % (num_spins)] = pd.read_csv("Textfiles/Output_%i.txt" % (num_spins), delim_whitespace=True,
                     names=["T_%i" % (num_spins), "E_%i" % (num_spins), "E_var_%i" % (num_spins),
                     "M_tot_%i" % (num_spins), "M_var_%i" % (num_spins), "M_abs_%i" % (num_spins)])  # Leser av tekstfilen.

    E_var["E_var%i"%(num_spins)] = np.array(df["df_%i"%(num_spins)]["E_var_%i"%(num_spins)])
    T["T_%i"%(num_spins)] = np.array(df["df_%i"%(num_spins)]["T_%i"%(num_spins)])
    C_num["C_num_%i"%(num_spins)] =  E_var["E_var%i"%(num_spins)]/num_spins**2

    max_C = np.amax(C_num["C_num_%i"%(num_spins)])
    max_T_index = np.where(C_num["C_num_%i"%(num_spins)] == max_C)[0][0]
    print(max_T_index)
    max_T[i] = T["T_%i"%(num_spins)][max_T_index]

    plot_C(T["T_%i"%(num_spins)], C_num["C_num_%i"%(num_spins)], num_spins)
# Skriver om til dataframe:

plt.xlabel("T")
plt.ylabel("$C_V$")
plt.title("MCC=1.8e6, $\Delta T=0.001$")
plt.legend()
plt.savefig('Exp_values_zoom.png', dpi=200)
plt.show()

T = np.arange(2.27, 2.300, 0.001)
T_c_L = np.array([T[5], T[10], T[14], T[21]])
L_inv = 1/L

slope, intercept, r_val, p_val, std_err = stats.linregress(L_inv, T_c)

print(intercept)
