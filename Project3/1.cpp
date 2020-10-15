#include <iostream>
#include<cmath>
#include <vector>

using namespace std;

double G = 6.94e-11;
double M_sun = 1.98e30;
int N = 10;
double dt = 0.1;




void Euler(double G, double M_sun, int N, double dt){


  double a[N][2];
  double v[N][2];
  double r[N][2];
  double t[N];

  v[0] = {1,0};



  int i;
  for(i=0;i<N;i++){
    for (int j=0;j<2;j++){
      a[i+1][j+1] = G*M_sun/pow(r[i][j],r[i][j]);
      v[i+1][j+1] = v[i][j]+a[i+1][j+1]*dt;
      r[i+1][j+1] = r[i][j] + v[i+1][j+1]*dt;
      t[i+1] = t[i] + dt;
    //cout << r[i][j] << endl;
    }
  }
  cout << r[i] << endl;
  //return r[i][j]

}


void Verlet(double G, double M_sun, int N, double dt){
  double a[N][N];
  double v[N][N];
  double r[N][N];
  double t[N];

  //double a ={0,0};


  int i;
  for(i=0;i<N;i++){
    for (int j=0;j<N;j++){
      a[i+1][j+1] = G*M_sun/pow(r[i][j],r[i][j]);
      v[i+1][j+1] = v[i][j] + (a[i][j]+a[i+1][j+1])*dt*0.5;
      r[i+1][j+1] = r[i][j] + v[i][j]*dt + a[i][j]*dt*dt*0.5;




    }
  }

}

int main(int argc, char const *argv[]) {
  Euler(G,M_sun,N,dt);
  return 0;
}
