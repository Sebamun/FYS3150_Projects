import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import pandas as pd
import subprocess

step_factor = [0.01, 0.5]  # [gir alfa mindre enn 0.5, gir alfa storre enn 0.5]
n_dx = [10, 100]
index1_a = [6, 600]  # Indeks som gir kurvet linje.
index1_b = [0, 0]  # Indeks som gir kurvet linje.
L = 1
N = 1000


def func_boundary_held(step_fac, n_dx, index1):
    subprocess.run(['./run_d.x', str(n_dx), str(step_fac)])
    df = pd.read_csv("Output/Output/forward_output.txt",
                     delim_whitespace=True, index_col=None)
    df2 = pd.read_csv("Output/Output/Backward_output.txt",
                      delim_whitespace=True, index_col=None)
    df3 = pd.read_csv("Output/Output/crank_nicholson.txt",
                      delim_whitespace=True, index_col=None)
    val1 = df.values
    val2 = df2.values
    val3 = df3.values

    dx = L/(n_dx+1)
    dt = step_fac/(n_dx*n_dx)
    alfa = dt/(dx**2)  # Regner ut alfa.

    # Setter opp for plotting:
    fig, axs = plt.subplots(1, 3)
    fig.suptitle("Alpha = %.4f, dx=1/%.0f and dt = %.6f" % (alfa, n_dx, dt))
    fig.tight_layout(rect=[1, 0.03, 1, 0.95])
    axs[0].set_title("Forward euler")
    axs[1].set_title("Backward euler")
    axs[2].set_title("Crank nicholson")
    axs[0].set_xlabel('x')
    axs[0].set_ylabel('Deviation in u')

    l = len(val2[0])-1  # Trekker fra det som tilsvarer tidssteget i lengde.
    x = np.linspace(0, L, l)
    index2 = len(val2) - index1  # 1000 Indeks som gir liner kurve.

    # [Tidspunkt for kurvet linje, for liner]
    t = [val2[index1][0], val2[index2][0]]

    for q in range(len(t)):
        ledd = 0
        for n in range(1, N):
            ledd += 2*(np.pi*n*np.cos(np.pi*n)-np.sin(np.pi*n)) / (np.pi**2 * n**2)\
                * np.sin(n*np.pi*x/L) * np.exp(-n**2 * np.pi**2 * t[q] / L)
        u = x/L + ledd

        if q == 0:
            axs[0].plot(x[1:], u[1:]-val1[index1][2:])
            axs[1].plot(x[1:], u[1:]-val2[index1][2:],
                        label='$t_{curve}$=%.2fs' % (t[0]))
            axs[2].plot(x[1:], u[1:]-val3[index1][2:])
        else:
            axs[0].plot(x[1:], u[1:]-val1[index2][2:])
            axs[1].plot(x[1:], u[1:]-val2[index2][2:],
                        label='$t_{linear}$=%.2fs' % (t[1]))
            axs[2].plot(x[1:], u[1:]-val3[index2][2:])
    axs[1].legend()


def func_boundary_not_held(step_fac, n_dx, index1, stability_constant):
    subprocess.run(['./run_d.x', str(n_dx), str(step_fac)])
    df = pd.read_csv("Output/forward_output.txt",
                     delim_whitespace=True, index_col=None)
    df2 = pd.read_csv("Output/Backward_output.txt",
                      delim_whitespace=True, index_col=None)
    df3 = pd.read_csv("Output/crank_nicholson.txt",
                      delim_whitespace=True, index_col=None)
    val1 = df.values
    val2 = df2.values
    val3 = df3.values

    dx = L/(n_dx+1)
    dt = step_fac/(n_dx*n_dx)
    alfa = dt/(dx**2)  # Regner ut alfa.

    # Setter opp for plotting:
    fig, axs = plt.subplots(1, 3)
    fig.suptitle("Alpha = %.4f, dx=1/%.0f and dt = %.4f" % (alfa, n_dx, dt))
    fig.tight_layout(rect=[1, 0.03, 1, 0.95])
    axs[1].ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
    axs[2].ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
    axs[0].set_title("Forward euler")
    axs[1].set_title("Backward euler")
    axs[2].set_title("Crank nicholson")
    axs[0].set_xlabel('x')
    axs[0].set_ylabel('Deviation in u')

    l = len(val2[0])-1  # Trekker fra det som tilsvarer tidssteget i lengde.
    x = np.linspace(0, L, l)  # Posisjonen i x-retning.
    # Denne konstanten matte jeg bare proove meg fram for aa finne riktig index for de ulike dxene.
    index2 = index1 + stability_constant

    # [Tidspunkt for kurvet linje, for liner]
    t = [val2[index1][0], val2[index2][0]]
    for q in range(len(t)):
        ledd = 0
        for n in range(1, N):
            ledd += 2*(np.pi*n*np.cos(np.pi*n)-np.sin(np.pi*n)) / (np.pi**2 * n**2)\
                * np.sin(n*np.pi*x/L) * np.exp(-n**2 * np.pi**2 * t[q] / L)
        u = x/L + ledd

        if q == 0:
            axs[0].plot(x[1:], u[1:]-val1[index1][2:])
            axs[1].plot(x[1:], u[1:]-val2[index1][2:],
                        label='t_curve=%.2fs' % (t[0]))
            axs[2].plot(x[1:], u[1:]-val3[index1][2:])
        else:
            axs[0].plot(x[1:], u[1:]-val1[index2][2:])
            axs[1].plot(x[1:], u[1:]-val2[index2][2:],
                        label='t_linear=%.2fs' % (t[1]))
            axs[2].plot(x[1:], u[1:]-val3[index2][2:])
    axs[1].legend()


func_boundary_held(step_factor[0], n_dx[0], index1_a[0])  # 1/10
plt.show()

func_boundary_held(step_factor[0], n_dx[1], index1_a[1])  # 1/100
plt.show()

func_boundary_not_held(step_factor[1], n_dx[0], index1_b[0], 1)
plt.show()

func_boundary_not_held(step_factor[1], n_dx[1], index1_b[1], 140)
plt.show()
