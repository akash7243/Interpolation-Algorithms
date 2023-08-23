import numpy as np
import matplotlib.pyplot as plt
from scipy.special import *
from math import *
import spline

def func(x): #function definition
	return x**(1+jv(0,x))/np.sqrt(1-x+100*x**2-100*x**3)

def fd(x): #function derivative
	f1 = (x**(1+jv(0,x)))*(((1+jv(0,x))/x)-(np.log(x)*jv(1,x)))/np.sqrt(1-x+100*x**2-100*x**3)
	f2 = (200*x-1-300*x**2)*x**(1+jv(0,x))/(2*(1+100*x**2-x-100*x**3)**1.5)
	return f1-f2

t = np.arange(100,1500,100)
max_err = np.zeros(t.shape)
for i in t:
	xa = np.linspace(0.1,0.9,int(i)) #support points
	ya = func(xa) #func val at support points
	y2a = np.zeros(ya.shape) #second derivative array intialization
	xx = np.linspace(0.1,0.9,20000) #points for interpolation
	yt = func(xx) #true value of func at xx
	yy = np.zeros(xx.shape) #interpolated value of func at xx

	y2a = spline.spline(xa,ya,fd(0.1),fd(0.9)) #takes in xa, ya tabulated values and fd at boundary ;returns second derivatives at the sampling points

	yyb = spline.splintn(xa,ya,y2a,xx) #interpolates the func with arguments -- xa, ya i.e., the sample table, second derivative array y2a and array of values at which func has to be interpolated
	
	plt.figure(1)
	plt.plot(xx,np.absolute(yt-yyb),label="N=%d"%int(i))
	plt.grid("True")
	l = np.where(t == i)
	max_err[l] = max(abs(yt-yyb))
	
plt.legend()
plt.show()

print(np.c_[0.8/t,max_err])

plt.figure(2)
plt.loglog(0.8/t,max_err)
plt.title("Maximum error varying with spacing")
plt.xlabel("Spacing")
plt.ylabel("Maximum error")
plt.grid("True")
plt.show()

for k in max_err:
	if k < 1e-06:
		print("Spacing for six-digit accuracy is",0.8/t[np.where(max_err == k)],"and the max error is",float(k))
		break
