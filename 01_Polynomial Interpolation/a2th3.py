from math import *
from pylab import *

import polint as p 

#locate 'm+1' number of points nearest to the value of x
#m is order of interpolation
def locate(xx,n,x,j,s):
	jl = 0
	ju = n-1
	s+=1
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
	return max(0,min(j-((s-2)//2),n-s)); #return index of the leftmost point in set of neighbors

t = int(input("Enter the value of t in sintx"))
m_max = int(input("Enter the maximum order of interpolation:")) #enter order above 3
xx = linspace(0,10,m_max+1)
yy = sin(t*xx)
x = linspace(0,10,1000)
j = 0 #initializing j,k,y,dy
k = 0
y = zeros(1000)
dy = zeros(1000)
m = arange(3,m_max+1) #array storing order starting from 3 to max order
maxest_err = zeros(m_max-2) #initializing max estimated and true error arrays
maxtru_err = zeros(m_max-2)
for s in m: #for loop for using different order of interpolation
	for i in x:
		l = where(x==i)
		k = locate(xx,10,x,j,s)
		xn = xx[k:k+s+1]
		yn = yy[k:k+s+1]
		y[l] = [p.polint(xn,yn,i)[0]]
		dy[l] = [p.polint(xn,yn,i)[1]]
	maxest_err[s-3] = amax(abs(array(dy))) #offset by 3 since order starts from 3
	maxtru_err[s-3] = amax(abs(array(sin(t*x)-y)))

print("Order of interpolation at which maximum error is least is",argmin(maxest_err)+3,"and the error is",amin(maxest_err))
#plotting maximum estimated and maximum true error vs. m
figure(1)
semilogy(m,maxest_err,'r',m,maxtru_err,'g')
title("Variation of error with respect to order of interpolation")
grid("True")
xlabel("Order of interpolation")
ylabel("Maximum error")
legend(["Maximum Estimated Error","Maximum True Error"])
	
show()
