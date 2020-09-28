#include "prosjekt2.hpp"

int main() {
    mat A;
    double max = 1;
    double MaxNonDiag = 5.0E-10;
    double eps = 1.0E-15;
    int p, q;
    double dim = 10;
    mat R = arma::zeros<mat>(dim, dim);
    Initialize(dim, 0, 1, A);
    check(dim, 1, A);
    int  iterations = 0;
    while( max > eps ){
        offdiag(A, p, q, dim, max);
        Jacobi_rotate(A, R, p, q, dim);
        iterations ++;
    }
    check(dim, 1, A);
    cout << iterations << endl;
    return 0;
}
