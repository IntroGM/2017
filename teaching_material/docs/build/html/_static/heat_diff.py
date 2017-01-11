#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erf
import analytical_solutions

### heat_diff_template.py

### Assign values for physical parameters
Cp = 1250
rho = ...   # EDITME
alpha = ... # EDITME
H = ...     # EDITME

### Assign values for boundary and initial conditions
T_ini = 1350 
T_surf = ...  # EDITME 
T_bott = ...  # EDITME

### Assign values needed to define the grid
L = 100e3      # problem size in meters
nx = ...       # EDITME number of grid points in space 
tottime = ...  # EDITME total simulation time, in seconds
nt = ...       # EDITME number of time steps to take

### Calculate other required parameters
dt = tottime / (nt - 1)  # calculate time step size based on nx and tottime
dx = ...                 # EDITME calculate grid spacing based on problem size 
                         # and grid spacing

### Create an 2-dimensional array to hold the calculated temperature 
### values. No editing needed here.
#   
# Once the array is created, you can refer to temperature value at 
# grid point 3 on time step 2 using expression T[3, 2], i.e. location index
# is the first index, time step the second index. 
# 'np.zeros' is a NumPy function that creates the array and sets all the 
# values to zero initially.
T = np.zeros((nx, nt))

### Initialize all the grid points of the first time step with the initial
### temperature value. No editing needed here.
for ix in range(nx):
	T[ix, 0] = T_ini

### Generate an array that holds the time (in seconds) for
### each time step. This is needed for plotting purposes.
###
### 'np.arange(a, b)' is a NumPy function that generates
### a 1D array with values from a to b, i.e.
###    [ a, a+1, a+2, ..., b ]
###
### Multiplying this by a constant ('dt' here) will
### multiply each array element separately (element-by-element
### multiplication).
###    => [ a*dt, (a+1)*dt, (a+2)*dt, ..., b*dt ]
###
### No editing needed here.
time = np.arange(0, nt) * dt

### Generate a similar array using similar expression
### to hold the physical locations of the grid points. 
x = ...  # EDITME

### The main time stepping loop:
### Loop over every time step, always calculating the new temperature
### at each spatial grid point, based on the values from the previous
### time step.
###
### The first time step is skipped, since that is the initial
### condition.
###
### The first and last spatial grid points are also skipped, since
### those values cannot be calculated but are instead given by
### the boundary condition.
for it in range(1, nt):
	# Set the temperature at the boundaries
	T[0, it] = ...      # EDITME
	T[nx-1, it] = ...   # EDITME

	# Calculate the other grid points:
	for ix in range(1, nx-1):
		# Calculate the new temperature at time step 'it'
		# based on the previous time step 'it-1':
		T[ix, it] = ...  # EDITME


### Calculate analytical solution for the problem given
### in the lecture notes. If you change the physical parameters
### this won't be valid any more. In that case, modify the
### analytical solution below or change 'do_analytical' to False
### No other editing needed here.
do_analytical = True

if do_analytical:
	x_analytical = np.linspace(0, 100e3, 200)
	T_analytical = analytical_solutions.oceanic_cooling(x_analytical, time[nt-1], alpha, rho, Cp, T_surf, T_bott)


### Create the plots for numerical and possible analytical solutions
### Here we plot the last time step calculated. No editing needed here.
plt.plot(T[:, nt-1], -x/1e3, '.--')
if do_analytical:
	plt.plot(T_analytical, -x_analytical/1e3, '-')
plt.xlabel("Temperature (C)")
plt.ylabel("Depth (km)")
plt.show()  


