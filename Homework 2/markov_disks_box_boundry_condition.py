# -*- coding: utf-8 -*-
import math,random,pylab,matplotlib.pyplot as plt

def dist(x,y):
    d_x = abs(x[0] - y[0]) % 1.0
    d_x = min(d_x, 1.0 - d_x)
    d_y = abs(x[1] - y[1]) % 1.0
    d_y = min(d_y, 1.0 - d_y)
    return  d_x ** 2 + d_y ** 2

def markov_disck(L,sigma,Lx,Ly, delta,nsteps):
    histox=[]
    histoy=[]
    for i in range(nsteps):
        a = random.choice(L)
        L.remove(a)
        b = ((a[0] + random.uniform(-delta, delta)) % Lx, (a[1] + random.uniform(-delta,delta)) % Ly)
        min_dist = min(dist(b, x) for x in L)
        if  min_dist < 4.0 * sigma ** 2:
            L.append(a)
        else:
            L.append(b)
            histox.append(b[0])
            histoy.append(b[1])
    return L, histox,histoy

#-------------------------------Initial Conditions ------------------------------#
L = [[0.25,0.25],[0.75,0.25],[0.25,0.75],[0.75,0.75]] #initial positions of disks
Lx = 1.0 #the length of the box x-axis
Ly = 1.0 #the length of the box x-axis
N=len(L) #numberm of disks
eta=0.18 #density
sigma = math.sqrt((eta)*Lx*Ly/(N*math.pi))#Disc radius
positions = [[0.25,0.25],[0.75,0.25],[0.25,0.75],[0.75,0.75]]
nsteps = 10 #routine
delta = 0.15   
#--------------------------------------------------------------------------------#


#---------------------------Snapshot Initial Positions --------------------------#
plt.subplot(221)
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

#--------------------------------------------------------------------------------#

L, histox,histoy = markov_disck(L,sigma,Lx,Ly, delta,nsteps)

#----------------------------Snapshot Final Positions ---------------------------#
plt.subplot(222)
v=[-Lx,0,Lx]
u=[-Ly,0,Ly]
for [x,y] in L:
    for delx in v:
            for dely in u:
                cir=pylab.Circle((x +delx  , y +dely ), radius = sigma)
                pylab.gca().add_patch(cir)
pylab.axis([0,Lx,0,Ly])
pylab.xlabel('x-position')
pylab.ylabel('y-position')
pylab.title('Snapshot Final Positions',fontsize = 14)

#--------------------------------------------------------------------------------#

#----------------------------Histogram of x positions ---------------------------#
if histox != []:
    plt.subplot(223)
    pylab.hist(histox, normed=True , bins=100 , histtype='step')
    pylab.xlabel('x-position')
    pylab.ylabel('Probability Density')
    pylab.title('Histogram of x-positions with $\eta$ = %.2f' %eta,fontsize = 14)

    
else: print 'There was no movement in the x-axis'
#--------------------------------------------------------------------------------#

#----------------------------Histogram of y positions ---------------------------#
if histoy != []:
    plt.subplot(224)
    pylab.hist(histoy, normed=True , bins=100 , histtype='step')
    pylab.xlabel('y-position')
    pylab.ylabel('Probability Density')
    pylab.title('Histogram of y-positions with $\eta$ = %.2f' %eta,fontsize = 14)
    pylab.savefig('markov_boundry_condition')
else: print 'There was no movement in the y-axis'
#--------------------------------------------------------------------------------#
#plt.subplots_adjust(left=0.08, right=0.95, wspace=0.50, hspace=0.40)
plt.get_current_fig_manager().resize(878, 760)
plt.tight_layout()
pylab.show()