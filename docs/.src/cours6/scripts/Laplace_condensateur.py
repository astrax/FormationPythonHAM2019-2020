## NOM DU PROGRAMME: Laplace_condensateur.py
#% IMPORTATION
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d
eps = 1e-3 # erreur fractionnaire autorisée
L = 1.0 # longueur de chaque côté
N = int(input('nombre de points de grille sur un côté -> '))
dy = dx = L/(N-1.0)
x = np.array(range(N))*dx
y = np.array(range(N))*dy
(x, y) = np.meshgrid(x, y)
V = np.zeros((N, N))
# dÃ©finition des paramÃ¨tres physiques de l'expÃ©rience
V0 = 0.0             # les cotÃ©s de la boite sont au potentiel nul
Vp = 1.0           # potentiel de plaque
V[:,0]  = V0  # bord gauche
V[:,-1] = V0  # bord droit
V[-1,:] = V0  # bord infÃ©rieur
# initialisation de l'intÃ©rieur de la grille
V[1:N-1,1:N-1] = 0.0
# dÃ©finition de la gÃ©omÃ©trie du condensateur
V[N//4:3*(N//4),N//4]  = -Vp  # bord plaque gauche potentiel nÃ©gatif
V[N//4:3*(N//4),3*(N//4)]  = Vp   # bord plaque droit potentiel positif

# calculer le paramètre de sur-relaxation
omega = 2.0/(1.0+np.sin(np.pi*dx/L))
# pixels blancs et noirs: les blancs ont j+k pairs; les noirs ont j+k impairs
blanc = [(j, k) for j in range(1, N-1) for k in range(1, N-1) if (j+k)%2 == 0]
noir = [(j, k) for j in range(1, N-1) for k in range(1, N-1) if (j+k)%2 == 1]
# préparer l'animation
image = plt.imshow(V.T, origin='lower', extent=(0.0, L, 0.0, L))
plt.colorbar()
n = 0 # nombre d'itérations
err = 1.0 # erreur moyenne par site
while err > eps:
    # mettre à jour le tracé animé
    image.set_data(V.T)
    plt.title('itération %d'%n)
    plt.tight_layout()
    plt.show()
    plt.pause(0.001)
    # prochaine itération en raffinement
    n = n+1
    err = 0.0
    for (j, k) in blanc+noir: # boucle sur pixels blancs puis pixels noirs
        dv = (V[j-1,k]+V[j+1,k]+V[j,k-1]+V[j,k+1])/4.0-V[j,k]
        V[j,k] += omega*dv
        V[N//4:3*(N//4),N//4]  = -Vp
        V[N//4:3*(N//4),3*(N//4)]  = Vp
        
        err += abs(dv)
    err /= N**2
# tracé de surface de la solution finale
fig = plt.figure()
equ = plt.contour(x,y,V.T,20,cmap = "jet")
#matplotlib.rcParams['contour.negative_linestyle'] = 'solid'
plt.clabel(equ, fontsize=10, inline=1,fmt='%1.2f')
plt.colorbar()

fig = plt.figure()
axis = fig.gca(projection='3d', azim=-60, elev=20)
surf = axis.plot_surface(x, y, V.T, rstride=1, cstride=1, cmap='viridis')
wire = axis.plot_wireframe(x, y, V.T, rstride=1+N//50, cstride=1+N//50,
                           color = "r", linewidth=0.5, alpha = 0.5)
axis.contour(x, y, V.T, 10, zdir='z', offset=-1.0)
axis.set_xlabel('x')
axis.set_ylabel('y')
axis.set_zlabel('u')
fig.colorbar(surf)
plt.tight_layout()
plt.savefig("Laplace_surrelax.png"); plt.savefig("Laplace_surrelax.pdf")
plt.show()