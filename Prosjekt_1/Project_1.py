import numpy as np
import matplotlib.pyplot as plt
n = 100 # Antall punkter.
h = 1 / (n + 1) # Steglengde.
x = np.linspace(0,1,n) # Intervallet vi studerer.
f = 100 * np.exp(-10 * x) * h**2 # Dette er funksjonen.
f_m = np.zeros(n) # Her lagrer vi verdiene for den nye funksjonen.
u_l = 1 - (1 - np.exp(-10)) * x - np.exp(-10 * x) # Dette er den analystiske løsningen.
#Diagonalen for matrisen er gitt:
a = np.full(n,-1, dtype='float')
b = np.full(n,2, dtype='float')
c = np.full(n,-1, dtype='float')
b_m = np.zeros(n) # Her lagrer jeg verdiene for den nye diagonalen.
# Initialbetingleser:
f_m[0] = f[0]
b_m[0] = b[0]
# Steg 1:
for i in range(1,n):
    b_m[i] = b[i] - (a[i] * c[i-1] / b_m[i-1])
    f_m[i] = f[i] - (a[i] * f_m[i-1] / b_m[i-1])
u = np.zeros(n) # Her lagrer vi verdiene for u.
u[-1] = f_m[-1] / b_m[-1] # Her setter vi den siste verdien for u.
# Steg 2:
for i in range(1,n):
    u[-i-1] = (f_m[-i-1] - c[-i-1] * u[-i]) / b_m[-i-1]
# Her plotter vi:
fig, (ax_1, ax_2) = plt.subplots(1, 2)
fig.suptitle('Tittel')
ax_1.plot(x, u)
ax_2.plot(x, u_l)
plt.show()
