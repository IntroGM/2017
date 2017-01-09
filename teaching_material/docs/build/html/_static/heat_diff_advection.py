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
SECINMYR  = 60*60*24*365.25*1e6  # constant: seconds in one million year

T_surface = 0      # boundary condition at the surface
T_bottom  = 1350   # boundary condition at the bottom
                   # Initial temperature will be a linear
		   # gradient between these two

L         = 100e3  # height of the rock column, meters
nx        = 10     # number of grid points in space
nt        = 100     # number of grid points in time
totaltime = 100*SECINMYR # total time to calculate, in seconds

rho    = 2800
Cp     = 800
alpha  = 2.5
H      = 0 #2.5e-6

vx     = -400 / SECINMYR  # advection velocity, m/s
                          #  ~ erosion speed

# Generate an array of depth values 
x = np.linspace(0, L, nx)
dx = L / (nx-1)

# Calculate the spacing between time steps
dt = totaltime / (nt-1)

# 
try:
	maxdt_diff = 0.5 * dx**2 / (alpha/(rho*Cp))
except:
	maxdt_diff = np.inf
try:
	maxdt_adv  = dx / np.abs(vx)
except:
	maxdt_adv = np.inf

if maxdt_diff > maxdt_adv:
	maxdt_reason = "adv"
else: 
	maxdt_reason = "diff"
maxdt = 0.5 * np.min((maxdt_diff, maxdt_adv))
print("Maxdt:", maxdt/SECINMYR, "; dt:", dt/SECINMYR, "||", maxdt_reason)

# Initialize an array to hold the results (temperature)
T = np.zeros(nx)   
Tprev = np.copy(T)  # this will hold the temperature of 
                    # the previous time step

# Calculate the initial condition
T_ini = T_surface + x * (T_bottom-T_surface)/L        

# Set it to be the first temperature field
T[:] = T_ini[:]

# Generate an array of time values for plotting purposes
time = np.zeros(nt)
time[0] = 0

# Loop over every time step, always calculating the new temperature 
# at each depth, and then advecting the temperature field.
for it in range(1, nt):
	# Copy current temperature to previous time step's values
	Tprev[:] = T[:]

	# Set boundary values
	T[0] = T_surface
	T[nx-1] = T_bottom

	# Calculate internal nodes
	for ix in range(1, nx-1):
		T[ix] = ( ( alpha * (Tprev[ix+1] - 2*Tprev[ix] + Tprev[ix-1]) ) / dx**2 + H ) * dt / (rho * Cp) - vx * (Tprev[ix] - Tprev[ix-1]) * dt / (dx) + Tprev[ix] 

	# Calculate the time in seconds at this timestep
	time[it] = time[it-1] + dt


# Calculate analytical solution
kappa = alpha/(rho*Cp)
B1 = -vx/kappa
B2 = -H/kappa
if T_surface != 0:
	raise Exception("analytical solution not valid")
C12 = (T_bottom - B2*L/B1) / (1/B1 - np.exp(-B1*L)/B1)
C3 = C12 / B1
x_analytical = np.linspace(0, L, 200)
T_analytical = B2*x_analytical/B1 + C3 - C12*np.exp(-B1*x_analytical)/B1

### Create the plot,
# here we only plot the last time step
fig, ax = plt.subplots() 
ax.plot(T, -x/1e3, '.--r')
ax.plot(T_ini, -x/1e3, '.--g')
ax.plot(T_analytical, -x_analytical/1e3, '-r')
plt.xlabel("Temperature (C)")
plt.ylabel("Depth (km)")
plt.show()  


