import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

Nobjects = 1

df1 = pd.read_csv("Textfiles/Escape/PlanetsVV_2_sqrt2.txt", delim_whitespace=True, index_col=False, names=["t","n","m","x","y","z","vx","vy","vz"])
planet_dfs1 = []

df2 = pd.read_csv("Textfiles/Escape/PlanetsVV_2_sqrt4.txt", delim_whitespace=True, index_col=False, names=["t","n","m","x","y","z","vx","vy","vz"])
planet_dfs2 = []

df3 = pd.read_csv("Textfiles/Escape/PlanetsVV_2_sqrt7.txt", delim_whitespace=True, index_col=False, names=["t","n","m","x","y","z","vx","vy","vz"])
planet_dfs3 = []

df4 = pd.read_csv("Textfiles/Escape/PlanetsVV_2_sqrt8.txt", delim_whitespace=True, index_col=False, names=["t","n","m","x","y","z","vx","vy","vz"])
planet_dfs4 = []

for guy in df1.groupby("n"):
    planet_dfs1.append(guy)

for guy in df2.groupby("n"):
    planet_dfs2.append(guy)

for guy in df3.groupby("n"):
    planet_dfs3.append(guy)

for guy in df4.groupby("n"):
    planet_dfs4.append(guy)

name = ['Earth', 'Sola','f','g','h']

for i in range(Nobjects):
    object1 = planet_dfs1[i][1]
    object2 = planet_dfs2[i][1]
    object3 = planet_dfs3[i][1]
    object4 = planet_dfs4[i][1]

    plt.plot(object1['x'], object1['y'], label='$v_0=\sqrt{2}\pi $ [AU/yr]')
    plt.plot(object2['x'], object2['y'], label='$v_0=2\pi $ [AU/yr]')
    plt.plot(object3['x'], object3['y'], label='$v_0=\sqrt{7}\pi $ [AU/yr]')
    plt.plot(object4['x'], object4['y'], label='$ v_0=2\sqrt{2}\pi  $ [AU/yr]')
plt.plot(0,0, 'o',label='Sun', c='k')
plt.xlabel('x[AU]')
plt.ylabel('y[AU]')
plt.legend()
plt.xlim(-19,4)
plt.ylim(-4,12)
plt.title('Escape velocity for Earth')
plt.show()
