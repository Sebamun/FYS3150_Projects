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
int main(int argc, char *argv[])
{
    int factor = atof(argv[1]);
    double variable = atof(argv[2]);
    int num_int = factor;
    int num_time_steps = 100 * (factor * factor);
    double time_step = variable / (factor * factor);
    double Length = 1.0;
    double u[num_int + 1], f[num_int - 1];

    for (int i = 0; i <= num_int; i++)
    {
        u[i] = 0.0;
    }
    u[num_int] = 1.0;

    Solver backward(num_int, num_time_steps, time_step, Length);
    backward.backward_euler(u, f);

    for (int i = 0; i <= num_int; i++)
    {
        u[i] = 0.0;
    }
    u[num_int] = 1.0;

    Solver crank(num_int, num_time_steps, time_step, Length);
    crank.crank_nicholson(u, f);

    for (int i = 0; i <= num_int; i++)
    {
        u[i] = 0.0;
    }
    u[num_int] = 1.0;

    double r[num_int + 1];
    Solver forward(num_int, num_time_steps, time_step, Length);
    forward.forward_euler(u, r);
}