import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import subprocess

#step_factor = [0.01,0.05] #[Alfa mindre enn 0.5, Alfa storre enn 0.5]
n_dx = [10,100]
index1 = [6,600] # Indeks som gir kurvet linje.
L=1
N=1000

def func(step_fac, n_dx, index1):
    subprocess.run(['./run2.x', str(n_dx), str(step_fac)])
    df = pd.read_csv("forward_output.txt", delim_whitespace=True, index_col=None)
    df2 = pd.read_csv("Backward_output.txt", delim_whitespace=True, index_col=None)
    df3 = pd.read_csv("crank_nicholson.txt", delim_whitespace=True, index_col=None)
    val1 = df.values
    val2 = df2.values
    val3 = df3.values

    dx = L/(n_dx+1)
    alfa = (step_fac/(n_dx*n_dx))/(dx**2) # Regner ut alfa.

    # Setter opp for plotting:
    fig, axs = plt.subplots(1,3)
    fig.suptitle("Alpha = %.4f and dx=1/%.0f"%(alfa, n_dx))
    fig.tight_layout()
    axs[0].set_title("Forward euler")
    axs[1].set_title("Backward euler")
    axs[2].set_title("Crank nicholson")

    l = len(val1[0])-1 # Trekker fra det som tilsvarer tidssteget i lengde.
    x = np.linspace(0,L,l)
    index2 = len(val1) - index1  # 1000 Indeks som gir liner kurve.

    t = [val1[index1][0], val1[index2][0]] # [Tidspunkt for kurvet linje, for liner]
    for q in range(len(t)):
        ledd = 0
        for n in range(1,N):
            ledd += 2*(np.pi*n*np.cos(np.pi*n)-np.sin(np.pi*n)) / (np.pi**2 * n**2)\
            * np.sin(n*np.pi*x/L) * np.exp(-n**2 * np.pi**2 * t[q] / L)
        u = x/L + ledd

        if q==0:
            axs[0].plot(x[1:], u[1:]-val1[index1][2:], label='t1=%.2fs' % (t[0]))
            axs[1].plot(x[1:], u[1:]-val2[index1][2:])
            axs[2].plot(x[1:], u[1:]-val3[index1][2:])
        else:
            axs[0].plot(x[1:], u[1:]-val1[index2][2:], label='t2=%.2fs' % (t[1]))
            axs[1].plot(x[1:], u[1:]-val2[index2][2:])
            axs[2].plot(x[1:], u[1:]-val3[index2][2:])
    axs[0].legend()


func(0.01, n_dx[0], index1[0]) # 1/10
plt.show()
'''
func(step_factor[0], n_dx[1], index1[1]) # 1/100
plt.show()
func(step_factor[1], n_dx[0], index1[0])
plt.show()
func(step_factor[1], n_dx[1], index1[1])
plt.show()
'''
