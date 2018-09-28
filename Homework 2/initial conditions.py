import math,random,pylab, matplotlib.pyplot as plt

def initial_conditions(N,eta):
    Dx=1./8. #distannce between two atoms on the x axis
    Dy=math.sqrt(3.)*Dx/2. #distannce between two atoms on the y axis
    positions=[[(k1+(k2%2)/2.)*Dx,k2*Dy] for k1 in range(N) for k2 in range(N)]
    Lx=N*Dx #Box size x axis
    Ly=N*Dy #Box size y axis
    sigma = math.sqrt((Lx*Ly*eta)/(N*N*math.pi))
    return positions,Lx,Ly,sigma,positions, Dx, Dy

N=8 #number of disks is N*N
eta = 0.4
L,Lx,Ly,sigma, positions, Dx, Dy= initial_conditions(N,eta)

#---------------------------Snapshot Final Positions --------------------------#
v=[-Lx,0,Lx]
u=[-Ly,0,Ly]
for [x,y] in positions:
    for delx in v:
            for dely in u:
                cir=pylab.Circle((x +delx  , y +dely ), radius = sigma)
                pylab.gca().add_patch(cir)
pylab.axis([0,Lx,0,Ly])
pylab.xlabel('x-position')
pylab.ylabel('y-position')
pylab.title('Snapshot Initial Positions',fontsize = 14)
pylab.savefig('Snapshot_Initial_Positions.jpeg')
#------------------------------------------------------------------------------#
plt.get_current_fig_manager().resize(878, 760)
plt.tight_layout()
pylab.show()