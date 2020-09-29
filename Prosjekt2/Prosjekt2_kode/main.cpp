#include "prosjekt2.hpp"

int main(int argc, char const *argv[]) {
    string filename_1 = argv[1];
    string filename_2 = argv[2];
    string filename_3 = "Egenvektorer";
    string filename_4 = "Egenvektorer_2";
    mat A;
    double max = 1;
    double MaxNonDiag = 5.0E-10;
    double eps = 1.0E-15;
    int p, q;
    double dim = 100;
    mat R = arma::zeros<mat>(dim, dim);
    for (int i = 0; i < dim; i++){
      R(i,i) = 1;
    }
    Initialize(dim, 0, 1, A);
    check(dim, 1, A, filename_1, filename_3);

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
