#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

# Solve 1D Eulerian advection problem
# with upwind differences


# Define problem parameters
L = 10   # Problem size. Since the edge starts at x=1
         # we want to leave some space on the right
	 # where the edge can advect

# Define here: the number of grid points, number of time steps
# total time to run the model, advection velocity, boundary condition value
...

# Calculate dx and dt based on the definitions above
...

# Generate array 'x' to hold the locations of the grid points
# Hint: function np.linspace
...

# Generate array 't' to hold the time values at each time step
...

# Generate two arrays:
#  'f' to hold the field values at current time step
#  'f_prev' to hold the field values of the previous time step
# Hint: functions np.zeros or np.empty
...

# Set the current field values in 'f' to correspond to the 
# initial field
# Hint: you can use a condition (e.g. "x < 1") as an index for an array
...

# This will copy the first (initial) field to another variable
# so that we can use it at the end to compare the final time step
# to the first time step. This is not needed in any of the calculations.
# This needs no editing.
f_orig = np.copy(f)


#### The main loop comes here:

# Create a loop that loops over all time steps
# Within the time loop, create another loop that goes over
# all grid points from 1 to nx

for ...

   # Every time step, copy the current field 'f' values
   # to the previous field 'f_prev'
   ...

   for ...
      # Here calculate the new function value at each grid point
      # based on the previous field values from f_prev
      ...

### End of main loop, last time step reached

# Do plotting:
# This plots the last time step calculated
plt.plot(x, f_orig, '.-g')
plt.plot(x, f, '.-g')
frange = np.max(f) - np.min(f)
axes = plt.gca()
axes.set_ylim([np.min(f)-0.1*frange, np.max(f)+0.1*frange])
plt.show()

