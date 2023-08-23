import numpy as np
import matplotlib.pyplot as plt
from scipy.special import *
import spline

def func(x): #function definition
	return x**(1+jv(0,x))/np.sqrt(1-x+100*x**2-100*x**3)

N = int(input("Enter the number of sampling points in the table:"))
xa = np.linspace(0.1,0.9,N) #support points
ya = func(xa) #func val at support points
y2a = np.zeros(ya.shape) #second derivative array intialization
xx = np.linspace(0.1,0.9,20000) #points for interpolation
yt = func(xx) #true value of func at xx
yy = np.zeros(xx.shape) #interpolated value of func at xx

y2a = spline.notaknot(xa,ya) #takes in xa, ya tabulated values with not-a-knot boundary conditions, see implementation in modspline.f90

print(np.c_[xa,y2a]) #print second derivative values at each support point

plt.figure(1)
plt.plot(xa,ya,'r',xa,y2a,'g')
plt.legend(["ya","y2a"])
plt.grid("True")
plt.show()

yyb = spline.splintn(xa,ya,y2a,xx) #interpolates the func with arguments -- xa, ya i.e., the sample table, second derivative array y2a and array of values at which func has to be interpolated

plt.figure(2)
plt.plot(xa,ya,'ro',xx,yt,'b+',xx,yyb,'k')
plt.legend(["ya","yt","yyb"])
plt.xlim([0,1])
plt.ylim([0,0.3])
plt.grid("True")
plt.show()

plt.figure(3)
plt.semilogy(xx,np.absolute(yt-yyb))
plt.grid("True")
plt.show()
