#!/usr/bin/python3

import numpy as np
from scipy.special import erf

def oceanic_cooling(x, time, alpha, rho, Cp, Tsurf, Tbott):
	# Calculates the analytical solution for the cooling of the
	# oceanic lithosphere -problem. Assumes surface to be
	# at z=0.
	# Pass in values:
	#  - x: locations (m) to evaluate the function at
	#  - time: time (s) at which to evaluate the solution
	#  - alpha, rho, Cp: (constant) physical parameters
	#  - Tsurf, Tbott: surface and bottom temperatures (K)

	thdiff = alpha / (rho * Cp)

	# Calculate the analytical solution
	T = (Tbott - Tsurf)*erf((x-x[0]) / (2*np.sqrt(thdiff*time))) + Tsurf

	return T

