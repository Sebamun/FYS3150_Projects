import numpy as np
import matplotlib.pyplot as plt

N = 1000
l = 10000
L = 1
x = np.linspace(0,L,l)
t = 0.001
ledd = 0

for n in range(1,N):
    ledd += 2*(np.pi*n*np.cos(np.pi*n)-np.sin(np.pi*n)) / (np.pi**2 * n**2)\
    * np.sin(n*np.pi*x/L) * np.exp(-n**2 * np.pi**2 * t / L)
    print(ledd)

u = x/L + ledd

plt.plot(x, u)
plt.show()

'''
for n in range(N):
    ledd += (2*(np.pi*n*np.cos(np.pi*n)-np.sin(np.pi*n))/np.pi**2 * n**2)\
    *np.sin(n*np.pi*x/L)*np.exp(-n**2 * np.pi**2 * t / L)
    '''









import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import subprocess

#b
N = 100
l = 10000
L = 1
x = np.linspace(0,L,l)
t = [0.001,0.999]
ledd = 0
'''
for n in range(1,N):
    ledd += 2*(np.pi*n*np.cos(np.pi*n)-np.sin(np.pi*n)) / (np.pi**2 * n**2)\
    * np.sin(n*np.pi*x/L) * np.exp(-n**2 * np.pi**2 * t / L)
    print(ledd)

u = x/L + ledd
'''
#b


n_dx = [10,100]

fig, axs = plt.subplots(1, 3)
fig, axs2 = plt.subplots(1, 2)
for i in range(len(n_dx)):
    subprocess.run(['./run.x', str(n_dx[i])])
    df = pd.read_csv("forward_output.txt", delim_whitespace=True, index_col=None)
    df2 = pd.read_csv("Backward_output.txt", delim_whitespace=True, index_col=None)
    df3 = pd.read_csv("crank_nicholson.txt", delim_whitespace=True, index_col=None)
    val1 = df.values
    val2 = df2.values
    val3 = df3.values

    l = len(val1[0])-1 # Trekker fra det som tilsvarer tidssteget i lengde.
    x = np.linspace(0,L,l)
    index1 = 100 # Indeks som gir kurvet linje.
    index2 = len(val1) - 1000  # Indeks som gir liner kurve.

    # Regner ut error:
    ledd = 0
    t1 = val1[index1][0] # Tidspunkt for kurvet linje.
    t2 = val1[index2][0] # Tidspunkt
    print(t1)
    print(t2)
    for n in range(1,n_dx[i]):
        ledd += 2*(np.pi*n*np.cos(np.pi*n)-np.sin(np.pi*n)) / (np.pi**2 * n**2)\
        * np.sin(n*np.pi*x/L) * np.exp(-n**2 * np.pi**2 * t1 / L)
    u = x/L + ledd
    axs2[i].plot(x, u)

    #print((np.mean(np.abs((u[1:] - val1[100][2:])) / u[1:])) * 100)


    # Plotting:
    axs[0].set_title("Forward euler")
    axs[0].plot(x, val1[index1][1:], label= 'dx=1/%.0f and t_1=%.3f s' %(n_dx[i], t1)) # Sette inn eksplisitt verdi for t?
    axs[0].plot(x, val1[index2][1:], label= 'dx=1/%.0f and t_2=%.3f s' %(n_dx[i], t2))
    axs[1].set_title("Backward euler")
    axs[1].plot(x, val2[index1][1:])
    axs[1].plot(x, val2[index2][1:])
    axs[2].set_title("Crank nicholson")
    axs[2].plot(x, val3[index1][1:])
    axs[2].plot(x, val3[index2][1:])



axs[0].legend()
fig.tight_layout()
plt.savefig("Sub c.png", dpi=95)
plt.show()













import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import subprocess

n = [10,100]
L = 1
fig, axs = plt.subplots(1, 3)
for i in range(len(n)):
    subprocess.run(['./run.x', str(n[i])])
    df = pd.read_csv("forward_output.txt", delim_whitespace=True, index_col=None)
    df2 = pd.read_csv("Backward_output.txt", delim_whitespace=True, index_col=None)
    df3 = pd.read_csv("crank_nicholson.txt", delim_whitespace=True, index_col=None)
    val1 = df.values
    val2 = df2.values
    val3 = df3.values

    l = len(val1[0])-1 # Trekker fra det som tilsvarer tidssteget i lengde.

    x = np.linspace(0,L,l)

    index = len(val1) - 100  # Indeks som gir liner kurve.
    # Plotting:
    axs[0].set_title("Forward euler")
    axs[0].plot(x, val1[100][1:], label= 'dx=1/%.0f and t_2=%.3f s' %(n[i], val1[100][0])) # Sette inn eksplisitt verdi for t?
    axs[0].plot(x, val1[index][1:], label= 'dx=1/%.0f and t_2=%.3f s' %(n[i], val1[index][0]))
    axs[1].set_title("Backward euler")
    axs[1].plot(x, val2[100][1:])
    axs[1].plot(x, val2[index][1:])
    axs[2].set_title("Crank nicholson")
    axs[2].plot(x, val3[100][1:])
    axs[2].plot(x, val3[index][1:])
axs[0].legend()
fig.tight_layout()
plt.savefig("c.png", dpi=95)
plt.show()
