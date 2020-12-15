#include <ostream>
#include <iostream>
#include "Diffusion_solver.hpp"
using namespace std;


Solver::Solver(int num_int, int num_time_steps, double time_step, double Length)
{
    cout << "Init called" << endl;
    n = num_int;
    L = Length;
    dx = L/(n+1);
    dt = time_step;
    Nt = num_time_steps;
    alpha = dt/dx/dx;
    
    cout << "alpha=" << alpha << endl;
    cout << "dt=" << dt << endl;
    cout << "n=" << n << endl;
    cout << "Nt=" << Nt << endl;
    cout << "dx=" << dx << endl;
    
};

void Solver::forward_euler(double *u, double *r){
    for (int i = 0; i <= n; i++)
        r[i] = u[i];
    std::ofstream output_forward("forward_output.txt");
    for (int t = 1; t <= Nt; t++)
    {
        for (int i = 1; i < n; i++)
        {
            // Discretized diff eq
            u[i] = alpha * r[i - 1] + (1 - 2 * alpha) * r[i] + alpha * r[i + 1];
        }
        double time = t * dt;
        if (t % 100 == 1)
            PrintToFile(u, time, output_forward);
        // note that the boundaries are not changed.
    }
};

void Solver::tridiag(double a, double b, double c, double *u, double *f)
{
    double b_array[n-1];
    double f_t[n-1];
    f[0] -= a * u[0];
    f[n-2] -= a * u[n];
    f_t[0] = f[0];
    b_array[0] = b;
    for (int i = 1; i <= n - 2; i++){
        b_array[i] = b - (a * c) / b_array[i-1];
        f_t[i] = f[i] - (f_t[i - 1] * a) / b_array[i-1];
    }
    // Backward substitution
    u[n-1] = f_t[n-2] / b_array[n-2];
    for (int i = n - 2; i >= 1; i--){
        u[i] = (f_t[i-1] - c * u[i+1])/b_array[i-1];
    }
}

void Solver::backward_euler(double *u, double *f){
    double a, b, c;
    a = c = - alpha;
    b = 1 + 2*alpha;
    std::ofstream output_back("Backward_output.txt");
    for (int t = 1; t <= Nt; t++)
    {
        for (int i = 0; i <= n - 2; i++) f[i] = u[i + 1];
        tridiag(a, b, c, u, f);
        // boundary conditions
        u[0] = 0.0;
        u[n] = 1.0;
        double time = t * dt;
        if (t % 100 == 1)
            PrintToFile(u, time, output_back);
    }
};

void Solver::crank_nicholson(double *u, double *f){
    double a, b, c;
    a = c = -alpha;
    b = 2 + 2 * alpha;
    std::ofstream output_crank("crank_nicholson.txt");
    for (int t = 1; t <= Nt; t++)
    {
        for (int i = 0; i <= n - 2; i++)
        {
            f[i] = alpha * u[i] + (2 - 2 * alpha) * u[i+1] + alpha * u[i + 2];
        }
        tridiag(a, b, c, u, f);
        // boundary conditions
        u[0] = 0.0;
        u[n] = 1.0;
        double time = t * dt;
        if (t % 100 == 1)
            PrintToFile(u, time, output_crank);
    }
}

void Solver::PrintToFile(double *u, double time, std::ofstream &output)
{
    output << time << " ";
    for (int i = 0; i <= n; i++)
    {
        output << u[i] << " ";
    }
    output << endl;
};
