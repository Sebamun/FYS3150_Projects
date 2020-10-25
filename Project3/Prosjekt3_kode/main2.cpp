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

int main(){
    double beta = 3.0; // For 3.99 så forlot den banen.
    //string Initial_values = "Initial_values.txt"; // Her henter vi initialbetingelser.
    int n = 100000;
    double FinalTime = 170.; //50
    int dim = 3;

    solver binary_vv(100.0);

    double *x, *y, *z, *vx, *vy, *vz; //To store initial conditions for each object.
    double *mass; //Store mass of particles.
    int Nobjects = 9;
    x = new double[Nobjects];
    y = new double[Nobjects];
    z = new double[Nobjects];
    vx = new double[Nobjects];
    vy = new double[Nobjects];
    vz = new double[Nobjects];
    mass = new double[Nobjects];
    char* filename_pos_and_vel = "Initial.txt";   //Each line of file gives initial condition for a particle on the form: x y z vx vy vz
    //char* filename_mass = "masses.txt";
    //Open files
    FILE *fp_init = fopen(filename_pos_and_vel, "r"); //Open file to read, specified by "r".
    //FILE *fp_mass = fopen(filename_mass, "r"); //Open file to read.
    //Loop over each objects and extract its initial conditions:

    for (int i = 0; i < Nobjects; i++){
    	fscanf(fp_init, "%lf %lf %lf %lf %lf %lf %lf", &mass[i], &x[i], &y[i], &z[i], &vx[i], &vy[i], &vz[i]); // One %lf (lf=long float or double) for each floating point number on each line of the file.
      //fscanf(fp_mass, "%lf", &mass[i]); //Extract mass for particle i.
      planet planet_(mass[i], x[i], y[i], z[i], vx[i], vy[i], vz[i]);
      //cout<<mass[i]<<','<<x[i]<<','<<y[i]<<','<<z[i]<<','<<vx[i]*365<<','<<vy[i]*365<<','<<vz[i]*365<<endl;
      binary_vv.add(planet_);
    }
    fclose(fp_init); //Close file with initial conditions
    //fclose(fp_mass); //Close file with masses.

    binary_vv.VelocityVerlet(dim, n, FinalTime, 9, 0., beta);
  return 0;
}
