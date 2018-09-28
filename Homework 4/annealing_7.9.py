import random, math, pylab
import matplotlib.pylab as plt

def unit_sphere():
    x = [random.gauss(0.0, 1.0) for i in range(3)]
    norm =  math.sqrt(sum(xk ** 2 for xk in x))
    return [xk / norm for xk in x]

def minimum_distance(positions, N):
    dists = [math.sqrt(sum((positions[k][j] - positions[l][j]) ** 2 \
             for j in range(3))) for l in range(N) for k in range(l)]
    return min(dists)

def resize_disks(positions, r, N, gamma):
    Upsilon = minimum_distance(positions, N) / 2.0
    r = r + gamma * (Upsilon - r)
    return r

N = 13
gammas  = [0.01, 0.05, 0.1, 0.5]
for gamma in gammas:
   
    r=0.2
    R=1./(1./r-1.)
    sigma=.25
   
    random.seed(138)
    while True: 
        positions = [unit_sphere() for j in range(N)] 
        if minimum_distance(positions, N) > 2.0 * r: break
    random.seed()
   
    n_acc = 0
    step = 0
    acc_rate = 0
    eta = 0

    Rs = []
    etas=[]
    
    print 'gamma =', gamma
    
    while sigma>1.e-7:
        step += 1
        if step % 100000 == 0:
            eta = N / 2.0 * (1.0 - math.sqrt(1.0 - r ** 2))
            R = 1.0 / (1.0 / r - 1.0)
            print 'r =',r,' | ', 'eta =', eta, ' | ', 'R =', 1./(1./r-1.),' | ', 'acc rate =', acc_rate,' | ', 'sigma =', sigma
            
        k = random.randint(0, N - 1)
        newpos = [positions[k][j] + random.gauss(0, sigma) for j in range(3)]
        norm = math.sqrt(sum(xk ** 2 for xk in newpos))
        newpos = [xk / norm for xk in newpos]
        new_min_dist = min([math.sqrt(sum((positions[l][j] - newpos[j]) ** 2 \
                       for j in range(3))) for l in range(k) + range(k + 1, N)])
        if new_min_dist > 2.0 * r:
            positions = positions[:k] + [newpos] + positions[k + 1:]
            n_acc += 1
        if step % 100 == 0:
            acc_rate = n_acc / float(100)
            n_acc = 0
            if acc_rate < 0.2:
                sigma *= 0.5
            elif acc_rate > 0.8 and sigma < 0.5:
                sigma *= 2.0
            r = resize_disks(positions, r, N, gamma)
            R = 1.0 / (1.0 / r - 1.0)
            eta = 1.0 * N / 2.0 * (1.0 - math.sqrt(1.0 - r ** 2))
    
    Rs.append(R)
    etas.append(eta)
    
    print 'r =',r,' | ', 'eta =', eta, ' | ', 'R =', 1./(1./r-1.),' | ', 'acc rate =', acc_rate,' | ', 'sigma =', sigma
    
    pylab.plot(Rs, etas ,'o',label=r'$\gamma = %g$' %gamma )
    plt.xlabel('$R$')
    plt.ylabel('$Density$')
    plt.title('Density x R')
    plt.legend()
    plt.legend(prop={'size':15}, loc = 4)
   
    from enthought.mayavi.mlab import points3d,show,figure
    figure(bgcolor=(0,0,.1),size=(1000, 700))
    m=1.+R
    x,y,z=[m*pos[0] for pos in positions],[m*pos[1] for pos in positions],[m*pos[2] for pos in positions]
    rad=[2*R for pos in positions]
    x.append(0);y.append(0);z.append(0);rad.append(2)
    points3d(x,y,z, rad, scale_factor=1, resolution=100,transparent=True)
    show()

pylab.show()
            
    
  

