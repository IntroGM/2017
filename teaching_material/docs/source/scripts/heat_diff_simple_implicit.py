#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
from printarr import printarr
np.set_printoptions(precision=9, suppress=True, linewidth=120)

### heat_diff_simple_implicit.py
# 
# Calculate ONE time step with the implicit finite differences method
# for the heat equation

# Physical parameters
alpha = 4.0
rho = 3300
Cp = 1250
H = 1e-6

# Grid spacing
dx = 10e3
dt = 1e6 * (60*60*24*365.25)

# Surface conditions 
T_surf = 0.0
T_bott = 500.0
T_ini = 500.0

# Number of spatial grid points
nx = 4

# Create temperature vector for known T, at current time step
T = np.ones(nx) * T_ini

# Constants for the coefficient matrix
A = -alpha/dx**2
B = rho*Cp/dt + 2*alpha/dx**2

# Number of equations formed
neq = nx     # one equation for each grid point

# Create empty coefficient matrix and right-hand-side vector
M = np.zeros((neq, neq))
rhs = np.zeros(neq)

# Fill in the values in M and rhs
for ix in range(nx):
	ieq = ix   # Equation number equals grid number
	if ix == 0:
		# Uppermost grid point, surface
		M[ieq, ieq] = 1.0
		rhs[ieq] = T_surf
	elif ix == nx-1:
		# Lowermost grid point, surface
		M[ieq, ieq] = 1.0
		rhs[ieq] = T_bott
	else:
		# Grid points that are not at boundaries
		M[ieq, ieq-1] = A
		M[ieq, ieq] = B
		M[ieq, ieq+1] = A

# Solve the system of equations
Tnew = np.linalg.solve(M, rhs)

