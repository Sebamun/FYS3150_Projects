import numpy as np
import matplotlib.pyplot as plt
import subprocess
import pandas as pd

beta = 3
beta_name = 2
N = 100000

fig, axs = plt.subplots()
subprocess.run(['./1.x', str(beta), str(N)])
infileVV = open('Textfiles/PlanetsVV_2.txt', 'r')

lines = infileVV.readlines()
xVV = np.zeros(len(lines))
yVV = np.zeros(len(lines))
zVV = np.zeros(len(lines))
vxVV = np.zeros(len(lines))
vyVV = np.zeros(len(lines))
vzVV = np.zeros(len(lines))
r = np.zeros([len(lines), 3])
v = np.zeros([len(lines), 3])
t = np.zeros(len(lines))
for i in range(1,len(lines)):
    vals = lines[i].split()
    xVV[i] = float(vals[3])
    yVV[i] = float(vals[4])
    zVV[i] = float(vals[5])
    vxVV[i] = float(vals[6])
    vyVV[i] = float(vals[7])
    vzVV[i] = float(vals[8])
    t[i] = float(vals[0])
    r[i] = np.array([xVV[i], yVV[i], zVV[i]])
    v[i] = np.array([vxVV[i], vyVV[i],vzVV[i]])

L = np.cross(r,v)

#plt.plot(t[1:],vyVV[1:],label='l')
plt.plot(t[1:],L[1:,2:])
plt.title('Angular momentum for Earth-Sun system')
#plt.legend()
plt.xlabel('Time [yr]')
plt.ylabel('Angular momentum [$M_\odot AU^2 / yr$]')
plt.show()

# Her kjorer vi for å finne energi:
Nobjects = 1
df = pd.read_csv("Textfiles/PlanetsVV_energy_2.txt", delim_whitespace=True, index_col=False, names=["t","n","Ek","Ep"])
planet_dfs = []

for j in df.groupby("n"):
    planet_dfs.append(j)

for i in range(Nobjects):
    object = planet_dfs[i][1]
    plt.plot(object['t'], object['Ek'], label='Kinetic energy')
    plt.plot(object['t'], object['Ep'], label='Potential energy')
    plt.plot(object['t'], object['Ep']+object['Ek'], label='Total energy')
plt.legend()
plt.xlabel('Time [yrs]')
plt.ylabel('Energy [$M_\odot AU^2 / yr^2$]')
plt.title('Energy in Earth-Sun system')
plt.show()
