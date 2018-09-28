# -*- coding: utf-8 -*-
import numpy, pylab
import matplotlib.pylab as plt
from math import pi, exp, sin, cos, log, sqrt
 
def v(x):
    v = (khi*(khi-1)/sin(x)**2 + lambdah*(lambdah-1)/cos(x)**2)/2
    return v

def density_matrix(grid, rho, beta):
    for k in range(N):
        x=grid[k]
        for j in range(N):
            xp=grid[j]
            rho[k][j]=1./sqrt(2*pi*beta) * exp(-(beta*v(x))/2) * exp(- ((x-xp)**2)/(2*beta)) * exp(-(beta*v(xp))/2)
            
    return rho

#-------------------------------------Initial Conditions ------------------------------------#   
beta=2.0**(-20)
betaf=2.0**(3)
N=2000
khi=1.1
lambdah=1.2
delta=10**-100
grid=numpy.linspace(delta,pi/2-delta,N)
rho=numpy.zeros(shape=(N,N))
del_x=grid[1]-grid[0]
#--------------------------------------------------------------------------------------------#

rho = density_matrix(grid, rho,beta)

#--------------------------------Plot Diagonal Matrix Square  -------------------------------#
z2 = sum ((sin(x)**khi*cos(x)**lambdah)**2 for x in grid)


plt.subplot(2,2,1)
y1 = [((sin(x)**khi * cos(x)**lambdah)**2) / z2  for x in grid]
pylab.plot(grid, y1, 'ro', label='Exac Solution')
plt.title(r'$Diagonal$ $Matrix$ $Square$ $with$ $\chi = %g$ $\lambda=%g$' %(khi, lambdah))
plt.legend(loc = 3, prop={'size':4})
#--------------------------------------------------------------------------------------------#

print 'z simulação','      |         ', 'z exato','       |               ', 'beta'

while beta < betaf:
    beta *= 2.0
    rho=del_x * numpy.dot(rho,rho)
    z_norm  = sum(rho.diagonal())
    
    rho_diagonal = rho.diagonal() 
    zvalues=numpy.trapz(rho_diagonal,grid) 
    
    plt.subplot(2,2,1)
    y2=[(rho[k][k] / z_norm) for k in range(N)]#plota matriz normalizada
    pylab.plot(grid, y2, '-',label=r'$\beta = %g$' %beta )
    plt.legend(prop={'size':4})
    
    
    plt.subplot(2,2,2)
    y4 = [y1[i] - y2[i] for i in range(N) ]
    pylab.plot(grid, y4, '-', label=r'$\beta = %g$' %beta)
    plt.title(r'$Error$ $Matrix$ $Square$ $with$ $\chi = %g$ $\lambda=%g$' %(khi, lambdah))
    plt.legend(prop={'size':4.})
    
    z_exa = sum(exp(-beta*0.5*(khi+lambdah+2*i)**2) for i in range(N))
    
    print zvalues,'           ', z_exa,'              ' , beta



E_simulation= - (1.0/beta) * log(zvalues) 
E_exac=0.5*(lambdah+khi)**2

print 'E simulation = ',E_simulation
print 'E exact = ',E_exac


#---------------------------------------Plot Potential --------------------------------------#
plt.subplot(2,2,3)
y1 = [(v(x))  for x in grid]
pylab.plot(grid, y1, '-', label='$V(x)$')
pylab.axis([0, pi/2,10, 1000])
plt.title(r'$Potential$ $with$ $\chi=%0.1f$ $and$ $\lambda= %0.1f$' %(khi,lambdah))
plt.legend(loc=1,prop={'size':8.})
#--------------------------------------------------------------------------------------------#

plt.get_current_fig_manager().resize(780, 660)
plt.tight_layout()
pylab.show()