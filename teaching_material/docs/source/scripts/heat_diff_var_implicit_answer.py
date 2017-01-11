#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
np.set_printoptions(precision=9, suppress=True, linewidth=120)


### heat_diff_var_implicit.py
###
### Script to calculate the finite differences
### solution for the 1D heat diffusion & production
### problem with variable physical properties.
### 
### Implicit.

# Convenience parameters
SECINYR = 60*60*24*365.25
SECINMYR = 1e6*SECINYR

#####################################
#### Define the model parameters ####
#####################################
nt = 4  # num of timesteps
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
x_mp = x + 0.5*dx   # i.e. add half-a-dx to each grid point



### Generate the arrays to hold the physical parameters
rho = np.empty(nx)   # density at main grid (kg/m3)
Cp = np.empty(nx)    # heat capacity at main grid (J/kgK)
H = np.empty(nx)     # heat production at main grid (W/m3)
alpha = np.empty(nx) # heat conductivity at mid-point grid (W/mK)

# Fill in the values, two layer lithosphere:
#  crust:   0- 35 km
#  mantle: 35-100 km
idx_crust = x < 35e3
idx_mantle = x > 35e3

rho[idx_crust] = 2800
rho[idx_mantle] = 3300
Cp[idx_crust] = 800
Cp[idx_mantle] = 1250
H[idx_crust] = 2.0e-6
H[idx_mantle] = 0.02e-6

idx_crust_mp = x_mp < 35e3
idx_mantle_mp = x_mp > 35e3

alpha[idx_crust] = 2.5
alpha[idx_mantle] = 2.5



# Generate the array to hold the temperature field
# and initialize it with the initial condition
T = np.zeros((nx, nt))
# Set temperature to T_ini in all spatial nodes at first time step (it==0)
T[:, 0] = T_ini


# Create the matrix and the right hand side vector
# for solution of the linear system of equations
nf = nx     # degrees of freedom, i.e. number of unknowns (i.e. number of equations)
M = np.zeros((nf, nf))
rhs = np.zeros(nf)

# Loop over the time steps, skipping the first one which is defined by initial condition
for it in range(1,nt):

	# Generate the left hand side matrix for the system fo equations
	# Note that if physical fields are kept constant from one time
	# step to the next one, this only needs to be done once.
	# Here we do it every time step.
	M[:, :] = 0 # set all values to zero
	for ix in range(1, nx-1):
		# Set the matrix coefficients for the inner nodes.

		# We are calculating a value for node ix, so the 
		# first index (the row of the matrix) is ix.
		# The second index (the column of the matrix)
		# is the index of the T to which the coefficient 
		# belongs to
		
		M[ix, ix-1] = -alpha[ix-1]/dx**2
		M[ix, ix  ] = rho[ix]*Cp[ix]/dt + alpha[ix]/dx**2 + alpha[ix-1]/dx**2
		M[ix, ix+1] = -alpha[ix]/dx**2


		# The right-hand side vector needs to be updated
		# every time step since it contains values
		# that change from time step to time step (T[ix, it-1]).
		
		# Calculate the value of the right-hand side vector:
		rhs[ix] = T[ix, it-1] * rho[ix] * Cp[ix] / dt + H[ix]

	# Set the matrix coefficients for the the boundaries:
	ix = 0
	M[ix, ix] = 1 
	rhs[ix] = T_surf     

	ix = nx-1 
	M[ix, ix] = 1 
	rhs[ix] = T_bott    

	# Print the coefficient matrix
	print("Time step", it, ", coefficient matrix M is:")
	print(M, "\n")

	# Solve the system of equations
	Tnew = np.linalg.solve(M, rhs)

	# Copy the solution to the temperature array
	T[:, it] = Tnew[:]
	
# Plot the last time steps
plt.plot(T[:, nt-1], -x, '.--')
plt.show()

