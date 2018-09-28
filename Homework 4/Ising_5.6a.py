import matplotlib.pyplot as plt
from math import*
#-------------------------------------------------------------------------------
def Vecinos(L):
    N = L * L
    site_dic = {}
    x_y_dic = {}
    for j in range(N):
        row = j // L
        column = j - row * L
        site_dic[(row, column)] = j
        x_y_dic[j] = (row, column)
        nbr = []
    for j in range(N):
        row, column = x_y_dic[j]
        right_nbr = site_dic[row, (column + 1) % L]
        up_nbr = site_dic[(row + 1) % L, column]
        left_nbr = site_dic[row, (column - 1 + L) % L]
        down_nbr = site_dic[(row - 1 + L) % L, column]
        nbr.append((right_nbr, up_nbr, left_nbr, down_nbr))
    nbr = tuple(nbr)
    return nbr
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
def gray_flip(t, N):
    k = t[0]
    if k > N: return t, k
    t[k - 1] = t[k]
    t[k] = k + 1
    if k != 1: t[0] = 1
    return t, k
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
L = 4
N = L * L
D = []
nbr = Vecinos(L)
S = [-1] * N
E = -2 * N
dos = {}
dos[E] = {}
M = sum(S)
dos[E][M] = 1
tau = range(1, N + 2)
for i in xrange(1, 2 ** N):
    tau, k = gray_flip(tau, N)
    h = sum(S[n] for n in nbr[k - 1])
    E += 2 * h * S[k - 1] 
    S[k - 1] *= -1
    M = sum(S)
    if E  in dos: 
        if M in dos[E]:
            dos[E][M] += 1
        else:
            dos[E][M] = 1
    else:
        dos[E] = {}       
        dos[E][M] = 1

print '-------------------Ising Model Data-----------------------------------'
print '----------------------------------------------------------------------'
for E in sorted(dos.keys()):
    for M in sorted(dos[E].keys()):
        print 'Energia =%2i Mag_tot=%2i DoS=%2i' % (E, M, dos[E][M])
print '----------------------------------------------------------------------'
print '\n'
print '------------------------Density of States %.0f X %.0f -----------------------------' %(L,L)
print 'Energy', '     ', 'DoS'
for E in sorted(dos.keys()):
    if E >= 0:
        print E,'          ' ,sum(dos[E].values())

def Magn(T):
    Z = 0; P = [] ; mag = []
    for E in sorted(dos.keys()):
            for M in sorted(dos[E].keys()):
                D.append(dos[E][M])
                Z += dos[E][M]*exp(-E/T)
                P.append(dos[E][M]*exp(-E/T))
                mag.append(M)
    P = [P[i]/Z for i in range(len(P))]
    
    plt.figure()
    plt.bar(mag,P,align='center')
    plt.xlabel('$Magnetization$ $Total$')
    plt.ylabel('$\pi_M$')
    plt.title('$Probability$ $\pi_M$ $for$ $a$ $lattice$ $4$ $X$ $4$ $T=%2.1f$' %(T))

Magn(2.5)
Magn(5.)

plt.figure()
n, bins, patches = plt.hist(D, 60, normed=1,facecolor='b',alpha=0.75)
plt.xlabel('$Density$ $of$ $States$ $D(E,N)$')
plt.ylabel('$Probability$ $of$ $DoS$')
plt.title('$Histogram$ $Density$ $of$ $States$')
plt.show()