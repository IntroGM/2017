#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
from math import pi

### falling_sphere.py
###
### Script to calculate the finite differences
### solution for the falling sphere in a viscous fluid
### (Stokes' law).
###
### Compared against analytical solution.

#####################
#### Parameters: ####
#####################
rho_f = 1000   # density of the fluid (kg m^-3)
rho_s = 7750   # density of the sphere (kg m^-3)

R = 0.02       # radius of the sphere (m)
eta = 100      # viscosity of the fluid (Pa s)

nt = 5        # how many timesteps to calculate (-)

z_ini = 0.0    # initial location of the sphere (m)
dt = 0.0020    # size of timestep used (s)
g = 9.81       # acceleration of gravity (m s^-2)
#####################


# Initialize an array to hold the results (sphere elevation)
# The first values is the initial elevation, rest are calculated
z = np.zeros(nt)
z[0] = z_ini

# generate array of times in seconds
time = np.zeros(nt)
time[0] = 0

# calculate sphere volume
V = (4/3)*pi*R**3

# calculate buoyancy
Fb = V*rho_f*g

# calculate sphere mass
m = V*rho_s

# calculate gravitational force
Fg = -m*g

# to shorten the expressions
A = -6 * pi * eta * R

# Loop over every time step, always calculating the new elevation
# based on the two previous elevation values. 
# Skip the first value which is directly given by the initial condition.
for it in range(1, nt):
	if it == 1:
		# z_{-1} is replaced by z_{1} in the discretized 
		# equation since we don't know value for z_{-1}
		# This is the zero velocity boundary (initial) condition
		z[it] = (Fb + Fg - z[it-1] * (-2*m/dt**2) - z[it] * (m/dt**2 + A/(2*dt))) / (m/dt**2 - A/(2*dt))
	else:
		# At timesteps it>1 we do know two previous values,
		# z[it-1] and z[it-2] so we use the normal discretized equation
		# to calculate the next value z[it+1]
		z[it] = (Fb + Fg - z[it-1] * (-2*m/dt**2) - z[it-2] * (m/dt**2 + A/(2*dt))) / (m/dt**2 - A/(2*dt))

	# Calculate the time in seconds at this timestep
	time[it] = time[it-1] + dt



### Calculate analytical solution
# See course material for the derivation.

# Calculate constants using initial conditions
# z = z_ini at t = 0
# v = dz/dt = 0 at t = 0

# Initialize arrays to hold the time values
# for the analytical solution. We calculate the analytical
# solution at 200 points for plotting.
t_analytical = np.linspace(0, (nt-1)*dt, 200)

# Coefficients of the differential equation
B1 = 6*pi*eta*R/m
B2 = (Fb+Fg)/m

# Here we can calculate all the points at once using NumPy's 
# element-by-element array multiplication 
z_analytical = (B2/B1)*(t_analytical + (1/B1)*np.exp(-B1*t_analytical) + (B1*z_ini/B2) - 1/B1)


# Create the plots for numerical and analytical solutions
fig, ax = plt.subplots() 
ax.plot(time*1000, 1000*z, '.--')
ax.plot(t_analytical*1000, 1000*z_analytical, '-')
plt.xlabel("Time (ms)")
plt.ylabel("z (mm)")
plt.show()  


