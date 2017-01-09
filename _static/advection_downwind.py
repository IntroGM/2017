#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
from math import pi

# Solve 1D Eulerian advection problem
# with downwind differences

nx = 50  # how many spatial grid points
dx = 0.01 # grid spacing

vx = 1.0   # advection velocity

nt = 40 # how many time steps to take
dt = 0.01 * dx / vx

x = np.linspace(0, dx*nx, nx)

# Generate (temporal) grid
t = np.linspace(0, dt*nt, nt)

# Generate initial field
f_ini = np.zeros((nx))
idx = (x < 0.4*x[-1]) & (x > 0.2*x[-1])
f_ini[idx] = 1

# Take boundary conditions directly from the initial field
f_0 = f_ini[nx-1]

# Generate a grid to hold the values of the field at
# every time step
f = np.empty((nt, nx))

# Copy the initial field to the array
f[0, :] = f_ini[:]

# Fill in all boundary values (at x = x_max) from the boundary condition
f[:, nx-1] = f_0

# Start advection calculation
for it in range(0, nt-1):
   for ix in range(0, nx-1):
      f[it+1, ix] = -vx * dt * (f[it, ix+1] - f[it, ix]) / dx + f[it, ix]

   ## Instead of the "for ix" loop one can do that on one line:
   # f[it+1, 0:(nx-1)] = -vx * dt * (f[it, 1:nx] - f[it, 0:(nx-1)]) / dx + f[it, 0:(nx-1)]


# Plot some results
for it in [0, 20, nt-1]:
   plt.plot(x, f[it, :], '.-')
plt.show()

