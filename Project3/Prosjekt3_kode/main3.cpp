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
    int n = 100000;    // Integrasjonspunkter.
    double FinalTime = 100.;
    int dim = 3;
    double x[3], v[3];
    planet planet1(0.16601E-6, 3.269770816268355E-01, 7.809178409376630E-02, - 2.460897254319929E-02, - 1.137000888603457E-02*365, 2.875571677398091E-02*365, 3.392751290933102E-03*365);
    planet planet2(1., -6.151489682016204E-03, 6.389988001518661E-03, 9.024482263224161E-05, - 7.240886699697975E-06*365, - 5.140115343860045E-06*365, 2.177046161642180E-07*365); // Sun: (mass,x,y,z,vx,vy,vz)

    solver binary_vv(5.0);
    binary_vv.add(planet1);
    binary_vv.add(planet2);
    binary_vv.VelocityVerlet(dim, n, FinalTime, 1, 0., beta, 0);

    return 0;
}
