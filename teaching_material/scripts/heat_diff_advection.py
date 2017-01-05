#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erf

### heat_diff_2.py
###
### Script to calculate the finite differences
### solution for the 1D heat diffusion & advection
### problem.
###
### Physical properties are kept constant.



#####################
#### Parameters: ####
#####################
T_ini     = 1350   # initial temperature of the rock column
T_surface = 0      # boundary condition at the surface
T_bottom  = 1350   # boundary condition at the bottom

L         = 100e3  # height of the rock column, meters
nx        = 10     # number of grid points in space
nt        = 200     # number of grid points in time
totaltime = 60*60*24*365.25*100e6 # total time to calculate, in seconds

rho    = 2800
Cp     = 800
alpha  = 2.5
H      = 2.5e-6

vx     = -300 / (60*60*24*365.25*1e6)  # advection velocity
                                       #  ~ erosion speed


# Generate an array of depth values 
x = np.linspace(0, L, nx)
dx = L / (nx-1)

# Calculate the spacing between time steps
dt = totaltime / (nt-1)

# Initialize an array to hold the results (temperature)
T = np.zeros((nx,nt)) # creates an 2D array where location varies along rows
                      # and time along columns
T[:, 0] = T_ini       # set the initial condition
T[0, :] = T_surface   # set the upper boundary condition
T[nx-1, :] = T_bottom # set the lower boundary condition

# Generate an array of time values for plotting purposes
time = np.zeros(nt)
time[0] = 0

# Loop over every time step, always calculating the new temperature 
# at each depth, and then advecting the temperature field.
for it in range(1, nt):

	# First, calculate heat diffusion
	for ix in range(1, nx-1):
		T[ix, it] = (  (  alpha * (T[ix+1, it-1] - 2*T[ix, it-1] + T[ix-1, it-1]) ) / dx**2 + H ) * dt / (rho * Cp) + T[ix, it-1]

	# Then, calculate heat advection. Note that we now use the 
	# recently calculated temperature values from this time step
	# instead of the values from previous time step. 
	T_dif = np.copy(T[:, it])  # temperature after diffusion, before advection
	for ix in range(1, nx):
		T[ix, it] = -vx * (T_dif[ix] - T_dif[ix-1]) / dx + T_dif[ix]

	# Calculate the time in seconds at this timestep
	time[it] = time[it-1] + dt



### Create the plot,
# here we only plot the last time step
fig, ax = plt.subplots() 
ax.plot(T[:, nt-1], -x/1e3, '.--')
plt.xlabel("Temperature (C)")
plt.ylabel("Depth (km)")
plt.show()  


