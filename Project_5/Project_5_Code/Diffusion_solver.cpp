#include <ostream>
#include "Diffusion_solver.hpp"
using namespace std;


Solver::Solver(int num_int, int num_time_steps, double time_step, double Length)
{
    int n = num_int;
    double L = Length;
    double dx = L/(n+1);
    double dt = time_step;
    int Nt = num_time_steps;
    double alpha = dt/dx/dx;
    //char filename = filename; 
};


void Solver::tridiag(double a, double b, double c, double *u, double *f)
{
    double a_array[n - 1]; //= new double[n - 1];
    double b_array[n - 1]; //= new double[n - 1];
    double c_array[n - 1]; // = new double[n - 1];
    for (int i = 1; i < n; i++)
    {
        a_array[i] = a;
        b_array[i] = b;
        c_array[i] = c;
    }
    for (int i = 1; i < n; i++)
    {
        u[i] = 0.0;
    }
    u[n] = 1.0;
    u[0] = 0.0; u[n] = 1.0;
    for (int i = 2; i < n; i++){
        b_array[i] = b_array[i] - (a_array[i] * c_array[i-1]) / b_array[i-1];
    }
    // Forward substitution
    for (int i = 2; i < n; i++){
        f[i] = f[i] + (f[i - 1] * a_array[i]) / b_array[i - 1];
    }
    // Backward substitution
    u[n] = f[n] / b_array[n];
    for (int i = n - 2; i > 0; i--){
        u[i] = (f[i-1] - c_array[i-1] * u[i+1])/b_array[i-1];
    }
        }
    for (int i = 1; i < n; i++)
    {
        u[i] = 0.0;
    }
    u[n] = 1.0;
    u[0] = 0.0; u[n] = 1.0;
    /*
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
    */
}

void Solver::backward_euler(){
    double a, b, c;
    double u[n + 1]; // This is u of Au = f
    double f[n + 1]; // Right side of matrix equation Au=f, the solution at a previous step
    a = c = - alpha;
    b = 1 + alpha*2;
    double count = 0;
    for (int t = 1; t <= dt; t++)
    {
        // here we solve the tridiagonal linear set of equations,
        // see chapter 6
        tridiag(a, b, c, u, f);
        // boundary conditions
        u[0] = 0;
        u[n] = 1;
        // replace previous time solution with new
        double time = t*dt;
        while( count < 11){
            if (count == 10){
                PrintToFile(u, time);
                count = 0;
            }
            else{
                count += 1;
            }
        }
        for (int i = 0; i <= n; i++)
        {
            f[i] = u[i];
        }
    }
};

void Solver::PrintToFile(double *u, double time){
    std::ofstream output_file("Backward_output.txt");
    output_file << time << std::endl;
    for ( int i; i < n; i++){
        output_file << u[i] << std::endl;
        }
};
