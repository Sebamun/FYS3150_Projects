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
    int n = 1000;
    double FinalTime = 50.;
    int dim = 3;
    double x[3], v[3];
    planet planet1(0.000003, 1., 0.0, 0.0, 0.0, 6.3, 0.); // Earth: (mass,x,y,z,vx,vy,vz)
    planet planet2(1., 0., 0., 0., 0., 0., 0.);           // Sun: (mass,x,y,z,vx,vy,vz)
    solver binary_vv(5.0);
    //solver binary_eu(5.0);
    binary_vv.add(planet1);
    binary_vv.add(planet2);
    //binary_eu.add(planet1);
    //binary_eu.add(planet2);

    binary_vv.VelocityVerlet(dim, n, FinalTime, 1, 0.);
    binary_vv.Euler(dim, n, FinalTime, 1, 0.);

    return 0;
}