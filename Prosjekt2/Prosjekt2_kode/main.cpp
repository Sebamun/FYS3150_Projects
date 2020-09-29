#include "prosjekt2.hpp"

int main(int argc, char const *argv[]) {

    string filename_1 = "Egenverdier1";
    string filename_2 = "Egenverdier2";
    string filename_3 = "Egenvektorer";
    string filename_4 = "Egenvektorer2";

    mat A;
    double max = 1;
    double MaxNonDiag = 5.0E-10;
    double eps = 1.0E-40;
    int p, q;
    double dim = 150;
    mat R = arma::zeros<mat>(dim, dim);
    for (int i = 0; i < dim; i++){
      R(i,i) = 1;
    }
    Initialize(dim, 0, 5, A, 0);
    check(dim, 5, A, filename_1, filename_3);

    clock_t start, end;
    start = clock();

    int  iterations = 0;
    while( max > eps ){
        offdiag(A, p, q, dim, max);
        Jacobi_rotate(A, R, p, q, dim);
        iterations ++;
    }
    check(dim, 1, A, filename_2, filename_4);
    end = clock();
    cout << "Diagonalization took " << iterations << " iterations" << endl;
    cout << scientific << "CPU time (sec) : " << ((double)end - (double)start) / CLOCKS_PER_SEC << endl;
    return 0;
}
