import subprocess
import matplotlib.pyplot as plt
ns = [10, 25, 50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300]
iterations = []
CPU_time = []
for n in ns:
    subprocess.run(['./Tridiag.x', str(n)])
    infile = open("Output","r")
    for line in infile:
        p = line.split()
        iterations.append(float(p[0]))
        CPU_time.append(float(p[1]))

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
