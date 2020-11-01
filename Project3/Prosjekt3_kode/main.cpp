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

int main(int argc, char const *argv[]){
    double beta = atof(argv[1]); // Vi prover for 3, 3.5 og 3.99
    int n = atoi(argv[2]); // Integrasjonspunkter.
    double FinalTime = 100.;
    int dim = 3;
    double x[3], v[3];

    planet planet1(0.000003, 1., 0.0, 0.0, 0.0, 6.3, 0.); // Earth: (mass,x,y,z,vx,vy,vz)
    planet planet2(1., 0., 0., 0., 0., 0., 0.);           // Sun: (mass,x,y,z,vx,vy,vz)

<<<<<<< HEAD
    planet planet3(1,-6.151489682016204E-03, 6.389988001518661E-03, 9.024482263224161E-05, 365*-7.240886699697975E-06-v_cm_x, 365*-5.140115343860045E-06-v_cm_y, 365*2.177046161642180E-07-v_cm_z); //Venus
    planet planet2(0.16601E-6, 3.269770816268355E-01, 7.809178409376630E-02, -2.460897254319929E-02, 365*-1.137000888603457E-02-v_cm_x, 365*2.875571677398091E-02-v_cm_y, 365*3.392751290933102E-03-v_cm_z); //Merkur
    planet planet1(2.4478383E-6,-3.335486637448234E-01, 6.454434722443811E-01, 2.775278968391979E-02, 365*-1.807712391477036E-02-v_cm_x, 365*-9.341060307773352E-03-v_cm_y, 365*9.148436818834693E-04-v_cm_z); //Sola

=======
>>>>>>> 8e4ae35b1654e3f94165e115ebc099adc78f5a52
    solver binary_vv(5.0);
    solver binary_eu(5.0);
    binary_vv.add(planet1);
    binary_vv.add(planet2);

    binary_eu.add(planet1);
    binary_eu.add(planet2);

<<<<<<< HEAD
    binary_eu.Euler(dim, n, FinalTime, 1, 0., beta);
    binary_vv.VelocityVerlet(dim, n, FinalTime, 3, 0., beta);
=======
    binary_eu.Euler(dim, n, FinalTime, 1, 0., 3,1);
    binary_vv.VelocityVerlet(dim, n, FinalTime, 1, 0., beta,1);
>>>>>>> 8e4ae35b1654e3f94165e115ebc099adc78f5a52

    return 0;
}
