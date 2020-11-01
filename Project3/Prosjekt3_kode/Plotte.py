import numpy as np
import matplotlib.pyplot as plt
import subprocess

beta = [3,3.5,3.99]
beta_name = [2,2.5,2.99]

subprocess.run(['./1.x', str(beta[0])])
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

plt.title('Euler method')
plt.plot(xEU[1:], yEU[1:], label=f'N={len(lines)}')
plt.axis('equal')
plt.tight_layout()
plt.legend()
plt.show()

fig, axs = plt.subplots(1, 3, sharex=True, sharey=True)
for n in range(len(beta)):
    subprocess.run(['./1.x', str(beta[n])])
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

    fig.suptitle(f'Verlet method with N={len(lines)}')
    axs[n].title.set_text(f'beta={str(beta_name[n])}')
    axs[n].plot(xVV[1:], yVV[1:],label=f'N={len(lines)}')
    axs[n].set_xlabel('x (AU)')
    axs[n].set_ylabel('y (AU)')

plt.show()
