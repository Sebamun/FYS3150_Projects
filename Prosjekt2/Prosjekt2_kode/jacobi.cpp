#include "prosjekt2.hpp"

int Initialize(int Dim, double Rmin, double Rmax, mat& U)
{
    int i, j;
    double Step, DiagConst, NondiagConst;
    U = zeros<mat>(Dim, Dim);
    // Integration step length
    Step = Rmax / Dim;
    DiagConst = 2.0 / (Step * Step);
    NondiagConst = -1.0 / (Step * Step);

    // Setting up tridiagonal matrix and diagonalization using Armadillo
    U(0, 0) = DiagConst;
    U(0, 1) = NondiagConst;
    for (i = 1; i < Dim - 1; i++)
    {
        U(i, i - 1) = NondiagConst;
        U(i, i) = DiagConst;
        U(i, i + 1) = NondiagConst;
    }
    U(Dim - 1, Dim - 2) = NondiagConst;
    U(Dim - 1, Dim - 1) = DiagConst;

    return 0;

}

int check(int Dim, double Rmax, mat& U, string filename){
    // diagonalize and obtain eigenvalues
    double Step, DiagConst, NondiagConst;
    Step = Rmax / Dim;
    DiagConst = 2.0 / (Step * Step);
    NondiagConst = -1.0 / (Step * Step);
    vec Eigval(Dim);
    eig_sym(Eigval, U);
    double pi = acos(-1.0);
    // Her skriver jeg til fil:
    ofstream ofile;
    ofile.open(filename);
    ofile << "Results" << endl;
    ofile << "-------"<<endl;


    ofile << setiosflags(ios::showpoint | ios::uppercase);
    //ofile <<  setw(15) << setprecision(8) << "relative error=" << RelativeError << endl;
    ofile << "Number of Eigenvalues = " << setw(15) << Dim << endl;
    ofile << endl;
    ofile << "Exact:" << setw(25) << "Numerical:" << setw(45) << "Exact versus numerical eigenvalues:" << endl;
    cout << scientific << endl; 
    for (int i = 0; i < Dim; i++)
    {
        double Exact = DiagConst + 2 * NondiagConst * cos((i + 1) * pi / (Dim + 1));
        ofile << setprecision(8) << Exact << setw(21) << Eigval[i] << setw(24) << fabs(Eigval[i] - Exact) << endl;
    }

    ofile.close();
    return 0;
} //  end of main function

/*

int Jacobi_solver(int n, double eps, mat& U){
    cout.precision(5);
    double aip = 0, aiq = 0, vpi = 0, vqi = 0;
    double tau = 0, t = 0, s = 0, c = 0; //tan(theta), sin(theta), cos(theta)
    int count = 1;                       //count of iterations
    int count_old = count - 10;          //keep track of every 10th iteration
    int p = n - 1, q = n - 2;            //off diag all same value to start
                                         //pick last as first maximum
    clock_t start, end;

    if (n <= 10)
    {
        cout << "Before diagonalization" << endl;
        print_vals(a, v, n, conv);
        cout << endl;
    }

    double app = a(p, p);
    double aqq = a(q, q);
    double apq = a(p, q);

    start = clock();

    while (abs(apq) > conv)
    {
        if (count > 1)
        {
            apq = 0;
            find_max(a, p, q, apq, n);
        }

        //calculate sin(theta) and cos(theta)
        aqq = a(q, q);
        app = a(p, p);
        tau = (aqq - app) / (2 * apq);
        if (tau > 0)
            t = 1 / (tau + sqrt(1 + tau * tau));
        else
            t = -1 / (-tau + sqrt(1 + tau * tau));
        c = 1 / sqrt(1 + t * t);
        s = c * t;

        //calculate new matrix elements and vectors
        for (int i = 0; i < n; i++)
        {
            if (i != p && i != q)
            {
                aip = a(i, p);
                aiq = a(i, q);
                a(i, p) = aip * c - aiq * s;
                a(p, i) = aip * c - aiq * s;
                a(i, q) = aiq * c + aip * s;
                a(q, i) = aiq * c + aip * s;
            }
            //vpi=v(p,i);
            //vqi=v(q,i);
            vpi = v(i, p);
            vqi = v(i, q);
            //v(p,i)=c*vpi-s*vqi;
            // v(q,i)=c*vqi+s*vpi;
            v(i, p) = c * vpi - s * vqi;
            v(i, q) = c * vqi + s * vpi;
        }
        a(p, p) = app * c * c - 2 * apq * c * s + aqq * s * s;
        a(q, q) = app * s * s + 2 * apq * c * s + aqq * c * c;
        a(p, q) = 0;
        a(q, p) = 0;

        count++;
    }

    end = clock();

    if (n <= 10)
    {
        cout << "After diagonalization" << endl;
        print_vals(a, v, n, conv);
        cout << endl;
    }

    cout << "Diagonalization took " << count << " iterations" << endl;
    cout << scientific << "CPU time (sec) : " << ((double)end - (double)start) / CLOCKS_PER_SEC << endl;

    return 0;
}
}
*/
