import math as m
import numpy as np

x = np.arange(0.1,0.95,0.05)
xbar = float(input("Enter xbar"))
n = int(input("Enter order of interpolation"))
dif = [xbar-i for i in x]
prod = 1
for w in dif:
	prod = prod*w

err = abs(((m.factorial(2*n))*(m.pi*prod))/((m.factorial(n+1))*(m.factorial(n))*(2**((2*n)+1.5))))

print(err)

