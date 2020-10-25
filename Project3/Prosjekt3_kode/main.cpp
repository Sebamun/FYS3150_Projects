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
    int n = 100000; // Integrasjonspunkter.
    double FinalTime = 100.;
    int dim = 3;
    double x[3], v[3];

    double v_cm_x = 365 * (-7.240886699697975E-06 - 1.137000888603457E-02 * 0.16601E-6) / (1.0 + 0.16601E-6);
    double v_cm_y = 365 * (-5.140115343860045E-06 + 2.875571677398091E-02 * 0.16601E-6) / (1.0 + 0.16601E-6);
    double v_cm_z = 365 * (2.177046161642180E-07 + 3.392751290933102E-03 * 0.16601E-6) / (1.0 + 0.16601E-6);

    planet planet3(1,-6.151489682016204E-03, 6.389988001518661E-03, 9.024482263224161E-05, 365*-7.240886699697975E-06-v_cm_x, 365*-5.140115343860045E-06-v_cm_y, 365*2.177046161642180E-07-v_cm_z); //Venus
    planet planet2(0.16601E-6, 3.269770816268355E-01, 7.809178409376630E-02, -2.460897254319929E-02, 365*-1.137000888603457E-02-v_cm_x, 365*2.875571677398091E-02-v_cm_y, 365*3.392751290933102E-03-v_cm_z); //Merkur
    planet planet1(2.4478383E-6,-3.335486637448234E-01, 6.454434722443811E-01, 2.775278968391979E-02, 365*-1.807712391477036E-02-v_cm_x, 365*-9.341060307773352E-03-v_cm_y, 365*9.148436818834693E-04-v_cm_z); //Sola

    solver binary_vv(5.0);
    solver binary_eu(5.0);
    binary_vv.add(planet1);
    binary_vv.add(planet2);
    binary_vv.add(planet3);
    //binary_eu.add(planet1);
    //binary_eu.add(planet2);

    //binary_eu.Euler(dim, n, FinalTime, 1, 0., beta);
    binary_vv.VelocityVerlet(dim, n, FinalTime, 3, 0., beta);

    return 0;
}
