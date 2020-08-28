import numpy as np
import matplotlib.pyplot as plt

n = 10000
h = 1/(n+1)
x = np.linspace(0,1,n)
f = 100*np.exp(-10*x)*h**2
d = 2
for j in range(1, n):
    f[j] = f[j] + (j)*f[j-1]/(j+1) #i=i+1
u = np.zeros(n)

u[-1] = n*f[-1]/(n+1)

for j in range(1, n):
    u[-j-1] = (f[-j-1]+u[-j])*((n-j)-1)/(n-j)  #i=(n-i)

u2 = 1 - (1 - np.exp(-10)) * x - np.exp(-10 * x)
# Her plotter vi:
fig, axes = plt.subplots(1,2)
axes[0].plot(x, u2)
axes[1].plot(x, u)
plt.show()
# d)
eps = np.log10((np.abs((u-u2)/u)))
max = np.max(eps[1:-1])
print(max)
