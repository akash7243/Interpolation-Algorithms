#include<stdio.h>
#include<math.h>
#include<stdlib.h>

static int imaxarg1, imaxarg2;
#define IMAX(a,b) (imaxarg1 = (a), imaxarg2 = (b), (imaxarg1) > (imaxarg2) ? (imaxarg1) : (imaxarg2))

static int iminarg1, iminarg2;
#define IMIN(a,b) (iminarg1 = (a), iminarg2 = (b), (iminarg1) < (iminarg2) ? (iminarg1) : (iminarg2))

float li(int i, int n, float xx[n+1],float x){
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

int binary(float xx[], unsigned long n, float x, unsigned long *j){
unsigned long ju, jm, jl;
int ascnd;
int mm = 4;
jl = 0;
ju= n;
ascnd = (xx[n] >= xx[0]);
while (ju-jl > 1) {
	jm = (ju+jl)>>1;
	if (x>= xx[jm] == ascnd)
		jl = jm;
	else
		ju = jm;
}
if(x==xx[0]) *j = 0;
else if(x==xx[n]) *j = n;
else *j = jl;
return IMAX(0,IMIN(n+1-mm,jl-((mm-2)>>1)));
}

void main(){
  int k, n;
  double pi = M_PI;
  unsigned long *j;
  printf("Enter the number of data points:\n");
  scanf("%d",&n);
  n = n-1;
  float xx[n], yy[n];
  for (k=0; k < n+1 ; k++){
      double inv = k*2*pi/n;
      xx[k] = inv;
      yy[k] = sin(xx[k]);
  }
  
  float x,y;
  int m;
  FILE *f = fopen("output2.txt", "w");
  if (f == NULL){
  printf("Error opening file");
  exit(1);
  }
    for(m=1; m<=79; m++){
      double inv_o = m*2*pi/80;
      x = inv_o;
      int o = binary(xx,n,x,j);
      y = lintp(&xx[o],&yy[o],x,4);
      fprintf(f,"%f %f\n",x,y);
    }
    fclose(f);
  }

