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
    int IntegrationPoints; // No. of integration points
    double FinalTime;      // End time of calculation
    int Dimension;         // No. of spatial dimensions

    cout << "Earth-Sun binary system" << endl;
    Dimension = 3;

    IntegrationPoints = 10000;
    FinalTime = 50.;

    double TimeStep = FinalTime / ((double)IntegrationPoints);
    double x[3], v[3]; // positions and velocities
    // initial position x = 1AU, y = z = 0, vx = 2pi, vy=0, vz=0
    planet planet1(0.000003, 1., 0.0, 0.0, 0.0, 6.3, 0.); // Earth: (mass,x,y,z,vx,vy,vz)
    planet planet2(1., 0., 0., 0., 0., 0., 0.);           // Sun: (mass,x,y,z,vx,vy,vz)

    solver binary_vv(5.0);
    binary_vv.add(planet1);
    binary_vv.add(planet2);

    return 0;
}