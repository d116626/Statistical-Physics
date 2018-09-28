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

def dist(a,b):
    return math.sqrt( sum((a[k] - b[k]) **2 for k in range(3)))
    
N = 15

for i in range(10) :
    if N==19:gamma = 0.01
    if N==15:gamma = 0.05
    r=0.2
    R=1./(1./r-1.)
    sigma=.25
    
    random.seed(138)
    while True: 
        positions = [unit_sphere() for j in range(N)] 
        if minimum_distance(positions, N) > 2.0 * r: break
    random.seed()
    
    print ''
    print i
    n_acc = 0; acc_rate = 0 ;eta = 0; step=0
    print 'N =', N
    while sigma>1.e-13:
        step += 1
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
        if step % 100000 == 0:
            eta = 1.*N/2.*(1.-math.sqrt(1-r*r))
            print 'r =',r,' | ', 'eta =', eta, ' | ', 'R =', 1./(1./r-1.),' | ', 'acc rate =', acc_rate,' | ', 'sigma =', sigma

    
    print 'r =',r,' | ', 'eta =', eta, ' | ', 'R =', 1./(1./r-1.),' | ', 'acc rate =', acc_rate,' | ', 'sigma =', sigma

    from enthought.mayavi.mlab import points3d,show,figure
    figure(bgcolor=(0,0,.1),size=(1000, 700))
    m=1.+R
    x,y,z=[m*pos[0] for pos in positions],[m*pos[1] for pos in positions],[m*pos[2] for pos in positions]
    rad=[2*R for pos in positions]
    x.append(0);y.append(0);z.append(0);rad.append(2)
    points3d(x,y,z, rad, scale_factor=1, resolution=100,transparent=True)
    show()
    

    print ''
    #eta_opt = eta
    #if N==19:N, eta_opt = 19, 0.81096
    #if N==15:N, eta_opt = 15, 0.80731    
    d_ref = math.sqrt(1.0 - (1.0 - 2.0 * eta / float(N)) ** 2) * 2.0
    mat_mat = [[0 for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(i):
            if (dist(positions[i], positions[j]) < d_ref*1.0001):
                mat_mat[i][j] = 1
                mat_mat[j][i] = 1
    connectivity = [sum(mat_mat[i]) for i in range(N)]
    for j in range(N):
        print 'disk %2i [connectivity %i] is connected with ' % (j, connectivity[j]) + \
    ' '.join(['%2i,' % (k) for k in range(N) if mat_mat[j][k]])

            
    
  

