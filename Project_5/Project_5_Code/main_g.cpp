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
    int num_int = 99;
    int num_time_steps = 1e6;
    double time_step = 1e-5;
    double Length = 1.0;
    double u[num_int + 1];
    double W0 = 0.5 * (1e-6 * 3600 * 24 * 365.24 * 1e9);
    double W1 = 1.4 * (1e-6 * 3600 * 24 * 365.24 * 1e9);
    double W2 = 0.35 * (1e-6 * 3600 * 24 * 365.24 * 1e9);
    double W3 = 0.05 * (1e-6 * 3600 * 24 * 365.24 * 1e9);
    double c_p = 1000.0;
    double rho = 3500.0;
    double kappa = 2.5;

    for (int i = 1; i <= num_int; i++)
    {
        u[i] = 10.77*i*120*Length/(num_int+1) + 8.0;
    }
    u[0] = 8.0;
    u[num_int] = 1300.0;

    double r[num_int + 1];
    Solver forward(num_int, num_time_steps, time_step, Length);
    forward.specific_forward(u, r, W0, W1, W2, W3, c_p, kappa, rho);
}
