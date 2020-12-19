import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import subprocess

N = 1000
l = 10000
L = 1

n_dx = [10,100]
index1 = [6,600] # Indeks som gir kurvet linje.

fig, axs = plt.subplots(1, 3)
fig2, axs2 = plt.subplots(1, 2)
for i in range(len(n_dx)):
    subprocess.run(['./run_c.x', str(n_dx[i])])
    df = pd.read_csv("forward_output.txt", delim_whitespace=True, index_col=None)
    df2 = pd.read_csv("Backward_output.txt", delim_whitespace=True, index_col=None)
    df3 = pd.read_csv("crank_nicholson.txt", delim_whitespace=True, index_col=None)
    val1 = df.values
    val2 = df2.values
    val3 = df3.values
    l = len(val1[0])-1 # Trekker fra det som tilsvarer tidssteget i lengde.
    x = np.linspace(0,L,l)
    index2 = len(val1) - index1[i]  # 1000 Indeks som gir liner kurve.

    # Regner ut error:
    t = [val1[index1[i]][0], val1[index2][0]] # [Tidspunkt for kurvet linje, for liner]
    for q in range(len(t)):
        ledd = 0
        for n in range(1,N):
            ledd += 2*(np.pi*n*np.cos(np.pi*n)-np.sin(np.pi*n)) / (np.pi**2 * n**2)\
            * np.sin(n*np.pi*x/L) * np.exp(-n**2 * np.pi**2 * t[q] / L)
        u = x/L + ledd
        # Plotting:
        axs2[i].set_title('For dx=1/%.0f' %(n_dx[i]))
        axs2[i].plot(x, u, label='t=%.2f' %(t[q])) # Plotter analytisk resultat.

        if q==0:
            print('For dx=1/%.0f and t_1=%.2f:' %(n_dx[i], t[q]))
            print(np.sqrt((1/len(u[1:]))*np.sum(u[1:]-val1[index1[i]][2:])**2/(np.sum(u[1:]**2))))
            print(np.sqrt((1/len(u[1:]))*np.sum(u[1:]-val2[index1[i]][2:])**2/(np.sum(u[1:]**2))))
            print(np.sqrt((1/len(u[1:]))*np.sum(u[1:]-val3[index1[i]][2:])**2/(np.sum(u[1:]**2))))
            print('----------------------')

        else:
            print('For dx=1/%.0f and t_2=%.2f:' %(n_dx[i], t[q]))
            print(np.sqrt(np.sum(u[1:]-val1[index2][2:])**2)/(np.sqrt(np.sum(u[1:]**2))))
            print(np.sqrt(np.sum(u[1:]-val2[index2][2:])**2)/(np.sqrt(np.sum(u[1:]**2))))
            print(np.sqrt(np.sum(u[1:]-val3[index2][2:])**2)/(np.sqrt(np.sum(u[1:]**2))))
            print('----------------------')

    # Plotting:
    if i==0:
        axs[0].plot(x, val1[index1[i]][1:],'--', label= 'dx=1/%.0f and t_1=%.2f s' %(n_dx[i], t[0]))
        axs[0].plot(x, val1[index2][1:],'--', label= 'dx=1/%.0f and t_2=%.2f s' %(n_dx[i], t[1]))
        axs[1].plot(x, val2[index1[i]][1:],'--')
        axs[1].plot(x, val2[index2][1:],'--')
        axs[2].plot(x, val3[index1[i]][1:],'--')
        axs[2].plot(x, val3[index2][1:],'--')
    else:
        axs[0].plot(x, val1[index1[i]][1:], label= 'dx=1/%.0f and t_1=%.2f s' %(n_dx[i], t[0]))
        axs[0].plot(x, val1[index2][1:], label= 'dx=1/%.0f and t_2=%.2f s' %(n_dx[i], t[1]))
        axs[1].plot(x, val2[index1[i]][1:])
        axs[1].plot(x, val2[index2][1:])
        axs[2].plot(x, val3[index1[i]][1:])
        axs[2].plot(x, val3[index2][1:])

fig.suptitle('Numerical solutions')
fig2.suptitle('Analytical solution')
axs[0].set_title("Forward euler")
axs[0].set_xlabel("x")
axs[0].set_ylabel("u")
axs2[0].set_xlabel("x")
axs2[0].set_ylabel("u")
axs[1].set_title("Backward euler")
axs[2].set_title("Crank nicholson")
axs[0].legend()
axs2[0].legend()
#fig.tight_layout()
fig.savefig("c.png", dpi=95)
fig2.savefig("b.png", dpi=95)
plt.show()
