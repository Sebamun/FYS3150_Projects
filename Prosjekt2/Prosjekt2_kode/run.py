import subprocess
import matplotlib.pyplot as plt
import numpy as np
import sys
switch = str(sys.argv[1]) # Her bestemmer man om vi skal ha med kvanteledd.
ns = [10, 25, 50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300] # De ulike dimensjonene.
omega = [0.01, 0.5, 1, 5]
iterations = [] # Her lagres iterasjonsverdier.
CPU_time = [] # Her lagres CPU tiden for de ulike iterasjonstidene.
if switch =='0':
    for n in ns: # Looper gjennom dimensjonsverdiene:
        subprocess.run(['./Tridiag.x', str(n), switch, str(0)]) # Kjører c++ filen uten kvantetilfellet.
        infile = open("Output","r") # Her leser vi av verdiene for egenvektoren.
        for line in infile: # Går gjennom linje for linje:
            p = line.split()
            iterations.append(float(p[0])) # Henter verdier for iterasjoner.
            CPU_time.append(float(p[1])) # Henter verdier for CPU tiden.

    infile = open('Egenvektorer', 'r') # Aapner filen som man leser av egenvektoren.
    lines = infile.readlines() # Leser linjene i filen.
    eig_vec = np.zeros(len(lines)-1) # Her lagrer vi verdiene.
    for i in range(len(lines)-1): # Løper gjennom hver linje.
        eig_vec[i] = float(lines[i]) # Legger til egenvektor verdier fra filen.
    rho = np.linspace(0,1, len(eig_vec)) # Lengden vi studerer.
    n = np.arange(0,len(eig_vec))
    u = np.sin(n*np.pi/len(eig_vec)) # Regner ut den teoretiske egenvektoren.
    plt.title("Eigenvector for the lowest eigenvalue")
    plt.plot(rho, u/np.linalg.norm(u), 'r-', label='teor')
    plt.plot(rho, eig_vec, 'b--', label='Num')
    plt.legend()
    plt.xlabel('rho')
    plt.ylabel('Eigenvec')
    plt.savefig('Egenvektorer1')
    plt.show()
    #Plotting for antall iterasjoner og CPU tid:
    plt.title('Number of iterations')
    plt.plot(ns, iterations,'bo')
    plt.xlabel('Dimension')
    plt.ylabel('Iterations')
    plt.savefig('Iterasjoner')
    plt.show()
    plt.title('The CPU time')
    plt.plot(ns, CPU_time,'bo')
    plt.xlabel('Dimension')
    plt.ylabel('CPU time')
    plt.savefig('CPU_tid')
    plt.show()
else: # Dette er for kvantetilfellet.
    omega = [0.01, 0.5, 1, 5] # Ulike verdiene for omega.
    for i in omega:
        subprocess.run(['./Tridiag.x', str(300), switch, str(i)])
        infile = open('Egenvektorer', 'r') # Aapner filen som man leser av egenvektoren.
        lines = infile.readlines() # Leser linjene i filen.
        eig_vec = np.zeros(len(lines)-1) # Her lagrer vi verdiene.
        for j in range(len(lines)-1): # Løper gjennom hver linje.
            eig_vec[j] = float(lines[j]) # Legger til egenvektor verdier fra filen.
        rho = np.linspace(0,1, len(eig_vec)) # Lengden vi studerer.
        plt.plot(rho, np.abs(eig_vec), label=f'$\omega$={i}')
    plt.title("Eigenvector for quantom case given $\omega$")
    plt.xlabel('rho')
    plt.ylabel('Eigenvec')
    plt.legend()
    plt.savefig('Egenvektorer_omega')
    plt.show()
