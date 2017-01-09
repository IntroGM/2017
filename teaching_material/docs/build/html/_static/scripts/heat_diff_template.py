#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erf

### heat_diff_template.py

### Assign values for physical parameters
Cp = 1250
rho = ...
...

### Assign values for boundary and initial conditions
T_ini = 1350
T_surf = ...
...

### Assign values needed to define the grid
L = 100e3      # problem size in meters
nx = ...       # number of grid points in space
tottime = ...  # total simulation time, in seconds

### Calculate other required parameters
dt = ...       # calculate time step size based on nx and tottime
dx = ...       # calculate grid spacing based on problem size and grid spacing

### Create an 2-dimensional array to hold the calculated temperature 
### values. No editing needed here.
#   
# Once the array is created, you can refer to temperature value at 
# grid point 3 on time step 2 using expression T[2, 3], i.e. time step 
# is the first index, (spatial) grid point the second index. 
# 'np.zeros' is a NumPy function that creates the array and sets all the 
# values to zero initially.
T = np.zeros((nx, nt))

### Initialize all the grid points of the first time step with the initial
### temperature value. No editing needed here.
for ix in range(nx):
	T[ix 0] = T_ini

### Generate an array that holds the time (in seconds) for
### each time step. This is need for plotting purposes.
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

### Generate a similar array to hold the physical locations
### of the grid points. No editing needed here.
x = np.arange(0, nx) * dx

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
	T[it, 0] = ...
	T[it, nx-1] = ...

	# Calculate the other grid points:
	for ix in range(1, nx-1):
		# Calculate the new temperature at time step 'it'
		# based on the previous time step 'it-1':
		T[it, ix] = ...


### Calculate analytical solution for the problem given
### in the lecture notes. If you change the physical parameters
### this won't be valid any more. In that case, modify the
### analytical solution below or change 'do_analytical' to False
### No other editing needed here.
do_analytical = True

if do_analytical:
	x_analytical = np.linspace(0, 100e3, 200)
	kappa = 2.5 / (1250 * 3300)
	T_analytical = 1350*erf(x_analytical / (2*np.sqrt(kappa*time[nt-1])))


### Create the plots for numerical and possible analytical solutions
### Here we plot the last time step calculated. No editing needed here.
plt.plot(T[nt-1, :], -x/1e3, '.--')
if do_analytical:
	plt.plot(T_analytical, -x_analytical/1e3, '-')
plt.xlabel("Temperature (C)")
plt.ylabel("Depth (km)")
plt.show()  


