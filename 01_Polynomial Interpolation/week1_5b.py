from math import *
from scipy import *
from numpy import *
from matplotlib.pyplot import *

xx = linspace(0.1,0.9,200)
yy = sin(pi*xx)/sqrt(1-xx**2)

figure(1)
plot(xx,yy,'g')
title("f(x) in [0.1,0.9]")
show()
