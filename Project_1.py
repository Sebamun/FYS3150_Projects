import numpy as np
import matplotlib.pyplot as plt

n = 10
h = 1 / (n + 1)
x = np.linspace(0,1,n)

u = 1 - (1 - np.exp(-10)) * x - np.exp(-10 * x)

f = np.zeros(n)
A = np.zeros((n,n))
a = np.full(10, 2)

for i in range(n-1):
    f[i] = - (u[i+1] + u[i-1] - 2 * u[i]) / h**2

qv = 2
z = 2

plt.plot(x,u)
plt.show()
