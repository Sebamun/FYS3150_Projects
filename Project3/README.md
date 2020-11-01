# Project 3

## Report

You can find the report document Project_3.pdf in the TEX folder.

## Code

We have used the following programming languages and packages: <br />

- C++
- Python
  - Pandas
  - Matplotlib
  - Numpy

To access the code of this project go to the Prosjekt3_kode folder. Here you will find a makefile, which will compile all our c++ programs. Use command `make all` to compile. You run the two body system of objects and plot their positions with the commands:<br />
```terminal
python3 Plotte.py # Plotting and runs executable 1.x.
```
Here we have run the program for beta = 3, 3.5 and 3.99 in the Velocity Verlet method. You run the three body system of objects and plot their positions with the commands:

```terminal
python3 Plotte2.py # Plotting and runs executable 2.x mass_adjust, with different mass adjustment for Jupiter.
```
Where mass_adjust=1,mass_adjust=10 and mass_adjust=1000. You run and plot the system of all the planets and the sun with the commands: <br />

```terminal
./3.x # Run the executable.
python3 Plotte3.py # Plotting.
```

Our data can be viewed in the folder Textfiles, where the positions and velocities are stored in the different textfiles. The method is given as vv_ (velocity verlet) or eu_ (euler) for the different methods and the number after _ is the number of objects in the system.

We have also used a python script to intiallize our initial positions and velocities. 

```terminal
python3 Initial.py # Write initial values to file. 
```

Which produces the textfile Initial.txt. We also want to test the speed of our algorithms. This is done by goin into the folder "Runtime_test" and use the commands:

```terminal
make all
./kjor_euler.x N # Here we run the executable for the Euler method.
./kjor_verlet.x N # Here we runt the executable for the Verlet method.
```
We compile these programmes with N=100000, N=1000000 and N=10000000. We can also check the accuracy of the two algorithms at different integration steps. This is done by using the commands:

```terminal
python3 PlotteN.py # Plotting of earth with different integration points.
```

Where we have integration points N=1000, N=5000 and N=10000. This is accessible in the "Prosjekt3_kode" folder after you have compiled, the same goes for plotting the angular momentum and energy for Velocity Verlet:

```terminal
python3 Plotte_ang_E.py # Plotting the angular momentum and energy for Velocity Verlet
```

We also have the plotting for the earth's orbit at different initial velocities. We changed these initial velocities manually and stored the data in textfiles at "Textfiles/Escape". You can run the program which plots the orbits at different initial velocities by using the commands:

```terminal
python3 photesc_vel.py # Plotting of earth's orbit with different initial velocities 
```



