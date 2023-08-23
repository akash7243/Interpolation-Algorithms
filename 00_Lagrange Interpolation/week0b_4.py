import os
import numpy as np
import matplotlib.pyplot as PLOT
import math

#for running and executing the C program directly from the Python terminal
os.system("gcc week0b_3.c -o week0b_3.out -lm")
os.system("./week0b_3.out")

x,y = np.loadtxt("./output.txt", usecols = (0,1), unpack=True)

z = np.sin(x) #defining an array of accurate sine values at the points where interpolated values were calculated
err = (z-y) #difference between the interpolated values and accurate sine values 
abserr = np.absolute(z-y) #absolute error

print(np.amax(abserr))

PLOT.figure(1)
PLOT.plot(x,z,'g',x,y,'r')
PLOT.title("Interpolated function and sin(x)")
PLOT.legend(["sin(x)", "Interpolated function"])

PLOT.figure(2)
PLOT.semilogy(x,abserr,'m')
PLOT.grid('True')
PLOT.title("Semilog error")

PLOT.show()
