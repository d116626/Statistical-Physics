from random import uniform
def pi_markov(delta, n):
    n_hits=float(0)
    x, y = 0.5, 0.5
    k=0
    for i in range (n):
        dx, dy = uniform(-delta, delta), uniform(-delta, delta)
        if(abs(x+dx)<1 and abs(y+dy)<1):
          x, y=x+dx, y+dy
        else:
            k+=1
        if (x**2 + y**2 <1):
            n_hits += 1
    pi=4*(n_hits/n)
    print k
    return pi

n=10**3     #total number of points
l=0
delta=0.1
j=0.0
while delta <3.1:
    for j in range(1):
        l=l+pi_markov(delta, n)
        
        j+=1
       
        
        delta += 0.1
    


   




    
        
                
            
    