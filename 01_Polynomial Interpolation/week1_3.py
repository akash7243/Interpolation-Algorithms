from scipy import *
from matplotlib.pyplot import *
from numpy import *
import polint as p


#locate 'm+1' number of points nearest to the value of x
#m is order of interpolation
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
	return max(0,min(j-((m-2)//2),n-m)); #return index of the leftmost point in set of neighbors

n = 30
m = int(input("Enter the order of interpolation:"))
xx = linspace(0,1,n)
yy = sin(xx+(xx**2))
x = linspace(-0.5,1.5,200)
j = 0 #intiliazing j,k,y,dy 
k = 0
y = zeros(200)
dy = zeros(200)
for i in x: #initialize loop for x values
	l = where(x==i)
	k = locate(xx,n,x,j,m) #using locate function define above
	xn = xx[k:k+m+1] #xn is the set of support points nearest to the specific value of x
	yn = yy[k:k+m+1] #set of support ordinates
	y[l] = [p.polint(xn,yn,i)[0]] #store polint o/p in y
	dy[l] = [p.polint(xn,yn,i)[1]] #store estimated error in dy

#plotting estimated and true error on a semilog scale in Y-axis
figure(1)
semilogy(x,abs(array(dy)),'r',x,abs(array(sin(x+(x**2))-y)),'go')
grid("True")
title("Estimated and True error for m = 20")
legend(["Estimated Error","True Error"])
show()
