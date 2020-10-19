import numpy as np
import matplotlib.pyplot as plt
infile = open('PlanetsVV_2_0.005.txt', 'r')
lines = infile.readlines()
x = np.zeros(len(lines))
y = np.zeros(len(lines))
z = np.zeros(len(lines))
x1 = np.zeros(len(lines))
y1 = np.zeros(len(lines))
z1 = np.zeros(len(lines))
for i in range(1,len(lines)):
    vals = lines[i].split()
    x[i] = float(vals[3])
    y[i] = float(vals[4])
    z[i] = float(vals[5])
    x1[i] = float(vals[6])
    y1[i] = float(vals[7])
    z1[i] = float(vals[8])

#ax = plt.axes(projection='3d')
#ax.plot3D(x, y, z, 'gray')
#plt.show()

plt.plot(x[1:], y[1:])
#plt.plot(x1,y1)
plt.axis('equal')
plt.tight_layout()
plt.show()
