#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
from printarr import printarr

### heat_diff_implicit.py
###
### Script to calculate the finite differences
### solution for the 1D heat diffusion & production
### problem with varying physical properties.
### 
### Implicit.

# Convenience parameters
SECINYR = 60*60*24*365.25
SECINMYR = 1e6*SECINYR

#####################################
#### Define the model parameters ####
#####################################
nt = 2  # num of timesteps
nx = 5  # num of (spatial) grid points
totaltime = 100*SECINMYR # total time to run
L = 100e3 # size of the model (lithosphere thickness)

T_surf = 0     # boundary condition, surface
T_bott = 1350  # boundary condition, bottom
T_ini  = 1350  # initial temperature

# Generate the main grids
x = np.linspace(0, L, nx)
t = np.linspace(0, totaltime, nt)
dx = L/(nx-1)
dt = totaltime/(nt-1)

# Generate the "mid-point" grid for heat conductivity values 
# between the main grid points. 
x_mp = x + 0.5*dx

# Set the (constant) physical parameters
rho = 3300
Cp = 1250
H = 0.1e-6
alpha = 2.5

# Generate the array to hold the temperature field
# and initialize it with the initial condition
T = np.ones(nx) * T_ini  # holds T for current time step
T_old = np.zeros(nx)     # holds T for the previous time step


# Create the matrix and the right hand side vector
# for solution of the linear system of equations
nf = nx     # degrees of freedom, i.e. number of unknowns (i.e. number of equations)
M = np.zeros((nf, nf))
rhs = np.zeros(nf)


for it in range(nt):
	# New time step, copy the current time step to be
	# the previous one
	T_old = np.copy(T)

	M[:, :] = 0

	# Generate the left hand side matrix for the system fo equations
	# Note that if physical fields are kept constant from one time
	# step to the next one, this only needs to be done once.
	# Here we do it every time step.
	for ix in range(1, nx-1):
		# Set the matrix coefficients for the inner nodes
		M[ix, ix-1] = -alpha/dx**2
		M[ix, ix  ] = rho*Cp/dt + alpha/dx**2 + alpha/dx**2
		M[ix, ix+1] = -alpha/dx**2
		rhs[ix] = T_old[ix] * rho * Cp / dt + H

	# ... and then for boundaries:
	# (Dividing by dx**2 here is done to make the matrix coefficients
	# to be in the same order of magnitude with those of inner nodes,
	# which makes printing prettier...)
	ix = 0
	M[ix, ix] = 1 / dx**2
	rhs[ix] = T_surf / dx**2

	ix = nx-1 
	M[ix, ix] = 1 / dx**2
	rhs[ix] = T_bott / dx**2

	# Uncomment to print the final matrix:
	printarr(M)

	# Solve the system of equations
	res = np.linalg.solve(M, rhs)

	# Copy the solution to the temperature array
	T[:] = res[:]
	
# Plot the last and second to last time steps
plt.plot(T, -x, '.--')
plt.plot(T, -x, '.-')
plt.show()
