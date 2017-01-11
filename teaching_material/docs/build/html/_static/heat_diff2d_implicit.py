#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
np.set_printoptions(precision=9, suppress=True, linewidth=240)

### heat_diff_simple_implicit.py
# 
# Calculate ONE time step with the implicit finite differences method
# for the heat equation in 2D

# Physical parameters
alpha = 4.0
rho = 3300
Cp = 1250
H = 1e-6

# Grid spacing
dx = 10e3
dy = 10e3
dt = 1e5 * (60*60*24*365.25)
nt = 100

# Surface conditions 
T_surf = 0.0
T_bott = 500.0
T_left = 0.0
T_right = 0.0
T_ini = 500.0

# Number of spatial grid points
nx = 7
ny = 8

# Create temperature array for known T, at current time step
T = np.ones((nx,ny)) * T_ini

# Number of equations formed
neq = nx*ny     # one equation for each grid point

# Create empty coefficient matrix and right-hand-side vector
M = np.zeros((neq, neq))
rhs = np.zeros(neq)


for it in range(nt):

	# Constants for the coefficient matrix
	A = -alpha/dx**2
	B = 2*alpha/dx**2 + 2*alpha/dy**2 + rho*Cp/dt
	C = -alpha/dy**2

	# Fill in the values in M and rhs
	# This loops over all the grid points (for ix; for iy loops)
	for ix in range(nx):
		for iy in range(ny):

			# Calculate the global index of the 
			# grid point we are about to  calculate
			gidx = ix * ny + iy

			if iy == 0:
				# Uppermost grid point, surface
				M[gidx, ix*ny + iy] = 1.0
				rhs[gidx] = T_surf
			elif iy == ny-1:
				# Lowermost grid point, bottom
				M[gidx, ix*ny + iy] = 1.0
				rhs[gidx] = T_bott
			elif ix == 0:
				# Leftmost boundary
				M[gidx, ix*ny + iy] = 1.0
				rhs[gidx] = T_left
			elif ix == nx-1:
				# Rightmost boundary
				M[gidx, ix*ny + iy] = 1.0
				rhs[gidx] = T_right
			else:
				# Grid points that are not at boundaries
				M[gidx, (ix-1)*ny +  iy   ] = A
				M[gidx, (ix+1)*ny +  iy   ] = A
				M[gidx,     ix*ny +  iy   ] = B
				M[gidx,     ix*ny + (iy-1)] = C
				M[gidx,     ix*ny + (iy+1)] = C
				rhs[gidx] = H + T[ix, iy] * rho * Cp / dt

	# Solve the system of equations
	Tnew = np.linalg.solve(M, rhs)

	# Tnew will come out as one vector, we will reshape it back to nx-ny -size
	Tnew = Tnew.reshape((nx,ny))

	# Replace the old solution (T) with the new solution Tnew
	T = np.copy(Tnew)

# Plot the array
plt.imshow(Tnew.T, extent=(0, ny*dy/1e3, nx*dx/1e3, 0), interpolation='nearest', cmap=cm.viridis, aspect='auto')
plt.colorbar()
plt.show()
