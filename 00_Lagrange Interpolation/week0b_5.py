import os
import numpy as np
import matplotlib.pyplot as PLOT
import math

#for running and executing the C program directly from the Python terminal
os.system("gcc week0b_5.c -o week0b_5.out -lm")
os.system("./week0b_5.out")

x,y = np.loadtxt("./output2.txt", usecols = (0,1), unpack=True)

z = np.sin(x) #defining an array of accurate sine values at the points where interpolated values were calculated
abserr = np.absolute(z-y) #absolute difference between the interpolated values and accurate sine values

PLOT.figure(1)
PLOT.plot(x,z,'g',x,y,'r')
PLOT.title("Cubic Lagrange Interpolated function and sin(x)")
PLOT.legend(["sin(x)", "Interpolated function"])

PLOT.figure(2)
PLOT.semilogy(x,abserr,'m')
PLOT.title("Semilog error")

PLOT.show()
