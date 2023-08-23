#include<stdio.h>
#include<math.h>
#include<stdlib.h>


//Defining the Lagrange interpolation function

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

//MAIN FUNCTION

void main(){

//data input according to sine function and the number of data points
  int k, n;
  float pi = M_PI;
  printf("Enter the number of data points:\n");
  scanf("%d",&n);
  n = n-1;
  float xx[n], yy[n];
  for (k=0; k < n+1 ; k++){
      float inv = k*2*pi/n;
      xx[k] = inv;
      yy[k] = sin(xx[k]);
  }

  float x,y;
  int m;
  FILE *f = fopen("output.txt", "w"); //Choosing the file into which interpolated values have to be written.
  if (f == NULL){ //In case the file cannot be used due to lack of access permission
  printf("Error opening file");
  exit(1);
  }
  /*Loop for calculating interpolated values at 100 uniformly spaced values BETWEEN 0 and 2pi and then writing them into output.txt*/
  #define N 79
  for(m=1; m<=N; m++){
      float inv_o = m*2*pi/(N+1);
      x = inv_o;
      y = lintp(xx,yy,x,n);
      
      fprintf(f,"%f %f\n",x,y);
  }
  fclose(f);
  }
