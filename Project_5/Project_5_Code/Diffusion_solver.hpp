#ifndef TRIDIAG_HPP
#define TRIDIAG_HPP
#include <string>
#include <fstream>
using namespace std;

class Solver
{
private:
    int n, Nt; 
    double L, dx, dt, alpha;

public:;
    Solver(int num_int, int num_time_steps, double time_step, double Length); //, char filename);
    void tridiag(double a, double b, double c, double *u, double *f);
    void PrintToFile(double *u, double time);
    void backward_euler(double *u, double *f);
};
#endif //TRIDIAG_HPP