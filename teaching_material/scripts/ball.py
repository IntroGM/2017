z = 1.8     # Starting elevation
Vz = 15     # Initial vertical velocity
nt = 6      # In how many steps we do the calculation
tottime = 3 # Total time (s) to calculate
            # The total time and the number of time steps
	    # together implicitly set the size of the time step, dt.

dt = tottime / nt
print ("Size of one time step is:", dt, "seconds")

print ("Time, elevation:")
for it in range(nt):
   t = it * dt
   z = (Vz - 0.5 * 9.81 * t**2) * dt + z
   print(t+dt, z)
