import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import subprocess
# Initialverdier:
mcs = 1000000  # Monte Carlo cycles.
init_temp = 2.0
final_temp = 2.5
temp_step = 0.05
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
fig, axs = plt.subplots(2, 2)
axs[0,0].set_title('Energy')
axs[0,0].set_xlabel('T [K]')
axs[0,0].set_ylabel('$J$')
axs[0,1].set_title('Magnetization')
axs[0,1].set_xlabel('T [K]')
axs[0,1].set_ylabel('$< |M| >$')
axs[1,0].set_title('Heat capacity')
axs[1,0].set_xlabel('T [K]')
axs[1,0].set_ylabel('$J/K$')
axs[1,1].set_title('Susceptibility')
axs[1,1].set_xlabel('T [K]')
axs[1,1].set_ylabel('$1/J$')
def plot(T, E, M_abs, C_num, Chi_num, num_spins):
    axs[0,0].plot(T, E, label='L=%i'%(num_spins))
    axs[0,0].grid(True)
    axs[0,1].plot(T, M_abs, label='L=%i'%(num_spins))
    axs[0,1].grid(True)
    axs[1,0].plot(T, C_num, label='L=%i'%(num_spins))
    axs[1,0].grid(True)
    axs[1,1].plot(T, Chi_num, label='L=%i'%(num_spins))
    axs[1,1].grid(True)
for num_spins in L:
    # Kjoorer programmet vårt:
    subprocess.run(['mpirun', '-n', str(proc), './code.x', "Textfiles/Output_%i.txt" % (num_spins),
                    str(num_spins), str(mcs), str(init_temp), str(final_temp), str(temp_step), str(T_1), '0', '1'])
    df["df_%i" % (num_spins)] = pd.read_csv("Textfiles/Output_%i.txt" % (num_spins), delim_whitespace=True,
                     names=["T_%i" % (num_spins), "E_%i" % (num_spins), "E_var_%i" % (num_spins),
                     "M_tot_%i" % (num_spins), "M_var_%i" % (num_spins), "M_abs_%i" % (num_spins)])  # Leser av tekstfilen.

    E["E_%i"%(num_spins)] = np.array(df["df_%i"%(num_spins)]["E_%i"%(num_spins)])
    M_abs["M_abs_%i"%(num_spins)] = np.array(df["df_%i"%(num_spins)]["M_abs_%i"%(num_spins)])
    E_var["E_var%i"%(num_spins)] = np.array(df["df_%i"%(num_spins)]["E_var_%i"%(num_spins)])
    T["T_%i"%(num_spins)] = np.array(df["df_%i"%(num_spins)]["T_%i"%(num_spins)])
    C_num["C_num_%i"%(num_spins)] =  E_var["E_var%i"%(num_spins)]/num_spins**2

    M_var["M_var%i"%(num_spins)] = np.array(df["df_%i"%(num_spins)]["M_var_%i"%(num_spins)])
    Chi_num["Chi_num_%i"%(num_spins)] = M_var["M_var%i"%(num_spins)]/num_spins**2

    #plt.plot(df["df_%i"%(num_spins)]["T_%i"%(num_spins)], C_num["C_num_%i"%(num_spins)]/num_spins/num_spins/mcs)
    plot(T["T_%i"%(num_spins)], E["E_%i"%(num_spins)], M_abs["M_abs_%i"%(num_spins)], C_num["C_num_%i"%(num_spins)],
        Chi_num["Chi_num_%i"%(num_spins)], num_spins)
# Skriver om til dataframe:
#handles, labels = ax.get_legend_handles_labels()
#fig.legend(handles, labels, loc='upper center')
plt.legend()
plt.suptitle('MCC = %i, $\Delta T = 0.05$'%(mcs))
fig.tight_layout()
plt.savefig('Exp_values.png', dpi=200)
plt.show()
