import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import subprocess

mass_adjust = [1,10,100] # The mass adjustments for Jupiter
fig, axs = plt.subplots(1, 3, sharex=True, sharey=True) # Set figure.
fig.suptitle('Three body problem with different Jupiter masses')
for n in range(len(mass_adjust)):
    subprocess.run(['./2.x', str(mass_adjust[n])])
    Nobjects = 3 # Antall planeter vi plotter for.
    # Skriver om til dataframe:
    df = pd.read_csv("Textfiles/PlanetsVV_3.txt", delim_whitespace=True, \
    index_col=False, names=["t","n","m","x","y","z","vx","vy","vz"]) # Leser av tekstfilen.
    planet_dfs = [] # legger verdiene til denne.
    for guy in df.groupby("n"): # Her grupperer vi etter hvilke objekt vi ser på n.
        planet_dfs.append(guy)
    name = ['Jupiter', 'Earth', 'Sun'] # Navn på objektene.
    # PLotting:
    for i in range(Nobjects):
        object = planet_dfs[i][1]
        axs[n].plot(object['x'], object['y'], label=f'{name[i]}')
    axs[n].set_xlabel('x (AU)')
    axs[n].set_ylabel('y (AU)')
    axs[n].title.set_text(f'Jupiter mass ={str(mass_adjust[n])}')
plt.legend()
plt.show()
