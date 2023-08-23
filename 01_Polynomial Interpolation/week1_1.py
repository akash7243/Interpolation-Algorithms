from scipy import *
from matplotlib.pyplot import *
from numpy import *

#import the polint module which performs polynomial interpolation
import polint as p 

xx = linspace(0,1,5) 
yy = sin(xx+(xx**2))
x = linspace(-0.5,1.5,200) #interpolate these values
y = [p.polint(xx,yy,w)[0] for w in x] #storing interpolated values in an array
dy = [p.polint(xx,yy,w)[1] for w in x] #storing estimated error in an arra

#plotting interpolated values and the true function in the Figure 1
figure(1)
plot(xx,yy,'ro',x,y,'r',x,sin(x+(x**2)),'g')
grid("True")
title("Interpolating sin(xx+(xx^2))")
legend(["Table values","Interpolated values","True Function"])

#plotting estimated and true error on a semilog scale in Y-axis
figure(2)
semilogy(x,abs(array(dy)),'r',x,(array(sin(x+(x**2))-y)),'g')
grid("True")
title("Estimated and True error")
legend(["Estimated Error","True Error"])
show()
