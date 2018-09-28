import random, pylab, math, matplotlib.pyplot as plt
 
def direct_disks_box(N, sigma):
    z = True
    while z == True:
        L = [(random.uniform(sigma, 1.0 - sigma), random.uniform(sigma, 1.0 - sigma))]
        for k in range(1, N):
            a = (random.uniform(sigma, 1.0 - sigma), random.uniform(sigma, 1.0 - sigma))
            min_dist = min(((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) for b in L) 
            if min_dist < 4.0 * (sigma**2) : 
                z = True
                break
            else:
                z = False
                L.append(a)
    return L
#------------------------------Initial Conditions -----------------------------#
N = 4    #Number of disks
eta=0.18 #density
sigma = math.sqrt((eta)/(N*math.pi))
nruns = 10**2 #routine
#------------------------------------------------------------------------------#

#if u want to see histogram of y delete "#" in lines 27,32,35, 44 to 49

histox = []
#histoy = []
for i in range(nruns):
    abc = direct_disks_box(N, sigma)
    for k in range(N): 
        histox.append(abc[k][0])
        #histoy.append(abc[k][1])
        
#---------------------------Histogram of x positions --------------------------#
#plt.subplot(221)
pylab.hist(histox, normed=True , bins=100 , histtype='step')
pylab.xlabel('x-position')
pylab.ylabel('Probability Density')
pylab.title('Histogram of x-positions with $\eta$ = %.2f' %eta,fontsize = 14)
pylab.savefig('direct_disks_histo.jpeg')
#------------------------------------------------------------------------------#

#---------------------------Histogram of y positions --------------------------#
#plt.subplot(221)
#pylab.hist(histoy, normed=True , bins=100 , histtype='step')
#pylab.xlabel('y-position')
#pylab.ylabel('Probability Density')
#pylab.title('Histogram of y-positions with $\eta$ = %.2f' %eta,fontsize = 14)
#pylab.savefig('direct_disks_histo.jpeg')
#------------------------------------------------------------------------------#
plt.get_current_fig_manager().resize(878, 760)
plt.tight_layout()
pylab.show()