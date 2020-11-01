import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

Nobjects = 2

df = pd.read_csv("Textfiles/PlanetsVV_2.txt", delim_whitespace=True, index_col=False, names=["t","n","m","x","y","z","vx","vy","vz"])
planet_dfs = []

for guy in df.groupby("n"):
    planet_dfs.append(guy)

#ax = plt.axes(projection='3d')
for i in range(Nobjects):
    object = planet_dfs[i][1]

t = np.array(planet_dfs[0][1]['t'])
x = np.array(planet_dfs[0][1]['x'])
y = np.array(planet_dfs[0][1]['y'])
z = np.array(planet_dfs[0][1]['z'])
r = np.sqrt(x**2 + y**2 + z**2)
r_min = np.amin(r)
per_ind = np.where(r == r_min)[0]
theta_p = np.rad2deg(np.arctan2(y[per_ind[0]], 0.3075))*3600
print("The perihelion angle is ", theta_p)
