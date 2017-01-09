#!/usr/bin/python3

import sys
import numpy as np

def printarr(A):
   maxorder = np.log10(np.max(np.abs(A[A!=0])))
   divider = int(np.ceil(maxorder))

   if len(A.shape) == 1:
      for ix in range(A.shape[0]):
         sys.stdout.write("{:^8d}".format(ix))
      sys.stdout.write("\n")
      for ix in range(A.shape[0]):
         sys.stdout.write("{:>8.5f} ".format(A[ix]/10**divider))
   elif len(A.shape) == 2:
      sys.stdout.write("{:^8}".format(" "))
      for ix in range(A.shape[0]):
         sys.stdout.write("{:^8d}".format(ix))
      sys.stdout.write("\n")
      for iy in range(A.shape[1]):
         sys.stdout.write("{:>8d}".format(iy))
         for ix in range(A.shape[0]):
            sys.stdout.write("{:>8.5f}".format(A[iy,ix]/10**divider))
         sys.stdout.write("\n")
   else:
      raise Exception("printarr(): Cannot print arrays with dimensions > 2")

   print(" x 10^{}".format(divider))
