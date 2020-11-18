<<<<<<< HEAD
// This code uses standard c++ allocation of arrays

=======
// Her kjører vi gjennom programmet med alle objektene.
>>>>>>> c095c616f23321b4d91f5c1b962e8304cfac9115
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
<<<<<<< HEAD

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
=======
using namespace std;
int main(){
    double beta = 3.0; // For 3.99 så forlot den banen.
    int n = 100000; // Antall steg.
    double FinalTime = 170.; // Tiden vi kjører over i år.
    int dim = 3; // Dimensjonene vi studerer.
    solver binary_vv(100.0); // Kaller på globale variabler.
    double *mass, *x, *y, *z, *vx, *vy, *vz; // Lagrer initialverdiene i disse.
    int Nobjects = 9; // Antall objekter.
    mass = new double[Nobjects]; // Definerer hvor mange verdier vi får lagret i minnet.
    x = new double[Nobjects];
    y = new double[Nobjects];
    z = new double[Nobjects];
    vx = new double[Nobjects];
    vy = new double[Nobjects];
    vz = new double[Nobjects];
    char* filename_pos_and_vel = "Textfiles/Initial.txt"; // Tekstfil på form m,x,y,z,vx,vy,vz
    FILE *fp_init = fopen(filename_pos_and_vel, "r"); // Åpner filen.
    for (int i = 0; i < Nobjects; i++){ // Her hentes initialbetingelsene:
    	fscanf(fp_init, "%lf %lf %lf %lf %lf %lf %lf",
      &mass[i], &x[i], &y[i], &z[i], &vx[i], &vy[i], &vz[i]);
      planet planet_(mass[i], x[i], y[i], z[i], vx[i], vy[i], vz[i]); // Gir objektene initialbetingelser.
      binary_vv.add(planet_); // Legger til objektene.
    }
    fclose(fp_init); // Lukker filen med initialbetingelser.
    binary_vv.VelocityVerlet(dim, n, FinalTime, 9, 0., beta,1); // Kaller på løsningsmetoden.
  return 0;
>>>>>>> c095c616f23321b4d91f5c1b962e8304cfac9115
}
