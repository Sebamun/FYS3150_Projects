#include "prosjekt2.hpp"
int main(int argc, char const *argv[]) {
    // Her henter vi filene vi skal lese til:
    string runtime = "Output";
    string filename_1 = "Egenverdier";
    string filename_2 = "Egenverdier_2";
    string filename_3 = "Egenvektorer";
    string filename_4 = "Egenvektorer_2";
    // Definerer variabler:
    double dim = atof(argv[1]); // Her hentes stoorelsen på matrisen.
    int quant = atoi(argv[2]); // Her bestemmes det om vi skal ha kvantedel med. 
    mat A;
    double max = 1;
    double MaxNonDiag = 5.0E-10;
    double eps = 1.0E-15;
    int p, q;
    mat R = arma::zeros<mat>(dim, dim);
    for (int i = 0; i < dim; i++){
      R(i,i) = 1;
    }

    Initialize(dim, 0, 5, A, quant);
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
    double time = ((double)end - (double)start) / CLOCKS_PER_SEC;
    ofstream ofile;
    ofile.open(runtime);
    ofile<<iterations<<setw(15)<<time<<endl;
    ofile.close();
    return 0;
}
