import numpy as np
import matplotlib.pyplot as plt
import subprocess

N = [1000,5000,10000]

fig, axs = plt.subplots(3, 2, sharex=True, sharey=True)
fig.suptitle('Euler vs Verlet')

for n in range(len(N)):
    subprocess.run(['./1.x', str(3), str(N[n])])
    infileEU = open('Textfiles/PlanetsEU_2.txt', 'r')
    lines = infileEU.readlines()
    xEU = np.zeros(len(lines))
    yEU = np.zeros(len(lines))
    zEU = np.zeros(len(lines))
    x1EU = np.zeros(len(lines))
    y1EU = np.zeros(len(lines))
    z1EU = np.zeros(len(lines))
    for i in range(1,len(lines)):
        vals = lines[i].split()
        xEU[i] = float(vals[3])
        yEU[i] = float(vals[4])
        zEU[i] = float(vals[5])
        x1EU[i] = float(vals[6])
        y1EU[i] = float(vals[7])
        z1EU[i] = float(vals[8])
    axs[n][0].title.set_text(f'N={N[n]}')
    axs[n][0].plot(xEU[1:], yEU[1:],label=f'N={len(lines)}')
    axs[2][0].set_xlabel('x (AU)')
    axs[n][0].set_ylabel('y (AU)')

    infileVV = open('Textfiles/PlanetsVV_2.txt', 'r')
    lines = infileVV.readlines()
    xVV = np.zeros(len(lines))
    yVV = np.zeros(len(lines))
    zVV = np.zeros(len(lines))
    x1VV = np.zeros(len(lines))
    y1VV = np.zeros(len(lines))
    z1VV = np.zeros(len(lines))
    for i in range(1,len(lines)):
        vals = lines[i].split()
        xVV[i] = float(vals[3])
        yVV[i] = float(vals[4])
        zVV[i] = float(vals[5])
        x1VV[i] = float(vals[6])
        y1VV[i] = float(vals[7])
        z1VV[i] = float(vals[8])
    axs[n][1].title.set_text(f'N={N[n]}')
    axs[n][1].plot(xVV[1:], yVV[1:],label=f'N={len(lines)}')
    axs[2][1].set_xlabel('x (AU)')
    axs[n][1].set_ylabel('y (AU)')

plt.show()
