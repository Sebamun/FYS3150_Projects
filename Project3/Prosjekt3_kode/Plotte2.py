import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

Nobjects = 9

df = pd.read_csv("PlanetsVV_9.txt", delim_whitespace=True, index_col=False, names=["t","n","m","x","y","z","vx","vy","vz"])
planet_dfs = []

for guy in df.groupby("n"):
    planet_dfs.append(guy)

#sun = planet_dfs[0][1]
#plt.plot(mercury['x'], mercury['y'])

name = ['Neptun', 'Uranus', 'Saturn', 'Jupiter', 'Mars', 'Jorden', 'Venus', 'Merkur', 'Sola']

for i in range(Nobjects):
    object = planet_dfs[i][1]
    plt.plot(object['x'], object['y'], label=f'{name[i]}')
plt.legend()
plt.show()


#sun = planet_dfs[0][1]
#mercury = planet_dfs[1][1]
#jupiter = planet_dfs[5][1]

#plt.plot(sun.x, sun.y)
#for i in range():
