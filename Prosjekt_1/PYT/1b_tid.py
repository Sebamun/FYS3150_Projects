import numpy as np
import matplotlib.pyplot as plt
import time

start_time = time.time()

def algo(n):
    h = 1.0 / (n + 1.0) # Steglengde.
    x = np.linspace(0,1,n) # Intervallet vi studerer.
    f = 100 * np.exp(-10 * x) * h**2 # Dette er funksjonen.
    f_m = np.zeros(n) # Her lagrer vi verdiene for den nye funksjonen.
    #Diagonalen for matrisen er gitt:
    a = np.full(n,-1, dtype='float')
    b = np.full(n,2, dtype='float')
    c = np.full(n,-1, dtype='float')
    b_m = np.zeros(n) # Her lagrer jeg verdiene for den nye diagonalen.
    # Initialbetingleser:
    f_m[0] = f[0]
    b_m[0] = b[0]
    # Steg 1:
    for j in range(1,n):
        b_m[j] = b[j] - (a[j] * c[j-1] / b_m[j-1])
        f_m[j] = f[j] - (a[j] * f_m[j-1] / b_m[j-1])
    u = np.zeros(n) # Her lagrer vi verdiene for u.
    u[-1] = 0 # Her setter vi den siste verdien for u.
    # Steg 2:
    for j in range(1,n-1):
        u[-j-1] = (f_m[-j-1] - c[-j-1] * u[-j]) / b_m[-j-1] # Den numeriske tilnærmingen.
        #print("--- %s seconds ---" % (time.time() - start_time))

    u2 = 1 - (1 - np.exp(-10)) * x - np.exp(-10 * x) # Den analystiske løsningen.
    return x, u, u2

z = [10,10**2,10**3,10**4,10**5,10**6]

for i in range(len(z)):
    u_new = algo(z[i])[1]
    print("--- %s seconds ---" % (time.time() - start_time))
