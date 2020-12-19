import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import pandas as pd 

df = pd.read_csv("Output/lithosphere_data.txt", delim_whitespace=True, index_col=None)
df_90 = pd.read_csv("Output/lithosphere_data.txt", delim_whitespace=True,
                  index_col=None, usecols=[90, 90])
df_50 = pd.read_csv("Output/lithosphere_data.txt", delim_whitespace=True,
                    index_col=None, usecols=[50, 50])
df_10 = pd.read_csv("Output/lithosphere_data.txt", delim_whitespace=True,
                    index_col=None, usecols=[10, 10])
df_30 = pd.read_csv("Output/lithosphere_data.txt", delim_whitespace=True,
                    index_col=None, usecols=[30, 30])
df_t = pd.read_csv("Output/lithosphere_data.txt", delim_whitespace=True,
                   index_col=None, usecols=[0, 0])
df_d = pd.read_csv("Output/lithosphere_data.txt", delim_whitespace=True,
                          index_col=None)

vals_d = np.array(df_d.values)
t = np.reshape(np.array(df_t.values), len(np.array(df_t.values)))
T = np.zeros([len(t), len(vals_d[0][1:])])
for i in range(0, len(t)):
    T[i] = vals_d[i][1:]


T_90 = np.reshape(np.array(df_90.values), len(np.array(df_90.values)))
T_10 = np.reshape(np.array(df_10.values), len(np.array(df_10.values)))
T_30 = np.reshape(np.array(df_30.values), len(np.array(df_30.values)))
T_50 = np.reshape(np.array(df_50.values), len(np.array(df_50.values)))
depth = np.linspace(0, 120, len(vals_d[0][1:]))
tt, dd = np.meshgrid(depth, t)


fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(tt, dd, T, rstride=5, cstride=5, cmap=plt.get_cmap('magma'),
                       linewidth=0, antialiased=False, shade=False)
ax.set_xlabel("Depth [km]", fontsize=10)
ax.set_ylabel("Time [Gy]", fontsize=10)
ax.set_zlabel("T [$\degree C$]", fontsize=10)
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()

plt.plot(t, T_90, label="z=90km")
plt.plot(t, T_10, label="z=10km")
plt.plot(t, T_30, label="z=30km")
plt.plot(t, T_50, label="z=50km")
plt.grid(True)
plt.xlabel("time [Gy)")
plt.ylabel("Temperature [$\degree C$]")
plt.legend()
plt.savefig("Output/T_90km_vs_t_V2.png", dpi=200)
plt.show()

t_0_index = 0  # Indeks som gir kurvet linje
t_stdystate_index = 1000
t_radi_index = 200
vals = df.values
#t = [vals[index1][0], vals[index2][0]]

T0 = np.array(vals[t_0_index][1:])

T1 = np.array(vals[t_stdystate_index][1:])

T2 = np.array(vals[2000][1:])

T3 = np.array(vals[5000][1:])

T4 = np.array(vals[7500][1:])

T5 = np.array(vals[9998][1:])

T6 = np.array(vals[250][1:])

z = np.linspace(0, 120, len(T0))

plt.plot(z, T5, label="t = 10 Gy")
plt.plot(z, T4, label="t = 7.5 Gy")
plt.plot(z, T3, label="t = 5 Gy")
plt.plot(z, T2, label="t = 2 Gy")
plt.plot(z, T1, label="t = 1 Gy")
plt.plot(z, T6, "--", label="t = 0.25 Gy")
plt.plot(z, T0, label="t=0 Gy")
plt.xlabel("Depth [km]")
plt.ylabel("Temperature [$\degree C$]")
plt.grid(True)
plt.legend()
plt.savefig("Output/T_vs_depth_V2.png", dpi=200)
plt.show()
