import numpy, pylab
import matplotlib.pylab as plt
from math import pi, exp, sqrt, sinh, tanh
 
def density_matrix(grid, rho,beta):
    for i in range(N):
        x = grid[i]
        for j in range(N):
            xp = grid[j]
            vx=x**2 / 2
            vxp=xp**2 / 2
            rho[i][j] = exp(-(beta*vx)/2) * 1/sqrt(2.0 * pi * beta) * exp(- ((x-xp)**2)/(2*beta)) * exp(-(beta*vxp)/2)
            rho2[i][j] = 1.0 / sqrt(2.0 * pi * sinh(beta)) * exp( -((x+xp) ** 2)/4  * tanh(beta / 2.0) - ((x-xp) ** 2)/4  * (tanh(beta / 2.0))**-1 )
            rho_diference[i][j] = rho[i][j] - rho2[i][j]
            #Density matrix for a free particle 
    return rho, rho2, rho_diference

beta = 2**-10
betaf= 2**-20
N = 2000
grid = numpy.linspace(-5.0, 5.0, N)#make a list with 100 elements between -5 and 5
rho = numpy.zeros(shape=(N,N))#fills a NxN size matrix with zeros
rho2 = numpy.zeros(shape=(N,N))
rho_diference=numpy.zeros(shape=(N,N))
del_x = grid[1] - grid[0] # distance between elements in a list

rho, roh2 , rho_diference = density_matrix(grid, rho,beta)

while beta<betaf:
    beta *= 2
    rho = del_x*numpy.dot(rho, rho)
    rho2 = del_x*numpy.dot(rho2, rho2)
    

plt.subplot(2,2,1)
plt.imshow(rho, interpolation='nearest')
plt.colorbar(orientation ='vertical')
plt.title(r'$Trotter$ $formular$ $\beta = %g$' %beta)

plt.subplot(2,2,2)
plt.imshow(rho2, interpolation='nearest' )
plt.colorbar(orientation ='vertical')
plt.title(r'$Exact$ $density$ $matrix$ $\beta = %g$' %beta)

plt.subplot(2,2,3)
plt.imshow(rho_diference, interpolation='nearest' )
plt.colorbar(orientation ='vertical')
plt.title(r'$Error$ $\beta = %g$' %beta)

#plt.subplot(2,2,4)
#y_arrow = [rho[k][k] for k in range(N)]
#pylab.plot(grid, y_arrow, 'ro')
#y2_arrow = [1.0 / sqrt(2.0 * pi * sinh(beta)) * exp( -x ** 2 * tanh(beta / 2.0)) for x in grid]
#pylab.plot(grid, y2_arrow, 'b-')



pylab.savefig('asbdbasdabsd.jpeg')
plt.get_current_fig_manager().resize(878, 760)
plt.tight_layout()
pylab.show()