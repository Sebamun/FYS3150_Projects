#ifndef TRIDIAG_HPP
#define TRIDIAG_HPP
#include <string>
#include <fstream>
#include <ostream>
#include <iostream>
using namespace std;

class Solver
{
private:
    int n, Nt; 
    double L, dx, dt, alpha;

public:;
    Solver(int num_int, int num_time_steps, double time_step, double Length); //, char filename);
    void tridiag(double a, double b, double c, double *u, double *f);
    void PrintToFile(double *u, double time, std::ofstream &output);
    void backward_euler(double *u, double *f);
    void crank_nicholson(double *u, double *f);
    void forward_euler(double *u, double *r);
    void forward_euler2d(double **u, double **r);
    void PrintToFile2d(double **u, double time, std::ofstream &output);
    void specific_forward(double *u,double *r, double W0, double W1, double W2, double W3, double c_p, double kappa, double rho);
};
#endif //TRIDIAG_HPP