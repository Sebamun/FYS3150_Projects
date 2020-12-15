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
};
#endif //TRIDIAG_HPP