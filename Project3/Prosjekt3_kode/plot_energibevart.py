import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

Nobjects = 2

df = pd.read_csv("Textfiles/PlanetsVV_energy_2.txt", delim_whitespace=True, index_col=False, names=["t","n","Ek","Ep"])
planet_dfs = []

for j in df.groupby("n"):
    planet_dfs.append(j)

name = ["Earth", "Sun"]


for i in range(Nobjects):
    object = planet_dfs[i][1]
    plt.plot(object['t'], object['Ek'], label=f'{name[i]}"Ek"')
    plt.plot(object['t'], object['Ep'], label=f'{name[i]}"Ep"')
    plt.plot(object['t'], object['Ep']+object['Ek'], label=f'{name[i]}"Tot"')
plt.legend()
plt.show()
