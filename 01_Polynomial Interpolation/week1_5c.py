from scipy import *
from matplotlib.pyplot import *
from numpy import *

#import the polint module which performs polynomial interpolation
import polint as p 

#locate 'm+1' number of points nearest to the value of x
#m is order of interpolation
#return index of the leftmost point in set of neighbors
def locate(xx,n,x,j,m): 
	jl = 0
	ju = n-1
	m+=1
	while ju-jl > 1:
		jm = (ju+jl)//2
		if x[l] >= xx[jm]:
			jl = jm
		else:
			ju = jm
	if x[l] == xx[0]:
		j = 0
	elif x[l] == xx[n-1]:
		j = n-1
	else:
		j = jl
	return max(0,min(j-((m-2)//2),n-m)); 

m = int(input("Enter the order of interpolation:"))
xx = arange(0.1,0.95,0.05)
yy = sin(pi*xx)/sqrt(1-xx**2)
x = linspace(0.1,0.9,1000)
j = 0 #intiliazing j,k,y,dy 
k = 0
y = zeros(1000)
dy = zeros(1000)
for i in x: #initialize loop for x values
	l = where(x==i)
	k = locate(xx,17,x,j,m) #using locate function define above
	xn = xx[k:k+m+1] #xn is the set of support points nearest to the specific value of x
	yn = yy[k:k+m+1] #set of support ordinates
	y[l] = [p.polint(xn,yn,i)[0]] #store polint o/p in y
	dy[l] = [p.polint(xn,yn,i)[1]] #store estimated error in dy

print(amax(dy))
#plotting estimated and true error on a semilog scale in Y-axis
figure(1)
semilogy(x,abs(array(dy)),'r',x,abs(array(sin(pi*x)/sqrt(1-x**2)-y)),'g')
title("Estimated and True error for m = 16")
grid("True")
legend(["Estimated Error","True Error"])
show()

