from pylab import *

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
fig, ax = plt.subplots(figsize=(8,8))
im = imshow(I, cmap='gray', interpolation='bilinear',
                origin='lower',  vmin= 0, vmax = 0.005)

title('Diffraction par une ouverture rectangulaire', fontweight='bold')

xlabel('X (cm)', fontsize=12, fontweight='bold')
ylabel('Y (cm)', fontsize=12, fontweight='bold')
xticks(linspace(0, 400, 7))
ax.set_xticklabels(linspace(-15, 15, 7),  color='r')
yticks(linspace(0, 400, 7))
ax.set_yticklabels(linspace(-15, 15, 7),  color='r')

savefig("diff2D.png"); savefig("diff2D.pdf")
show()