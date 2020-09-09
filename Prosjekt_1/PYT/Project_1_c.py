import numpy as np
import matplotlib.pyplot as plt

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
    x_new = x[1:-2]
    u_new = u[1:-2]
    return x_new, u_new
# Her er den analytiske verdien:
x2 = np.linspace(0,1,1e5) # Intervall.
u2 = 1 - (1 - np.exp(-10)) * x2 - np.exp(-10 * x2) # Analytiske.
# Her plotter vi:
fig, axes = plt.subplots(1,7)
axes[0].plot(x2[1:-2], u2[1:-2])
axes[1].plot(algo(10)[0], algo(10)[1])
axes[2].plot(algo(100)[0], algo(100)[1])
axes[3].plot(algo(1000)[0], algo(1000)[1])
axes[4].plot(algo(10000)[0], algo(10000)[1])
axes[5].plot(algo(100000)[0], algo(100000)[1])
axes[6].plot(algo(1000000)[0], algo(1000000)[1])
# Navn på plott:
fig.suptitle('u(x)')
axes[0].title.set_text('analytiske')
axes[1].title.set_text('n=10')
axes[2].title.set_text('n=100')
axes[3].title.set_text('n=1000')
axes[4].title.set_text('n=10000')
axes[5].title.set_text('n=100000')
axes[6].title.set_text('n=1000000')
axes[0].set_xlabel('x')
axes[0].set_ylabel('u(x)')
plt.show()
# d)
diff = np.abs((u_new-u2_new)) # Differansen mellom den analytiske og numeriske verdien.
eps = np.abs((u_new-u2_new)/u2_new) # Den relative feilen.
max = np.max(eps) # Den maksimale relative feilen.
q = np.where(eps == np.max(eps))
plt.plot(x_new[q], u_new[q], 'o') # Sier hvor punktet som gir stoorst avvik ligger.
plt.show()

'''
plt.plot(x_new, diff, '--')
plt.plot(x_new, np.log(eps), '--')
#plt.yscale('log')
plt.show()
'''
