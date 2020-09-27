#include <iostream>
#include <fstream>
#include <math.h>
#include <iomanip>
#include <armadillo>
#include <time.h>
#include <vector>

using namespace std;
using namespace arma;

int Initialize(int Dim, double Rmin, double Rmax, mat &U);
int check(int Dim, double Rmax, mat &U);
