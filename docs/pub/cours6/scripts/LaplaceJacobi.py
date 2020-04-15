## NOM DU PROGRAMME: Laplace.py
#% IMPORTATION
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d
eps = 1e-5 # fractional error allowed
L = 1.0 # length of each side
N = int(input('number of grid points on a side −> '))
dy = dx = L/(N-1.0)
x = np.array(range(N))*dx
y = np.array(range(N))*dy
(x, y) = np.meshgrid(x, y)
u0 = np.zeros((N, N))
u1 = np.zeros((N, N))
# boundary conditions
for j in range(N):
    u1[j,N-1] = u0[j,N-1] = 1.0
# prepare animated plot

image = plt.imshow(u0.T, origin='lower', extent=(0.0, L, 0.0, L))
n = 0 # number of iterations
err = 1.0 # average error per site
while err > eps:
    # update animated plot
    image.set_data(u0.T)
    plt.title('itération %d'%n)
    plt.tight_layout()
    plt.show()
    plt.savefig("anim4/"+str(n)+".png")
    plt.pause(0.001)
    # next iteration in refinement
    n = n+1
    err = 0.0
    for j in range(1, N-1):
        for k in range(1, N-1):
            u1[j,k] = (u0[j-1,k]+u0[j+1,k]+u0[j,k-1]+u0[j,k+1])/4.0
            err += abs(u1[j,k]-u0[j,k])
    err /= N**2
    (u0, u1) = (u1, u0) # swap old and new arrays for next iteration
    
# surface plot of final solution

fig = plt.figure()
axis = fig.gca(projection='3d', azim=-60, elev=20)
surf = axis.plot_surface(x, y, u0.T, rstride=1, cstride=1, cmap='viridis')
wire = axis.plot_wireframe(x, y, u0.T, rstride=1+N//50, cstride=1+N//50,
                           color = "r", linewidth=0.5, alpha = 0.5)
axis.contour(x, y, u0.T, 10, zdir='z', offset=-1.0)
axis.set_xlabel('x')
axis.set_ylabel('y')
axis.set_zlabel('u')
axis.set_zlim(-1.0, 1.0)
fig.colorbar(surf)
plt.tight_layout()
plt.savefig("LaplaceJacobi.png"); plt.savefig("LaplaceJacobi.pdf")
plt.show()
            

