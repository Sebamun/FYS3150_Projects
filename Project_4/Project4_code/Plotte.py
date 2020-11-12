import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Skriver om til dataframe:
df = pd.read_csv("Output.txt", delim_whitespace=True, \
index_col=False, names=["T","E_tot","E_var","M_tot","M_var","M_abs"]) # Leser av tekstfilen.
plt.plot(df['T'], df['M_abs'])
plt.show()
