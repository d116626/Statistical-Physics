from random import uniform
import math
def markov_pi(delta, n):
    x, y = 1.0, 1.0
    data=[]
    for i in range (n):
        dx, dy = uniform(-delta, delta), uniform(-delta, delta)
        if(abs(x+dx)<1 and abs(y+dy)<1):
          x, y=x+dx, y+dy
        if (x**2 + y**2 <1):
            data.append(1)
        else:
            data.append(0)    
    return data
    
power = 22
n=2**power    # total number of points
delta=0.03  # size of the box 
data= markov_pi(delta, n)
new_data2=[]
for j in range(power):
    new_data2 = []
    sum_data = 0.0
    sum_data_sq = 0.0
    N = n/2**j
    while data != []:
        x = data.pop()
        y = data.pop()
        sum_data += x + y
        sum_data_sq += x ** 2 + y ** 2
        new_data2.append((x + y) / 2.0 )
    error_ap = (math.sqrt(sum_data_sq /(2* N) - (sum_data /(2* N)) ** 2) / math.sqrt(2*N))
    data = new_data2[:]
    pi = sum_data*4/N
    print error_ap



    
   
    
        
        
    
    
    
   
        
    
        
    
    



