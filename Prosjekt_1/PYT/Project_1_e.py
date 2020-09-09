import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import lu
import time




start_time = time.time()

n = 10
h = 1/(n+1)

u = np.zeros(n+1)
u[0] = 100



A = np.zeros((10, 10), int) #Creating a matrix A
for i in range(10):
    for j in range(10):
        if i==j:
            np.fill_diagonal(A,2, wrap=True)
        elif i == j+1:
            A[i,j] = -1
        elif i == j-1:
            A[i,j] = -1



x = np.linspace(0,1,n)
f = 100*np.exp(-10*x)*h**2 #our given function


for i in range(1,n):
    f[i] = f[i] + (i-1)*f[i-1]/i


P,L,U = lu(A) #calculating the LU decompsition

L_inv = np.linalg.inv(L)

y = L_inv@f*h**2

U_inv = np.linalg.inv(U)

x = U_inv@y

print(x)
print("--- %s seconds ---" % (time.time() - start_time))


A = np.zeros((100, 100), int)
for i in range(10):
    for j in range(10):
        if i==j:
            np.fill_diagonal(A,2, wrap=True)
        elif i == j+1:
            A[i,j] = -1
        elif i == j-1:
            A[i,j] = -1



x = np.linspace(0,1,100)
f = 100*np.exp(-10*x)*h**2


for i in range(1,n):
    f[i] = f[i] + (i-1)*f[i-1]/i


P,L,U = lu(A)

L_inv = np.linalg.inv(L)

y = L_inv@f*h**2

U_inv = np.linalg.inv(U)

x = U_inv@y

print("--- %s seconds ---" % (time.time() - start_time))

A = np.zeros((1000, 1000), int)
for i in range(10):
    for j in range(10):
        if i==j:
            np.fill_diagonal(A,2, wrap=True)
        elif i == j+1:
            A[i,j] = -1
        elif i == j-1:
            A[i,j] = -1



x = np.linspace(0,1,1000)
f = 100*np.exp(-10*x)*h**2


for i in range(1,n):
    f[i] = f[i] + (i-1)*f[i-1]/i


P,L,U = lu(A)

L_inv = np.linalg.inv(L)

y = L_inv@f*h**2

U_inv = np.linalg.inv(U)

x = U_inv@y

print("--- %s seconds ---" % (time.time() - start_time))

A = np.zeros((10000, 10000), int)
for i in range(10):
    for j in range(10):
        if i==j:
            np.fill_diagonal(A,2, wrap=True)
        elif i == j+1:
            A[i,j] = -1
        elif i == j-1:
            A[i,j] = -1



x = np.linspace(0,1,10000)
f = 100*np.exp(-10*x)*h**2


for i in range(1,n):
    f[i] = f[i] + (i-1)*f[i-1]/i


P,L,U = lu(A)

L_inv = np.linalg.inv(L)

y = L_inv@f*h**2

U_inv = np.linalg.inv(U)

x = U_inv@y

print("--- %s seconds ---" % (time.time() - start_time))
