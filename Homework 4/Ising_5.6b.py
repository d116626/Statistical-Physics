import matplotlib.pyplot as plt
from math import*
def Dos(L):
    dos = {}
    f = open('C:/Users/diego/Desktop/Listas Estat Comp/Lista 4/data_dosEM_L=%i.txt' % L, 'r')
    for line in f:
        E, M, D = line.split() 
        dos[int(E)] = {}   
    f.close() 
    f = open('C:/Users/diego/Desktop/Listas Estat Comp/Lista 4/data_dosEM_L=%i.txt' % L, 'r')
    for line in f:
        E, M, D = line.split()
        dos[int(E)][int(M)] = int(D)
    f.close() 
    return dos
def mag(T):
    Z = 0.; Mag = []; P = []
    dos = Dos(6)
    print '------------------------Density of States %.0f X %.0f -----------------------------' %(L,L)
    print 'Energy', '     ', 'DoS' 
    for E in sorted(dos.keys()):
        for M in sorted(dos[E].keys()):
            Z += dos[E][M]*exp(-E/T)
            P.append(dos[E][M]*exp(-E/T))
            Mag.append(M)
        
        if E >= 0:
            print E,'          ' ,sum(dos[E].values())
        
    P = [P[i]/Z for i in range(len(P))]
    plt.figure()
    plt.bar(Mag,P,align='center', width=2.0)
    plt.xlabel('$Magnetization$ $Total$')
    plt.ylabel('$\pi_M$')
    plt.title('$Probability$ $\pi_M$ $for$ $a$ $lattice$ $%.0f$ $X$ $%.0f$ $with$ $T=%2.1f$' %(L,L,T))

L=6
Ts=[3.0]
for T in Ts: mag(T)

def binder(T,L):
    dos = Dos(L); N=L*L
    Z = 0.; m2=0.; m4=0.
    dos = Dos(L)
    for E in sorted(dos.keys()):
        for M in sorted(dos[E].keys()):
            Z += dos[E][M]*exp(-E/T)
            m2 += (M/float(N))**2*dos[E][M]*exp(-E/T)
            m4 += (M/float(N))**4*dos[E][M]*exp(-E/T) 
    m2 /= Z
    m4 /= Z
    Bin = 0.5*(3-m4/m2**2)
    return Bin  
list_T = [0.5 + 0.01 * i for i in range(800)]
B2 =[]; B4 =[]; B6 =[]
for T in list_T:
    B2.append(binder(T,2))
    B4.append(binder(T,4))
    B6.append(binder(T,6))
plt.figure()
plt.plot(list_T,B2,'r',label='$L=2$')
plt.plot(list_T,B4,'g',label='$L=4$')  
plt.plot(list_T,B6,'b',label='$L=6$')
plt.axvline(x=2.269,ymin=0.,ymax=1.0,color='k',linestyle='--',label="$T_c$  = 2.269")
plt.xlabel('$Temperature$')
plt.ylabel('$B(T)$')
plt.title('$Binder$ $Cumulant$')
plt.legend()    
plt.show()
    