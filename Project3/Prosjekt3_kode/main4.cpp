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
    //int n = 100000000; // Integration points for the simulation of 100 yrs.
    int n = 10000000; // Integration points for the second simulation
    //double FinalTime = 100.; 
    double FinalTime = 0.3; 
    int dim = 3;
    double x[3], v[3];
    //planet planet3(1., 0.0, 0.0, 0.0, 0.0, 0.0, 0.0); // Initialize the sun for the simulation of 100 yrs.
    //planet planet2(0.16601E-6, 0.3075, 0.0, 0.0, 0.0, 12.44, 0.0); // Initialize Mercury for the simulation of 100 yrs.
    //planet planet3(1., 0.0, 0.0, 0.0, 0.0, 0.0, 0.0); // Initialize the sun for the simulation of 100 yrs.
    //planet planet2(0.16601E-6, 0.3075, 0.0, 0.0, 0.0, 12.44, 0.0); // Initialize Mercury for the simulation of 100 yrs.
    //planet planet3(1., 1.16414e-07, 0.000206485, 0.0, 7.11683e-07, 3.27174e-06, 0.0); //Initialize the sun with the final position and velocity from the 100 yr run
    //planet planet2(0.16601E-6, -0.414621, 0.189561, 0.0, -4.28728, -7.26804, 0.0); //Initialize Mercury with the final position and velocity from the 100 yr run without rel cor
    planet planet3(1., 1.12758e-07, 0.000206485, 0.0, 7.10902e-07, 3.27209e-06, 0.0);                  //Initialize the sun with the final position and velocity from the 100 yr run
    planet planet2(0.16601E-6, -0.414729, 0.189359, 0.0, -4.28302, - 7.27019, 0.0);           //Initialize Mercury with the final position and velocity from the 100 yr run without rel cor
    solver binary_vv(5.0);
    binary_vv.add(planet2);
    binary_vv.add(planet3);
    binary_vv.VelocityVerlet(dim, n, FinalTime, 2, 0., beta, 0);
    return 0;
}
