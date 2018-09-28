import math,random,pylab,matplotlib.pyplot as plt

def gama_distribution(N, beta, P):
    gama = random.uniform(0,1)  
    for i in range(N):
        #alfa[i]=random.uniform(0,1)
        gama = gama * random.uniform(0,1)
    L=- math.log((gama)/(beta*P))
    return beta*P*L

def gama_cut(N,xcut):
    x1=1-(N*1.0)/(1.0*xcut)
    if(x1<0):
        return 
    else:
        z=True
        while z == True:
            delta_x = - math.log(random.uniform(0,1))/x1
            x = xcut + delta_x
            gama1 = ((x/xcut)**N) * math.exp(-(1-x1)*delta_x)
            if(random.uniform(0,1)>gama1): z = True
            else:
                z = False
        return xcut+delta_x

N = 4
beta = .5
P=2.
nruns=10**4
xcut=5.

#graf_gamax=[]
#graf_gamay=[]
#graf_gamax_cut=[]
#graf_gamay_cut=[]
x_sorting = []
kn_y=[]
xk_x=[]
for k in range (nruns):
    x = gama_distribution(N, beta, P)
    x_cut = gama_cut(N,xcut)
    #gama_function = (x**N * math.exp(-x))/math.factorial(N)
    #gama_function_cut = (x_cut**N * math.exp(-x_cut))/math.factorial(N)
    #graf_gamax.append(x)
    #graf_gamay.append(gama_function)
    #graf_gamax_cut.append(x_cut)
    #graf_gamay_cut.append(gama_function_cut)
    x_sorting.append(x)

x_sorting.sort()

for l in range(nruns):
    a = random.choice(x_sorting)
    for j in range (nruns):
        if (a == x_sorting[j]) :
            b=float(j)
            break
    xk_x.append(a)
    kn_y.append((b)/nruns)

#pylab.plot(graf_gamax,graf_gamay,'s')
#pylab.plot(graf_gamax_cut,graf_gamay_cut,'o')
#pylab.hist(graf_gamax, normed=True , bins=350 )
#pylab.hist(graf_gamax_cut, normed=True , bins=350 )
pylab.plot(xk_x,kn_y,'s')
#pylab.hist(xk_x, normed=True , bins=300, histtype = 'step' )
pylab.xlabel('xk')
pylab.ylabel('k/N')
pylab.axis([0,16,0,1])
#pylab.xlabel('x')
#pylab.ylabel('GammaN(x)(gamma dist.)')
pylab.title('Gamma Distribuition whit N = %d and xcut = 5'%N )
pylab.savefig('gama_function.sorting.jpeg')
pylab.grid(True)
plt.get_current_fig_manager().resize(878, 760)
plt.tight_layout()
pylab.show()