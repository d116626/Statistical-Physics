# -*- coding: utf-8 -*-

import random, math
import matplotlib.pyplot as plt

def energy(S, N, nbr):
    E = 0.0
    for k in range(N):
        E -=  S[k] * sum(S[nn] for nn in nbr[k])
    return 0.5 * E

list_T = [1.0 + 0.2 * i for i in range(25)] # temperaturas
for L in [2,4]: #dimensões das redes
    CV = []; EN=[]; M=[]; B=[]
    
    for T in list_T:
        
        
        N = L * L
        nbr = {i : ((i // L) * L + (i + 1) % L, (i + L) % N,
                    (i // L) * L + (i - 1) % L, (i - L) % N) \
                                            for i in range(N)}

        S = [random.choice([1, -1]) for k in range(N)]
        p  = 1.0 - math.exp(-2.0 / T)
        nsteps = 10**4
        S = [random.choice([1, -1]) for k in range(N)]
        E = [energy(S, N, nbr)]

        for step in range(nsteps):
            k = random.randint(0, N - 1)
            Pocket, Cluster = [k], [k]
            while Pocket != []:
                j = Pocket.pop()
                for l in nbr[j]:
                    if S[l] == S[j] and l not in Cluster \
                        and random.uniform(0.0, 1.0) < p:
                        Pocket.append(l)
                        Cluster.append(l)
            for j in Cluster:
                S[j] *= -1
            E.append(energy(S, N, nbr))
            M.append(sum(S))
            
        
        #if (T==2.6 and L == 6):
        #    plt.figure(1)
        #    n, bins, patches = plt.hist(M, 60, normed=1,facecolor='r',alpha=0.75)
        #    plt.xlabel('$Magnetization$ $Total$')
        #    plt.ylabel('$Probabiliti \pi_M$')
        #    plt.title('$Probability$ $\pi_M$ $for$ $a$ $lattice$ $%.0f$ $X$ $%.0f$ $with$ $T=%2.1f$' %(L,L,T))
        #
        print 'L =', L , ' T =',T   
         
        M4 = sum(float(m)**4/(float(len(M))*N**4) for m in M)
        M2 = sum(float(m)**2/(float(len(M))*N**2) for m in M)
        B  += [0.5 * ( 3 - M4 / ( M2 ** 2 ) )]
        E_mean = sum(E)/ len(E)
        E2_mean = sum(a ** 2 for a in E) / len(E)
        cv = (E2_mean - E_mean ** 2 ) / N / T ** 2
        EN += [E_mean/N]
        CV += [cv]
        
    plt.figure(2)
    plt.plot(list_T, EN,'-', label='$L$=$%.0f\\times %.0f$' %(L,L))
    plt.xlabel('$T$', fontsize=16)
    plt.ylabel('$E/N$', fontsize=16)
    plt.title('Mean Energy x Temperature for a Square Lattice')
    plt.legend(loc='top left',title='Lattice Size')
    
   
    plt.figure(3)
    plt.plot(list_T,CV,'-', label='$L$=$%.0f \\times %.0f$' %(L,L))
    plt.xlabel('$T$', fontsize=16)
    plt.ylabel('$c_{V}$', fontsize=16)
    plt.title('Heat Capacity x Temperature for a Square Lattice')
    plt.legend(loc = 'top right',title='Lattice Size')
    
    plt.figure(4)
    plt.plot(list_T,B,'-', label='$L$=$%.0f \\times %.0f$' %(L,L))
    plt.xlabel('$T$', fontsize=16)
    plt.ylabel('$B(T)$', fontsize=16)
    plt.title('Binder Cumulant x Temperature for a Square Lattice')
    plt.legend(loc='lower left',title='Lattice Size')

plt.figure(4)
plt.axvline(x=2.269,ymin=0.,ymax=1.0,color='k',linestyle='--',label="$T_c =2.269$")
plt.legend(loc='lower left' ,title='Lattice Size')
plt.show()