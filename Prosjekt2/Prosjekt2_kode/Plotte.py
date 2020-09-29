import numpy as np
import matplotlib.pyplot as plt
infile = open('Egenvektorer', 'r')
lines = infile.readlines()
eig_vec = np.zeros(len(lines)-1)
for i in range(len(lines)-1):
    eig_vec[i] = float(lines[i])
rho = np.linspace(0,1, len(eig_vec))
plt.plot(rho, eig_vec)
plt.show()
