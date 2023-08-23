#include<stdio.h>
#include<math.h>


//Lagrange interpolation function

float li(int i, int n, float xx[n],float x){
  int j;
  float prod = 1;
  for (j=0; j <= n ; j++){
    if (j!=i)
      prod = prod* (x - xx[j])/(xx[i]-xx[j]);
  }
  return prod;
}

float lintp (float *xx, float *yy, float x, int n){
  float sum=0;
  int i;
  for (i=0; i<=n; i++){
    sum = sum + li(i,n,xx,x)*yy[i];
  }
  return sum;
}

void main(){
  int k, n;
  double pi = M_PI;
  printf("Enter the number of data points:\n");
  scanf("%d",&n);
  n = n-1;
  float xx[n], yy[n];
  for (k=0; k < n+1 ; k++){
      double inv = k*2*pi/n;
      xx[k] = inv;
      yy[k] = sin(xx[k]);
  }
  
  float x;
  printf("Enter the value of x for which you want the interpolated value of the given function:\n");
  scanf("%f", &x);
  printf("The interpolated value is %f\n",lintp(xx,yy,x,n));
  }
  
