import numpy as np
import matplotlib.pyplot as plt
import time

start_time = time.time()

# c)
def algo(n):# n er Antall maalepunkter.
    h = 1/(n+1) # Steglengde.
    x = np.linspace(0,1,n) # Intervall.
    f = 100*np.exp(-10*x)*h**2 # Funksjonen.
    for j in range(1, n): # Regner ut hooyre side.
        f[j] = f[j] + (j)*f[j-1]/(j+1) # Når indexer i=i+1 borsett fra i vektorer.
    u = np.zeros(n) # Lagres sluttverdiene.
    u[-1] = 0 # Her definerer vi det siste punktet.
    for j in range(1, n-1): # Backward substitution.
        u[-j-1] = (f[-j-1]+u[-j])*((n-j)-1)/(n-j)  #i=(n-i)
        #Legger til 1 hver gang det står j.
    # Lager nye arrays der jeg eksluderer ytterpunktene:
    u2 = 1 - (1 - np.exp(-10)) * x - np.exp(-10 * x) # Analytiske.
    return x, u, u2
#max = np.zeros(6)
# Lagrer verdiene gitt ulike n:
n = [10,10**2,10**3,10**4,10**5,10**6]
for i in range(len(n)):
    #x_new = algo(n[i])[0]
    u_new = algo(n[i])[1]

    print("--- %s seconds ---" % (time.time() - start_time))
