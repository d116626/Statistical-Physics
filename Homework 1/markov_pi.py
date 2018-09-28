# -*- coding: utf-8 -*-
from random import uniform
from math import sqrt
import math
def markov_pi(delta, n):
    n_hits=float(0)
    x, y = 1.0, 1.0
    for i in range (n):
        dx, dy = uniform(-delta, delta), uniform(-delta, delta)
        if(abs(x+dx)<1 and abs(y+dy)<1):
          x, y=x+dx, y+dy
        if (x**2 + y**2 <1):
            n_hits += 1
    return n_hits

n=10**3    # total number of points
delta=0.3  # size of the box 
pi, var = 0.0, 0.0

for j in range(20):
   pi = pi + markov_pi(delta,n)*4/n
   var = var + (markov_pi(delta,n)/(n) - math.pi/4)**2
   j+=1
   print pi/(j), sqrt(var/(j))


    
        
                
            
    