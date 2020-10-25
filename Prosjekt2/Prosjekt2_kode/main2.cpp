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
    double beta = 3.99;
    //string Initial_values = "Initial_values.txt"; // Her henter vi initialbetingelser.
    int n = 100000; // Integrasjonspunkter.
    double FinalTime = 50.;
    int dim = 3;
    double x[3], v[3];

          // Create a text string, which is used to output the text file
      string myText;

      // Read from the text file
      ifstream MyReadFile("Initial_values.txt");

      // Use a while loop together with the getline() function to read the file line by line
      while (getline (MyReadFile, Initial_values)) {
        // Output the text from the file
        cout << myText << endl;
      }

      // Close the file
      MyReadFile.close();




    planet planet1(0.000003, 1., 0.0, 0.0, 0.0, 6.3, 0.); // Earth: (mass,x,y,z,vx,vy,vz)
    planet planet2(1., 0., 0., 0., 0., 0., 0.);           // Sun: (mass,x,y,z,vx,vy,vz)
    planet planet3(0.003, 5.20, 0.0, 0.0, 0.0 , 10.0, 0.); //Jupiter


    solver binary_vv(5.0);
    solver binary_eu(5.0);
    binary_vv.add(planet1);
    binary_vv.add(planet2);
    binary_vv.add(planet3);
    binary_eu.add(planet1);
    binary_eu.add(planet2);

    binary_eu.Euler(dim, n, FinalTime, 1, 0., beta);
    binary_vv.VelocityVerlet(dim, n, FinalTime, 1, 0., beta);


    return 0;
}
