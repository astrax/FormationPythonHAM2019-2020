from pylab import *
from mpl_toolkits.mplot3d.axes3d import Axes3D

def Intensity(X, Y, a = 0.2 * 1.E-3, b = 0.2 * 1.E-3, lambda_ = 630 * 1.E-9, f2 = 10):
    # les dimensions de la tache centrale
    Dx = 1.E2 * (2 * lambda_ * f2) / a
    print("La largeur du maximum central le long (Ox) = {:.3f} cm".format(Dx))
    Dy = 1.E2 * (2 * lambda_ * f2) / b
    print("La largeur du maximum central le long (Oy) = {:.3f} cm".format(Dy))
    # Variables intermidières
    A = (pi * X * a)/(lambda_ * f2)
    B = (pi * Y * b)/(lambda_ * f2)
    return (sin(A)/A)**2 * (sin(B)/B)**2

# coordonnées de l'écran
X, Y = meshgrid(linspace(-15*1e-2, 15*1e-2, 400), linspace(-15*1e-2, 15*1e-2, 400)) 
# Intensité 
I = Intensity(X, Y)

# Figure de diffraction
fig = plt.figure(figsize=(10,8))
ax = plt.axes(projection='3d')
# plot surface
p = ax.plot_surface(X, Y, I, rstride=4, cstride=4, cmap='coolwarm',
                    linewidth=0, antialiased=False)
cb = fig.colorbar(p, shrink=0.5)

xlabel('X (m)', fontsize=12, fontweight='bold')
ylabel('Y (m)', fontsize=12, fontweight='bold')
title('Diffraction par une ouverture rectangulaire', fontweight='bold')

savefig("diff3D.png"); savefig("diff3D.pdf")
plt.show()