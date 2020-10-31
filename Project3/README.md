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
./2.x # Run the executable.
python3 Plotte2.py # Plotting.
```
You run and plot the system of all the planets and the sun with the commands: <br />

```terminal
./3.x # Run the executable.
python3 Plotte3.py # Plotting.
```

Our data can be viewed in the folder Textfiles, where the positions and velocities are stored in the different textfiles. The method is given as vv_ (velocity verlet) or eu_ (euler) for the different methods and the number after _ is the number of objects in the system.

We have also used a python script to intiallize our initial positions and velocities. 

```terminal
python3 Initial.py # Write initial values to file. 
```

Which produces the textfile Initial.txt.
