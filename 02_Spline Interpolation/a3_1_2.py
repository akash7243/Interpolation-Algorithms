import numpy as np
from scipy.special import *
import matplotlib.pyplot as plt

x = np.arange(0.1,0.95,0.05)
y = (x**(1+jv(0,x)))/np.sqrt(1-x+(100*x**2)-(100*x**3))

print(np.c_[x,y])

plt.figure(0)
plt.plot(x,y,'g')
plt.grid("True")
plt.xlabel("Values of x between 0.1 and 0.9")
plt.ylabel("f(x)")
plt.title("Plot of f(x) against x")
plt.show()