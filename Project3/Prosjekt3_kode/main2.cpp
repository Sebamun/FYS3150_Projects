// This code uses standard c++ allocation of arrays
#define _USE_MATH_DEFINES
#include <iostream>
#include <cmath>
#include <cstring>
#include <fstream>
#include <random>
#include <chrono>
#include <time.h>
#include "planet.hpp"
#include "solver.hpp"

using namespace std;

int main()
{
    double beta = 3.0; // For 3.99 så forlot den banen.
    //string Initial_values = "Initial_values.txt"; // Her henter vi initialbetingelser.
    int n = 100000;
    double FinalTime = 50.0;
    int dim = 3;

    solver binary_vv(100.0);

    double *x, *y, *z, *vx, *vy, *vz; //To store initial conditions for each object.
    double *mass;                     //Store mass of particles.
    int Nobjects = 9;
    x = new double[Nobjects];
    y = new double[Nobjects];
    z = new double[Nobjects];
    vx = new double[Nobjects];
    vy = new double[Nobjects];
    vz = new double[Nobjects];
    mass = new double[Nobjects];
    char *filename_pos_and_vel = "Textfiles/Initial.txt"; //Each line of file gives initial condition for a particle on the form: x y z vx vy vz
    //char* filename_mass = "masses.txt";
    //Open files
    FILE *fp_init = fopen(filename_pos_and_vel, "r"); //Open file to read, specified by "r".
    //FILE *fp_mass = fopen(filename_mass, "r"); //Open file to read.
    //Loop over each objects and extract its initial conditions:

    for (int i = 0; i < Nobjects; i++)
    {
        fscanf(fp_init, "%lf %lf %lf %lf %lf %lf %lf", &mass[i], &x[i], &y[i], &z[i], &vx[i], &vy[i], &vz[i]); // One %lf (lf=long float or double) for each floating point number on each line of the file.
        //fscanf(fp_mass, "%lf", &mass[i]); //Extract mass for particle i.
    }
    fclose(fp_init); //Close file with initial conditions
    //fclose(fp_mass); //Close file with masses.
    planet jupiter(mass[3]*100, x[3], y[3], z[3], vx[3], vy[3], vz[3]);
    planet earth(mass[5], x[5], y[5], z[5], vx[5], vy[5], vz[5]);
    planet sun(mass[8], x[8], y[8], z[8], vx[8], vy[8], vz[8]);
    binary_vv.add(jupiter);
    binary_vv.add(earth);
    binary_vv.add(sun);
    binary_vv.VelocityVerlet(dim, n, FinalTime, 3, 0., beta, 1);
    return 0;
}
