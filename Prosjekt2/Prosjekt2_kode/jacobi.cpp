#include "prosjekt2.hpp"
int Initialize(int Dim, double Rmin, double Rmax, mat& A, int quantum)
{
    // Definerer variabler:
    int i, j; // Iterasjonselementene.
    double Step, DiagConst, NondiagConst, h, omega, ledd, q;
    A = zeros<mat>(Dim, Dim); // Matrise av nuller som vi skal fylle opp.
    Step = Rmax / Dim; // Stegene i itereringen.
    DiagConst = 2.0 / (Step * Step); // Diagonalelementene.
    NondiagConst = -1.0 / (Step * Step); // Elementene som ikke ligger på diagonalen.
    omega = 0.5; // Styrken av oscilator potensialet.
    h = Step; // Steglengde.
    // Her bestemmer man om vi skal ha med kvantedelen i utregningene:
    if (quantum==1){
      q = 1.0; // Kvantetilfellet.
    }
    else{
      q = 0.0; // Ikke- kvantetilfellet.
    }
    // Finner initialverdiene for matrisen:
    A(0, 0) = DiagConst;
    A(0, 1) = NondiagConst;
    for (i = 1; i < Dim - 1; i++)
    {
        A(i, i - 1) = NondiagConst;
        A(i, i) = DiagConst + q*(omega * omega * (i*h) * (i*h) + (1.0/(i*h)));
        A(i, i + 1) = NondiagConst;
    }
    A(Dim - 1, Dim - 2) = NondiagConst;
    A(Dim - 1, Dim - 1) = DiagConst + q*(omega * omega * (i*h) * (i*h) + (1.0/(i*h)));
    return 0;
}
int check(int Dim, double Rmax, mat& A, string filename, string filename2){
    // Diagonaliser og finn egenverdier:
    double Step, DiagConst, NondiagConst; // Variabler.
    Step = Rmax / Dim; // Steglengde.
    DiagConst = 2.0 / (Step * Step); // Diagonalelementene.
    NondiagConst = -1.0 / (Step * Step); // Ikke diagonalelementene
    vec Eigval(Dim); // Egenverdiene lagret.
    mat Eigvec; // Egenvektorene lagret.
    eig_sym(Eigval, Eigvec, A); // Finner egenverdier/egenvektorer.
    double pi = acos(-1.0);
    // Her skriver vi til fil:
    ofstream ofile;
    ofile.open(filename); // Åpner filen.
    ofile << "Results" << endl;
    ofile << "-------"<<endl;
    ofile << setiosflags(ios::showpoint | ios::uppercase);
    ofile << "Number of Eigenvalues = " << setw(15) << Dim << endl;
    ofile << endl;
    ofile << "Exact:" << setw(25) << "Numerical:" << setw(45) << "Exact versus numerical eigenvalues:" << endl;
    ofile << scientific << endl;
    for (int i = 0; i < Dim; i++) // Skriver ut egenverdiene til fil:
    {
        double Exact = DiagConst + 2 * NondiagConst * cos((i + 1) * pi / (Dim + 1));
        ofile << setprecision(8) << Exact << setw(21) << Eigval[i] << setw(24) << fabs(Eigval[i] - Exact) << endl;;
    }
    ofile.close();
    ofile.open(filename2);
    ofile << Eigvec.col(0) << endl; // Skriver egenvektoren med den minste egenverdien til fil.
    ofile.close();
    return 0;
}
// Finner elementene som ikke ligger på diagonalen:
int offdiag(mat A, int &p, int &q, int n, double& max){
    max = 0.0; // Finner verdier som er stoorre enn dette.
    for (int i = 0; i < n; ++i)
    {
        for (int j = i + 1; j < n; ++j)
        {
            double aij = fabs(A(i, j)); // Absoluttverdi for etthvert matriseelement.
            if (aij > max) // Hvis denne verdien er større enn 0.0:
            {
                max = aij; // Ny grense for den stoorste verdien.
                p = i; // Indeksen til denne verdien.
                q = j; // Indeksen til denne verdien.
            }
        }
    }
    return 0;
}

void Jacobi_rotate(mat& A, mat &R, int k, int l, int n)
{
    double s, c;
    if (A(k, l) != 0.0) // Her setter vi inn indeks fra offdiag.
    {
        double t, tau;
        tau = (A(l, l) - A(k, k)) / (2 * A(k, l));
        if (tau >= 0)
        {
            t = 1.0 / (tau + sqrt(1.0 + tau * tau));
        }
        else
        {
            t = -1.0 / (-tau + sqrt(1.0 + tau * tau));
        }
        c = 1 / sqrt(1 + t * t);
        s = c * t;
    }
    else
    {
        c = 1.0;
        s = 0.0;
    }
    double a_kk, a_ll, a_ik, a_il, r_ik, r_il;
    a_kk = A(k, k);
    a_ll = A(l, l);
    A(k, k) = c * c * a_kk - 2.0 * c * s * A(k, l) + s * s * a_ll;
    A(l, l) = s * s * a_kk + 2.0 * c * s * A(k, l) + c * c * a_ll;
    A(k, l) = 0.0; // Hardkoder ikke diagonal elementene for haand.
    A(l, k) = 0.0; // Vi gjoor det samme her.
    for (int i = 0; i < n; i++)
    {
        if (i != k && i != l)
        {
            a_ik = A(i, k);
            a_il = A(i, l);
            A(i, k) = c * a_ik - s * a_il;
            A(k, i) = A(i, k);
            A(i, l) = c * a_il + s * a_ik;
            A(l, i) = A(i, l);
        }
        // Her legger vi til de nye egenvektorene:
        r_ik = R(i, k);
        r_il = R(i, l);
        R(i, k) = c * r_ik - s * r_il;
        R(i, l) = c * r_il + s * r_ik;
    }
    return;
}
