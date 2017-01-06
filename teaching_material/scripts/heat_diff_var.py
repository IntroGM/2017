#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erf

### heat_diff_2.py
###
### Script to calculate the finite differences
### solution for the 1D heat diffusion & production
### problem.
###
### Uses a staggered grid:
###  |                 |
###  O--z--O--z--O--z--O--z
###  |                 |
###     -----> x
### 
###  O: T, rho, Cp, H
###  z: alpha, (q)



#####################
#### Parameters: ####
#####################
T_ini     = 1350   # initial temperature of the rock column
T_surface = 0      # boundary condition at the surface
T_bottom  = 1350   # boundary condition at the bottom

L         = 100e3  # height of the rock column, meters
nx        = 10     # number of grid points in space
nt        = 10    # number of grid points in time
totaltime = 60*60*24*365.25*10e6 # total time to calculate, in seconds
#########################################
#### Arrays for physical parameters: ####
#########################################
rho = np.zeros(nx)   # density, kg/m3
Cp = np.zeros(nx)    # heat capacity, J/kgK
alpha = np.zeros(nx) # heat conductivity, W/mK
H = np.zeros(nx)     # heat production rate, W/m3

# Generate an array of depth values for the main grid
x = np.linspace(0, L, nx)
dx = L / (nx-1)
# ... and for the "mid-point" grid. Note that the last
# grid point of this grid will be outside our problem
# and will be ignored in the calculations
x_mp = x + 0.5*dx

# Create a two-layer model: crust < 35 km, mantle > 35 km
idx_crust = x < 35e3
idx_mantle = x >= 35e3

# Set the values
rho[idx_crust] = 2800
rho[idx_mantle] = 3300

Cp[idx_crust] = 800
Cp[idx_mantle] = 1250

H[idx_crust] = 2.5e-6
H[idx_mantle] = 0.02e-6

idx_crust = x_mp < 35e3
idx_mantle = x_mp >= 35e3

alpha[idx_crust] = 2.5
alpha[idx_mantle] = 4.0
#########################################


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
# at each depth
# The first (T[0,:]) and last (T[nx,:]) rows are skipped
# since these values are known from the boundary condition.
# The first columnt (T[:,0]) is also skipped since these 
# values are known from the initial condition
for it in range(1, nt):
	for ix in range(1, nx-1):
		T[ix, it] = 

	# Calculate the time in seconds at this timestep
	time[it] = time[it-1] + dt



### Create the plot,
# here we only plot the last time step
fig, ax = plt.subplots() 
ax.plot(T[:, nt-1], -x/1e3, '.--')
plt.xlabel("Temperature (C)")
plt.ylabel("Depth (km)")
plt.show()  


