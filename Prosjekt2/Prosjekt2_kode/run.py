import subprocess
import matplotlib.pyplot as plt
import numpy as np
import sys
ns = [10, 25, 50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300]
iterations = []
CPU_time = []
switch = sys.argv[1]
for n in ns:
    subprocess.run(['./Tridiag.x', str(n), str(switch)])
    infile = open("Output","r")
    for line in infile:
        p = line.split()
        iterations.append(float(p[0]))
        CPU_time.append(float(p[1]))

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

#Plotting:
plt.title('Number of iterations')
plt.plot(ns, iterations,'bo')
plt.xlabel('Dimension')
plt.ylabel('Iterations')
plt.show()
plt.title('The CPU time')
plt.plot(ns, CPU_time,'bo')
plt.xlabel('Dimension')
plt.ylabel('CPU time')
plt.show()
