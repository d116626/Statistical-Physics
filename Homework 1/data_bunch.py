from random import uniform
from math import sqrt
import math
def markov_pi_data(delta, n):
    data_sum=float(0)
    
    x, y = 1.0, 1.0
    for i in range (n):
        dx, dy = uniform(-delta, delta), uniform(-delta, delta)
        if(abs(x+dx)<1 and abs(y+dy)<1):
          x, y=x+dx, y+dy
        if (x**2 + y**2 <1):
            data_sum += 4
    return data_sum
