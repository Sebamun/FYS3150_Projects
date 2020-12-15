#include <iostream>
#include <cmath>
#include <cstring>
#include <fstream>
#include <random>
#include <chrono>
#include <time.h>
#include <vector>
#include "Diffusion_solver.hpp"

using namespace std;

// parts of the function for backward Euler
int main()
{
    int num_int = 6;
    int num_time_steps = 1;
    double time_step = 0.001;
    double Length = 1.0;
    double u[num_int + 1], f[num_int -1];
    for (int i = 0; i <= num_int; i++){
        u[i] = 0.0;
    }
    // u[0] = 1.0;
    // u[num_int] = 2.0;
    for (int i = 0; i <= num_int - 2; i++)
    {
        f[i] = i + 1;
    }
    f[num_int - 2] = 6;
    for (int i = 0; i <= num_int - 2; i++)
        cout << u[i] << " " << f[i] << endl;
    cout << u[num_int-1] << endl;
    cout << u[num_int] << endl;

    Solver backward(num_int, num_time_steps, time_step, Length);
    backward.tridiag(-1.0, 2.0, -1.0, u, f);
    for (int i = 0; i <= num_int - 2; i++)
        cout << u[i] << " " << f[i] << endl;
    cout << u[num_int - 1] << endl;
    cout << u[num_int] << endl;
    }
