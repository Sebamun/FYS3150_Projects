import numpy as np
import matplotlib.pyplot as plt
n = 10000 # Antall målepunkter.
h = 1/(n+1) # Steglengde.
x = np.linspace(0,1,n) # Intervall.
f = 100*np.exp(-10*x)*h**2 # Funksjonen.
d = 2
for j in range(1, n): # Regner ut høyre side.
    f[j] = f[j] + (j-1)*f[j-1]/(j)
u = np.zeros(n) # Lagres sluttverdiene.
u[-1] = n*f[-1]/(n+1) # Her definerer vi det siste punktet.
for j in range(1, n): # Backward substitution.
    u[-j-1] = (f[-j-1]+u[-j])*((n-j)-1)/(n-j)  #i=(n-i)
u2 = 1 - (1 - np.exp(-10)) * x - np.exp(-10 * x) # Analytiske.
# Her plotter vi:
plt.plot(x, u2)
plt.plot(x, u,'--')
#plt.show()

# d)
eps = np.abs((u-u2)/u2)*100
#eps = np.log10((np.abs((u-u2)/u2))) # Den relative feilen.
max = np.max(eps[1:-1]) # Den maksimale relative feilen.
q = np.where(eps[1:-1] == np.max(eps[1:-1]))
plt.plot(x[q], u[q], 'o') # Sier hvor punktet som gir størst avvik ligger.
plt.plot(x[-1], u[-1],'p') # Siste punktet
plt.show()
print(max)
