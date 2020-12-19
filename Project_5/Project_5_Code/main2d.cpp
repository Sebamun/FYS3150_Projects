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
    int num_time_steps = 50000;
    double time_step = 0.00001;
    double Length = 1.0;
    double **u;
    double **r;
    u = new double*[num_int+1];
    r = new double*[num_int+1];
    for (int i = 0; i <= num_int; i++){
        u[i] = new double[num_int+1];
        r[i] = new double[num_int+1];
    }
    for (int i = 0; i < num_int; i++){
        for (int j = 0; j <= num_int; j++){
            u[i][j] = 1.0;
            //cout << u[i][j] << endl;
        }
    }
    for (int i = 0; i <= num_int; i++){
        u[num_int][i] = 0.0;
        u[0][i] = 0.0;
        u[i][num_int] = 0.0;
        u[i][0] = 0.0;

    }
    cout << "initialized" << endl;
    Solver forward_2d(num_int, num_time_steps, time_step, Length);
    cout << "initialized solver" << endl;
    forward_2d.forward_euler2d(u, r);
}
