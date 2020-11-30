infileVV = open('PlanetsVV_9.txt', 'r')
#infileEU = open('PlanetsEU_2.txt', 'r')
lines = infileVV.readlines()

n = len(lines)
Nobjects = 9
timesteps = int(n/Nobjects)

r = np.zeros((Nobjects, 3, timesteps))
v = np.zeros((Nobjects, 3, timesteps))

for i in range(1, Nobjects + 1):
    for j in range(0, n, Nobjects):
        vals = lines[i*j].split()
        r[i, 0, t] =


for i in range(0, timesteps, 9):
    vals = lines[i].split()
    planet = int(vals[1])

'''
    for j in range(3):
        r[planet-1, j, i] = float(vals[j+3])
        v[planet-1, j, i] = float(vals[j+6])
'''
'''

    r[planet-1,0, i] = float(vals[2])
    r[planet-1,1, i] = float(vals[3])
    r[planet-1,2, i] = float(vals[4])

#print(r[:,:,:])


for i in range(Nobjects):
    plt.plot(r[i, 1, :], r[i, 2, :])
plt.show()

#print(r[1,:,:])

'''
'''
for j in range(3):
    r[planet-1, j, i] = float(vals[j+3])
    v[planet-1, j, i] = float(vals[j+6])

'''


#print(r)


'''
for i in range(Nobjects):
    plt.plot(r[:, i, 0], r[:, i, 1])
plt.show()
'''
'''
#infileEU = open('PlanetsEU_2.txt', 'r')
lines = infileVV.readlines()

n = len(lines)
Nobjects = 2
timesteps = n/Nobjects

r = np.zeros((n, Nobjects, 3))
v = np.zeros((n, Nobjects, 3))
t = np.zeros(n)

for i in range(n):
    vals = lines[i].split()
    t[i] = float(vals[0])
    planet = int(vals[1])
    for j in range(3):
        r[i, planet-1, j] = float(vals[j+3])
        v[i, planet-1, j] = float(vals[j+6])




print(r[:,0,0])
print(r[:,1,0])

for i in range(Nobjects):
    plt.plot(r[:, i, 0], r[:, i, 1])
plt.show()
'''
