#include <ostream>
#include <iostream>
#include <math.h>
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
    std::ofstream output_forward("Output/forward_output.txt");
    for (int t = 1; t <= Nt; t++)
    {
        for (int i = 0; i <= n; i++)
            r[i] = u[i];
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

void Solver::forward_euler2d(double **u, double **r)
{
    std::ofstream output_2d("Output/2d_output.txt");
    for (int t = 1; t <= Nt; t++)
    {
        for (int i = 0; i <= n; i++)
        {
            for (int j = 0; j <= n; j++)
            {
                r[i][j] = u[i][j];
            }
        }
        for (int i = 1; i < n; i++)
        {
            for (int j = 1; j < n; j++)
            {
                u[i][j] = alpha * (r[i + 1][j] + r[i - 1][j] + r[i][j + 1] + r[i][j - 1] - 4 * r[i][j]) + r[i][j];
            }
        }
        double time = t * dt;
        if (t % 10 == 1)
            PrintToFile2d(u, time, output_2d);
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
};

void Solver::backward_euler(double *u, double *f){
    double a, b, c;
    a = c = - alpha;
    b = 1 + 2*alpha;
    std::ofstream output_back("Output/Backward_output.txt");
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
    std::ofstream output_crank("Output/crank_nicholson.txt");
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
};

void Solver::PrintToFile(double *u, double time, std::ofstream &output)
{
    output << time << " ";
    for (int i = 0; i <= n; i++)
    {
        output << u[i] << " ";
    }
    output << endl;
};

void Solver::PrintToFile2d(double **u, double time, std::ofstream &output){
    output << time << " ";
    for (int i = 0; i <= n; i++)
    {
        for (int j = 0; j <= n; j++){
            output << u[i][j] << " ";
        }
        
    }
    output << endl;
};

double W(double t, double W0)
{
    return W0 * (0.4 * pow(0.5, t / (1e5) / 4.47) + 0.4 * pow(0.5, t / (1e5) / 14.0) + 0.2 * pow(0.5, t / (1e5) / 1.25));
}

void Solver::specific_forward(double *u, double *r, double W0, double W1, double W2, double W3, double c_p, double kappa, double rho)
{
    std::ofstream output_lith("Output/lithosphere_data.txt");
    double alpha_new = alpha; 
    for (int t = 1; t <= Nt; t++)
    {
        for (int i = 0; i <= n; i++){
            r[i] = u[i];
        }
        for (int i = 1; i < n; i++)
        {
            u[i] = alpha_new * r[i - 1] + (1 - 2 * alpha_new) * r[i] + alpha_new * r[i + 1];
            if(i*dx < 1/6){
                u[i] += dt * W1 / c_p / rho; 
            }
            else if(1/6 < i * dx && i * dx < 1/3){
                u[i] += dt * W2 / c_p / rho; 
            }
            else if((i * dx) > 1/3){
                u[i] += dt * W3 / c_p / rho; 
                if (t > 1e5)
                {
                    u[i] += dt * W(t, W0) / c_p / rho;
                 }
            }
        }
        double time = t * dt;
        if (t % 100 == 1)
            PrintToFile(u, time, output_lith);
    }
};

