// Her kjører vi gjennom programmet med alle objektene.
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
    char* filename_pos_and_vel = "Initial.txt"; // Tekstfil på form m,x,y,z,vx,vy,vz
    FILE *fp_init = fopen(filename_pos_and_vel, "r"); // Åpner filen.
    for (int i = 0; i < Nobjects; i++){ // Her hentes initialbetingelsene:
    	fscanf(fp_init, "%lf %lf %lf %lf %lf %lf %lf",
      &mass[i], &x[i], &y[i], &z[i], &vx[i], &vy[i], &vz[i]);
      planet planet_(mass[i], x[i], y[i], z[i], vx[i], vy[i], vz[i]); // Gir objektene initialbetingelser.
      binary_vv.add(planet_); // Legger til objektene.
    }
    fclose(fp_init); // Lukker filen med initialbetingelser.
    binary_vv.VelocityVerlet(dim, n, FinalTime, 9, 0., beta); // Kaller på løsningsmetoden.
  return 0;
}
