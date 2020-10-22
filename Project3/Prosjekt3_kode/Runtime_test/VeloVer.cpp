#include <iostream>
#include <vector>
#include <cmath>
#include <armadillo>
#include <time.h>
using namespace std;
using namespace arma;

int main()
{
    double G = 4 * M_PI * M_PI;
    double M_sun = 1.0;
    int N = 1000000;
    vec x(2);
    vec v(2);
    vec a0(2);
    vec a1(2);
    double FinalTime = 50.0;
    double dt = FinalTime / N;
    double r;
    x[0] = 1;
    x[1] = 0;
    v[0] = 0;
    v[1] = 8;
    ofstream ofile;
    ofile.open("posisjonVV.txt");
    ofile << x[0] << "\t" << x[1] << endl; //write initial position to file
    clock_t start, end;
    start = clock();
    for (int i = 0; i < N; i++)
    {
        r = sqrt(x[0] * x[0] + x[1] * x[1]);
        a0[0] = -G * M_sun * x[0] / (r * r * r);
        a0[1] = -G * M_sun * x[1] / (r * r * r);
        x[0] += v[0] * dt + 0.5 * dt * dt * a0[0];
        x[1] += v[1] * dt + 0.5 * dt * dt * a0[1];
        r = sqrt(x[0] * x[0] + x[1] * x[1]);
        a1[0] = -G * M_sun * x[0] / (r * r * r);
        a1[1] = -G * M_sun * x[1] / (r * r * r);
        v[0] += 0.5 * dt * (a0[0] + a1[0]);
        v[1] += 0.5 * dt * (a0[1] + a1[1]);

        ofile << x[0] << "\t" << x[1] << endl;
    }
    ofile.close();
    end = clock();
    double time = ((double)end - (double)start) / CLOCKS_PER_SEC;
    cout << "Time elapsed:"
         << "\t" << time << endl;
    return 0;
}