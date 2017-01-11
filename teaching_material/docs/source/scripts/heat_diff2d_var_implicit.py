#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
np.set_printoptions(precision=9, suppress=True, linewidth=240)

### heat_diff2d_var_implicit.py
# 
# 2D heat equation with variable heat conductivity
# Implicit.

# Grid 
Lx = 100e3
Ly = 100e3
nx = 23
ny = 22
totaltime = 10e6 * (60*60*24*365.25)
nt = 100

# Surface conditions 
T_surf = 0.0
T_bott = 500.0
T_left = 0.0
T_right = 0.0
T_ini = 500.0



# Calculate dt, dx, dy
dx = Lx / (nx-1)
dy = Ly / (ny-1)
dt = totaltime / (nt-1)


# Create x and y for the grid point locations
x = np.zeros((nx, ny))
y = np.zeros((nx, ny))
x_mp = np.zeros((nx, ny))  # staggered grid in x dir
y_mp = np.zeros((nx, ny))  # staggered grid in y dir

for ix in range(nx):
	x[ix, :] = ix*dx
	x_mp[ix, :] = ix*dx + 0.5*dx

for iy in range(ny):
	y[:, iy] = iy*dy
	y_mp[:, iy] = iy*dy + 0.5*dy

# Create temperature array for known T, at current time step
T = np.ones((nx,ny)) * T_ini


#### PHYSICAL PARAMETERS
# Fill in heat conductivity values
alphax = np.ones((nx, ny)) * 4.0   # defined at x_mp, y
alphay = np.ones((nx, ny)) * 4.0   # defined at x, y_mp
alphax[y < 50e3] = 3.0
alphay[y_mp < 50e3] = 3.0

# Heat production, capacity, density
rho = np.ones((nx, ny)) * 3300
Cp = np.ones((nx, ny)) * 1250
H = np.ones((nx, ny)) * 0.0

# Change H at leftern half of the model
H[x < 50e3] = 1e-6


# Number of equations formed
neq = nx*ny     # one equation for each grid point

# Create empty coefficient matrix and right-hand-side vector
M = np.zeros((neq, neq))
rhs = np.zeros(neq)


for it in range(nt):
	print(it)

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
				M[gidx, (ix-1)*ny +  iy   ] = -alphax[ix,   iy  ] / dx**2
				M[gidx, (ix+1)*ny +  iy   ] = -alphax[ix-1, iy  ] / dx**2
				M[gidx,     ix*ny +  iy   ] = alphax[ix, iy] / dx**2 + alphax[ix-1, iy] / dx**2 + alphay[ix, iy] / dy**2 + alphay[ix, iy-1] / dy**2 + rho[ix,iy]*Cp[ix,iy]/dt
				M[gidx,     ix*ny + (iy-1)] = -alphay[ix,   iy  ] / dy**2
				M[gidx,     ix*ny + (iy+1)] = -alphay[ix,   iy-1] / dy**2
				rhs[gidx] = H[ix,iy] + T[ix, iy] * rho[ix,iy] * Cp[ix,iy] / dt

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
