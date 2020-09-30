import subprocess
import matplotlib.pyplot as plt
import numpy as np
import sys
ns = [10, 25, 50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300] # De ulike dimensjonene.
iterations = [] # Her lagres iterasjonsverdier.
CPU_time = [] # Her lagres CPU tiden for de ulike iterasjonstidene.
switch = str(sys.argv[1]) # Her bestemmer man om vi skal ha med kvanteledd.
for n in ns: # Løper gjennom dimensjonsverdiene:
    subprocess.run(['./Tridiag.x', str(n), switch]) # Kjører c++ filen.
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
#u = np.zeros(len(eig_vec))
n = np.arange(0,len(eig_vec)) # Regner ut den teoretiske egenvektoren.
u = np.sin(n*np.pi/len(eig_vec))
# Plotting for egenvektor for den laveste egenverdien:
if switch=='0': # Bestemmer hvilken teoretisk løsning vi skal ta med. 
    plt.title("Eigenvector for the lowest eigenvalue")
    plt.plot(rho, u/np.linalg.norm(u), label='teor')
else:
    plt.title("Eigenvector for the lowest eigenvalue in quantom case")
    # Her går plottet for den teoretiske egenvektoren i kvantetilfellet.
plt.plot(rho, eig_vec, label='Num')
plt.xlabel('rho')
plt.ylabel('Eigenvec')
plt.legend()
plt.show()
#Plotting for antall iterasjoner og CPU tid:
plt.title('Number of iterations')
plt.plot(ns, iterations,'bo')
plt.xlabel('Dimension')
plt.ylabel('Iterations')
plt.show()
plt.title('The CPU time')
plt.plot(ns, CPU_time,'bo')
plt.xlabel('Dimension')
plt.ylabel('CPU time')
plt.show()
