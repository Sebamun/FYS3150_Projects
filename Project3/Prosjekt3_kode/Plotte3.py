import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
Nobjects = 9 # Antall planeter vi plotter for.
# Skriver om til dataframe:
df = pd.read_csv("Textfiles/PlanetsVV_9.txt", delim_whitespace=True, \
index_col=False, names=["t","n","m","x","y","z","vx","vy","vz"]) # Leser av tekstfilen.
planet_dfs = [] # legger verdiene til denne.
for guy in df.groupby("n"): # Her grupperer vi etter hvilke objekt vi ser på n.
    planet_dfs.append(guy)
name = ['Neptune', 'Uranus', 'Saturn', 'Jupiter', \
'Mars', 'Earth', 'Venus', 'Mercury', 'Sun'] # Navn på objektene.
# PLotting:
for i in range(Nobjects):
    object = planet_dfs[i][1]
    plt.plot(object['x'], object['y'], label=f'{name[i]}')
plt.title('The solarsystem')
plt.xlabel('x (AU)')
plt.ylabel('y (AU)')
plt.legend()
plt.show()
