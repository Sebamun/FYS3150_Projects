#ifndef PLANET_H
#define PLANET_H
#define _USE_MATH_DEFINES
#include <cmath>
#include <vector>
using std::vector;

class planet{

public:
    // Globale verdier:
    double mass;
    double position[3];
    double velocity[3];
    double potential;
    double kinetic;
    //Initialiserer:
    planet(double M, double x, double y, double z, double vx, double vy,
      double vz);
    // Funksjoner:
    double distance(planet otherPlanet);
    double GravitationalForce(planet otherPlanet, double Gconst);
    double Acceleration(planet otherPlanet, double Gconst);
    double KineticEnergy();
    double PotentialEnergy(planet &otherPlanet, double Gconst, double epsilon);
};
#endif
