import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import pandas as pd

df = pd.read_csv("Output/2d_output.txt", delim_whitespace=True, index_col=None)

vals = np.array(df.values)
dim = np.int(np.sqrt(len(vals[100][1:])))
T_0 = np.reshape(vals[0][1:], [dim, dim])
T_1 = np.reshape(vals[100][1:], [dim, dim])
T_2 = np.reshape(vals[4000][1:], [dim, dim])
x = np.linspace(0, 10, dim)
y = np.linspace(0, 10, dim)

xx, yy = np.meshgrid(x, y)


fig0, ax0 = plt.subplots()
cs = ax0.contourf(xx, yy, T_0, vmin=0, vmax=1,
                 cmap=plt.get_cmap('coolwarm'))
cbar = fig0.colorbar(cs)
ax0.set_title("t=1e-5")
plt.savefig("Output/contour_0.png", dpi=200)
plt.show()
fig1, ax1 = plt.subplots()
cs = ax1.contourf(xx, yy, T_1, vmin=0, vmax=1, 
                 cmap=plt.get_cmap('coolwarm'))
cbar = fig1.colorbar(cs)
ax1.set_title("t=0.01")
plt.savefig("Output/contour_1.png", dpi=200)
plt.show()
fig2, ax2 = plt.subplots()
cs = ax2.contourf(xx, yy, T_2, vmin=0, vmax=1,
                 cmap=plt.get_cmap('coolwarm'))
cbar = fig2.colorbar(cs)
ax2.set_title("t=0.4")
plt.savefig("Output/contour_2.png", dpi=200)
plt.show()
'''
fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(xx, yy, T_0, rstride=5, cstride=5, cmap=plt.get_cmap('coolwarm'),
                       linewidth=0, antialiased=False, shade=False)
ax.set_xlabel("x", fontsize=10)
ax.set_ylabel("y", fontsize=10)
ax.set_zlabel("T", fontsize=10)
plt.clim(0, 1)
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()

fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(xx, yy, T_1, rstride=5, cstride=5, cmap=plt.get_cmap('coolwarm'),
                       linewidth=0, antialiased=False, shade=False)
ax.set_xlabel("x", fontsize=10)
ax.set_ylabel("y", fontsize=10)
ax.set_zlabel("T", fontsize=10)
plt.clim(0, 1)
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()

fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(xx, yy, T_2, rstride=5, cstride=5, cmap=plt.get_cmap('coolwarm'),
                       linewidth=0, antialiased=False, shade=False)
ax.set_xlabel("x", fontsize=10)
ax.set_ylabel("y", fontsize=10)
ax.set_zlabel("T", fontsize=10)
plt.clim(0, 1)
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()
'''
