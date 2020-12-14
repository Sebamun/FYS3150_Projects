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
    double a, b, c;
    int num_int = 1000;
    int num_time_steps = 1000;
    int time_step = 0.1;
    double Length = 1.0;
    Solver backward(num_int, num_time_steps, time_step, Length);
    backward.backward_euler();
}
