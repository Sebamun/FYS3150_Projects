import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import subprocess

step_factor = [0.001,0.005] #[Alfa mindre enn 0.5, Alfa storre enn 0.5]
n_dx = [10,100]
index1 = [6,600] # Indeks som gir kurvet linje.
L=1
N=1000

def func(step_fac, n_dx, index1):
    fig, axs = plt.subplots(1,2)
    subprocess.run(['./run2.x', str(n_dx), str(step_factor)])
    df = pd.read_csv("forward_output.txt", delim_whitespace=True, index_col=None)
    df2 = pd.read_csv("Backward_output.txt", delim_whitespace=True, index_col=None)
    df3 = pd.read_csv("crank_nicholson.txt", delim_whitespace=True, index_col=None)
    val1 = df.values
    val2 = df2.values
    val3 = df3.values

    l = len(val1[0])-1 # Trekker fra det som tilsvarer tidssteget i lengde.
    x = np.linspace(0,L,l)
    index2 = len(val1) - index1  # 1000 Indeks som gir liner kurve.

    t = [val1[index1][0], val1[index2][0]] # [Tidspunkt for kurvet linje, for liner]
    print(val1)
    for q in range(len(t)):
        ledd = 0
        for n in range(1,N):
            ledd += 2*(np.pi*n*np.cos(np.pi*n)-np.sin(np.pi*n)) / (np.pi**2 * n**2)\
            * np.sin(n*np.pi*x/L) * np.exp(-n**2 * np.pi**2 * t[q] / L)
        u = x/L + ledd
        print(u[1:]-val1[index1][2:])
        print(u[1:]-val1[index2][2:])
        #axs[q].plot(x[1:], u[1:]-val1[index1][2:], label='t1')
        #axs[q].plot(x[1:], u[1:]-val1[index2][2:], label='t2')
    #plt.legend()
    #plt.show()


func(step_factor[0], n_dx[0], index1[0])
#func(step_factor[0], n_dx[1], index1[1])
#func(step_factor[1], n_dx[0], index1[0])
#func(step_factor[1], n_dx[1], index1[1])
