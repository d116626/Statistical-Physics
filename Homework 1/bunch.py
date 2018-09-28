#!/usr/bin/env python

# Import modules
import time
import math

# Import files
import src.py3_pi_markov as spy3

# Constant

print("Disks \t Points\t Total Point \t Pi \t Error \t Time")

# Number of disk
for nDisk in [10, 50, 100, 500, 1000, 5000, 10000]:
    # Number of point
    for nPoint in [10, 100, 1000, 10000, 100000]:
        # Time
        aTime = time.clock()

        # Call 
        pPidisk = spy3.fpimarkov(nDisk, nPoint)
        
        # mean of all pi
        aPi = sum(pPidisk)/nDisk
        # Error
        aError = math.fabs(math.pi - aPi)
        # Time
        aTime = time.clock() - aTime

        print(nDisk, '\t', nPoint, '\t', nDisk*nPoint, '\t', aPi, '\t', aError, '\t', aTime)