import numpy as np
import matplotlib.pyplot as plt
infile = open('Egenvektorer', 'r')
lines = infile.readlines()
eig_vec = np.zeros(len(lines)-1)
for i in range(len(lines)-1):
    eig_vec[i] = float(lines[i])
rho = np.linspace(0,1, len(eig_vec))
#u = np.zeros(len(eig_vec))
n = np.arange(0,len(eig_vec))
u = np.sin(n*np.pi/len(eig_vec))
# Plotting:
plt.plot(rho, eig_vec, label='Num')
plt.plot(rho, u/np.linalg.norm(u), label='teor')
plt.legend()
plt.show()
