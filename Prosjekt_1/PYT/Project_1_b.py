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
        print("--- %s seconds ---" % (time.time() - start_time))

    u2 = 1 - (1 - np.exp(-10)) * x - np.exp(-10 * x) # Den analystiske løsningen.
    return x, u, u2
# Her plotter vi:fig, axes = plt.subplots(1,3)
fig, axes = plt.subplots(1,3)

axes[0].plot(algo(10)[0], algo(10)[1])



axes[0].plot(algo(10)[0], algo(10)[2],'--')

print("--- %s seconds ---" % (time.time() - start_time))

axes[1].plot(algo(100)[0], algo(100)[1])



axes[1].plot(algo(100)[0], algo(100)[2],'--')

print("--- %s seconds ---" % (time.time() - start_time))

axes[2].plot(algo(1000)[0], algo(1000)[1])

print("--- %s seconds ---" % (time.time() - start_time))

axes[2].plot(algo(10000)[0], algo(10000)[2],'--')

print("--- %s seconds ---" % (time.time() - start_time))

axes[2].plot(algo(100000)[0], algo(100000)[2],'--')

print("--- %s seconds ---" % (time.time() - start_time))

axes[2].plot(algo(1000000)[0], algo(1000000)[2],'--')

print("--- %s seconds ---" % (time.time() - start_time))



=======
axes[0].plot(algo(10)[0], algo(10)[1], label='Computed')
axes[0].plot(algo(10)[0], algo(10)[2],'--', label='Analytical')
axes[1].plot(algo(100)[0], algo(100)[1], label='Computed')
axes[1].plot(algo(100)[0], algo(100)[2],'--', label='Analytical')
axes[2].plot(algo(1000)[0], algo(1000)[1], label='Computed')
axes[2].plot(algo(1000)[0], algo(1000)[2],'--', label='Analytical')
axes[0].legend(loc="upper right")
axes[1].legend(loc="upper right")
axes[2].legend(loc="upper right")
>>>>>>> 5c4c6ddfbcf3798c69e257a92116cc287dee6951
# Navn på plott:
fig.suptitle('Analytical vs Computed')
axes[0].title.set_text('n=10')
axes[1].title.set_text('n=100')
axes[2].title.set_text('n=1000')
axes[0].set_xlabel('x')
axes[0].set_ylabel('u(x)')
axes[0].set_xlabel('x')
axes[0].set_ylabel('u(x)')
axes[1].set_xlabel('x')
axes[1].set_ylabel('u(x)')
axes[2].set_xlabel('x')
axes[2].set_ylabel('u(x)')
plt.tight_layout()
plt.show()
fig.savefig('1b.png', dpi=fig.dpi)
#print(time.clock()) # "Process time in seconds"
print(algo(10)[1])
