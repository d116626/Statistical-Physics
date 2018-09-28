import random, math, pylab

def gama_distribution(N, beta, P):
    gama = random.uniform(0,1)  
    for i in range(N):
        #alfa[i]=random.uniform(0,1)
        gama = gama * random.uniform(0,1)
    L=- math.log((gama)/(beta*P))
    return beta*P*L
    
N =4
beta = .5
P=1.
nruns=10**3
graf_gamax=[]
graf_gamay=[]
#graf_gamax_histo=[]

for k in range (nruns):
    x = gama_distribution(N, beta, P)
    gama_function = (x**N * math.exp(-x))/math.factorial(N)
    graf_gamax.append(x)
    graf_gamay.append(gama_function)
    #graf_gamax_histo.append(math.sqrt(N)*x)

pylab.plot(graf_gamax,graf_gamay)
#pylab.hist(graf_gamax_histo, normed=True , bins=150 )
pylab.axis([0,10,0,1])
pylab.xlabel('x')
pylab.ylabel('GammaN(x)(gamma dist.)')
pylab.title('Gamma Distribuition with N = %d' %N)
pylab.savefig('gama_function.jpeg')
pylab.grid(True)
pylab.show()