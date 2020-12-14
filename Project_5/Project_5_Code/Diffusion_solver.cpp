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
    //char filename = filename; 
};


void Solver::tridiag(double a, double b, double c, double *u, double *f)
{
    u[0] = 0.0; u[n] = 1.0;
    for (int i = 2; i < n; i++){
        b = b - (a * c) / b;
    }
    // Forward substitution
    for (int i = 2; i < n; i++){
        f[i] = f[i] + (f[i - 1] * a) / b;
    }
    // Backward substitution
    u[n] = f[n] / b;
    for (int i = n - 2; i > 0; i--){
        u[i] = (f[i-1] - c * u[i+1])/b;
    }
}

void Solver::backward_euler(){
    cout << "Backward called" << endl;

    double a, b, c;
    double u[n + 1]; // This is u of Au = f
    double f[n + 1]; // Right side of matrix equation Au=f, the solution at a previous step
    a = c = - alpha;
    b = 1 + alpha*2;
    for (int i = 0; i < n; i++)
    {
        u[i] = 0.0;
    }
    u[n] = 1.0;
    for (int t = 1; t <= Nt; t++)
    {
        tridiag(a, b, c, u, f);
        // boundary conditions
        u[0] = 0;
        u[n] = 1;
        // replace previous time solution with new
        double time = t*dt;
        if (t%10 == 1)
            PrintToFile(f, time);

        for (int i = 0; i <= n; i++)
        {
            f[i] = u[i];
        }
    }
};

void Solver::PrintToFile(double *u, double time){
    std::ofstream output_file("Backward_output.txt");
    output_file << time << std::endl;
    for ( int i = 0; i <= n; i++){
        output_file << u[i] << std::endl;
        }
};
