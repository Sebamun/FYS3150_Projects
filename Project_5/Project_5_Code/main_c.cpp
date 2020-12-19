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
    int num_int = factor;
    int num_time_steps = 1000 * (factor * factor);
    double time_step = 0.001 / (factor * factor);
    double Length = 1.0;
    double u[num_int + 1], f[num_int - 1];

    for (int i = 0; i <= num_int; i++)
    {
        u[i] = 0.0;
    }
    u[num_int] = 1.0;

    Solver backward(num_int, num_time_steps, time_step, Length);
    clock_t start1, end1;
    start1 = clock();
    backward.backward_euler(u, f);
    end1 = clock();
    double time1 = ((double)end1 - (double)start1) / CLOCKS_PER_SEC;
    cout << "Time elapsed for backward:"
         << "\t" << time1 << "s at dx=1/" << factor << endl;

    for (int i = 0; i <= num_int; i++)
    {
        u[i] = 0.0;
    }
    u[num_int] = 1.0;

    Solver crank(num_int, num_time_steps, time_step, Length);
    clock_t start2, end2;
    start2 = clock();
    crank.crank_nicholson(u, f);
    end2 = clock();
    double time2 = ((double)end2 - (double)start2) / CLOCKS_PER_SEC;
    cout << "Time elapsed for crank:"
         << "\t" << time2 << "s at dx=1/" << factor << endl;

    for (int i = 0; i <= num_int; i++)
    {
        u[i] = 0.0;
    }
    u[num_int] = 1.0;

    double r[num_int + 1];
    Solver forward(num_int, num_time_steps, time_step, Length);
    clock_t start3, end3;
    start3 = clock();
    forward.forward_euler(u, r);
    end3 = clock();
    double time3 = ((double)end3 - (double)start3) / CLOCKS_PER_SEC;
    cout << "Time elapsed for forward:"
         << "\t" << time3 << "s at dx=1/" << factor << endl;
}