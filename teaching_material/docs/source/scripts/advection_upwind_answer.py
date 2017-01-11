#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
from math import pi

# Solve 1D Eulerian advection problem
# with upwind differences

nx = 50  # how many spatial grid points
dx = 0.01 # grid spacing

vx = 1.0   # advection velocity

nt = 40 # how many time steps to take
dt = 0.25 * dx / vx

# Generate spatial grid
x = np.linspace(0, dx*nx, nx)

# Generate (temporal) grid
t = np.linspace(0, dt*nt, nt)

# Generate initial field
f_ini = np.zeros((nx))
idx = (x > 0.2*x[-1])
f_ini[idx] = 1

# Take boundary conditions directly from the initial field
f_0 = f_ini[0]

# Generate a grid to hold the values of the field at
# every time step
f = np.empty((nx, nt))

# Copy the initial field to the array
f[:, 0] = f_ini[:]

# Fill in all boundary values (at x = 0) from the boundary condition
f[0, :] = f_0

# Start advection calculation
for it in range(1, nt):
   for ix in range(1, nx):
      f[ix, it] = -vx * dt * (f[ix, it-1] - f[ix-1, it-1]) / dx + f[ix, it-1]

   ## Instead of the "for ix" loop one can do that on one line:
   # f[it, 1:nx] = -vx * dt * (f[it-1, 1:nx] - f[it-1, 0:(nx-1)]) / dx + f[it-1, 1:nx]


# Plot some results
# Here we plot at time steps 0, 2, 19, and 39.
# Modify these as needed.
for it in [0, 2, 19, 39]:
   plt.plot(x, f[:, it], 'o-')

frange = np.max(f) - np.min(f)
axes = plt.gca()
axes.set_ylim([np.min(f)-0.1*frange, np.max(f)+0.1*frange])
plt.show()

