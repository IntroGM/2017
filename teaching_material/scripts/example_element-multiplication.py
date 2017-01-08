#!/usr/bin/bash
import numpy as np
import matplotlib.pyplot as plt


### Example of NumPy element-by-element operations

# Consider function 'f' we want to evaluate between some
# range [xmin,xmax]
#
# For example:
#
#   f = C * x^2 - sin(x)
#
# where C=1.5 is a constant
#
# We are interested on the range x = [0,5]
#

# Define variabls
C = 1.5  # function constant
a = 0    # range min
b = 5    # range max
nx = 7   # at how many points we want to evaluate the function

# First, define x
x = np.linspace(a, b, nx)
# now x will be an array containing 'nx' elements,
# values running from a to b, e.g.
#  x = [0, 0.83, 1.67, 2.5, 3.33, 4.17, 5]
print(" x: ")
print(x)

# Then, evaluate the function itself:
f = C * x**2 - np.sin(x)
print("\n f: ")
print(f)

# Now, 'f' is an array of same length with 'x' and holding
# the values of the function at locations define by f

# Let's plot it
plt.plot(x, f, 'o-')
plt.show()
