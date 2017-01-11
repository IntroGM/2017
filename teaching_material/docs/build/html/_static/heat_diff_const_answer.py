#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
import analytical_solutions

### heat_diff_1.py
###
### Script to calculate the finite differences
### solution for the 1D heat diffusion
### problem.
###
### Compared against analytical solution.

#####################
#### Parameters: ####
#####################
rho       = 2800   # density of the rock
Cp        = 800    # heat capacity of the rock
alpha     = 2.5    # heat conductivity of the rock
T_ini     = 1350   # initial temperature of the rock column
T_surface = 0      # boundary condition at the surface
T_bottom  = 1350   # boundary condition at the bottom

L         = 100e3  # height of the rock column, meters
nx        = 6      # number of grid points in space
nt        = 2000   # number of grid points in time
totaltime = 60*60*24*365.25*10e6 # total time to calculate, in seconds
#####################

# Calculate the spacing between grid points
dx = L / (nx-1)
dt = totaltime / (nt-1)

# Initialize an array to hold the results (temperature)
T = np.zeros((nx,nt)) # creates an 2D array where location varies along rows
                      # and time along columns
T[:, 0] = T_ini       # set the initial condition

# Generate an array of depth values for plotting purposes
x = np.linspace(0, L, nx)

# Generate an array of time values for plotting purposes
time = np.linspace(0, totaltime, nt)

# Loop over every time step, always calculating the new temperature 
# at each depth.
# The first (T[0,:]) and last (T[nx,:]) rows are skipped
# since these values are known from the boundary condition.
# The first column (T[:,0]) is also skipped since these 
# values are known from the initial condition
for it in range(1, nt):
	for ix in range(0, nx):
		if ix == 0:
			# This is a surface grid point
			T[ix, it] = T_surface
		elif ix == nx-1:
			# This is the last (spatial) grid point
			# at the bottom of the lithosphere
			T[ix, it] = T_bottom
		else:
			# All the other grid points.
			T[ix, it] = (alpha * (T[ix+1, it-1] - 2*T[ix, it-1] + T[ix-1, it-1]) / dx**2) * dt / (rho*Cp) + T[ix, it-1]




### Calculate analytical solution, at the end of calculations

# We calculate the analytical
# solution at 200 points for plotting.
x_analytical = np.linspace(0, (nx-1)*dx, 200)

# Calculate diffusion
kappa = alpha / (Cp*rho)

# Calculate the analytical solution
T_analytical = analytical_solutions.oceanic_cooling(x_analytical, time[nt-1], alpha, rho, Cp, T_surface, T_bottom)


### Create the plots for numerical and analytical solutions
# Here we only plot the last time step
fig, ax = plt.subplots() 
ax.plot(T[:, nt-1], -x/1e3, '.--')
ax.plot(T_analytical, -x_analytical/1e3, '-')
plt.xlabel("Temperature (C)")
plt.ylabel("Depth (km)")
plt.show()  


