from math import *
from scipy import *
from numpy import *

xx = arange(0.1,0.95,0.05)
yy = sin(pi*xx)/sqrt(1-xx**2)
print("xx,yy")
for i in xx :
	l = where(xx==i)
	print(xx[l],yy[l])
