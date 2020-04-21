## NOM DU PROGRAMME: EquOnde2D.py
#% IMPORTATION
import numpy as np
import matplotlib.pyplot as plt
# PARAMETRES PHYSIQUES
C = 0.05  #VIT ONDE 
Lx = 6.0  #taille du domaine
Ly = 4.0  #taille du domaine
T = 5.0   #temps d'integration

# PARAMETRES NUMERIQUES
NX = 151  #nombre de points de grille
NY = 101  #nombre de points de grille
NT = 250  #nombre de pas de temps

dx = Lx/(NX-2) #pas de grille (espace)
dy = Ly/(NY-2) #pas de grille (espace)
dt = T/NT      #pas de grille (temps)
alpha=(C**2*dt**2/dx**2)
# Pour la figure
xx = np.zeros((NX,NY))
yy = np.zeros((NX,NY))
for i in np.arange(0,NX):
   for j in np.arange(0,NY):
      xx[i,j]=i*dx
      yy[i,j]=j*dy

a=40.0

#Initialisation
ddU   = np.zeros((NX,NY))
U_data = np.exp(-a*((xx-1.5)**2+(yy-1.5)**2))
U_old= U_data.copy()
U_new = np.zeros((NX,NY))

# Boucle en temps
for n in np.arange(0,NT):
   ddU[1:-1,1:-1] = (U_data[2:,1:-1]-2*U_data[1:-1,1:-1]+U_data[:-2,1:-1])/(dx**2) \
                  + (U_data[1:-1,2:]-2*U_data[1:-1,1:-1]+U_data[1:-1,:-2])/(dy**2)
   U_new[1:-1,1:-1]=2*U_data[1:-1,1:-1]-U_old[1:-1,1:-1] + alpha*ddU[1:-1,1:-1]
   toto=U_old
   U_old=U_data
   U_data=U_new
   U_new=toto
## FIXED BC
#   U_data[0,:]=0.0

# REFLECTING BC
   U_data[0,:]=U_data[2,:]
   U_data[NX-1,:]=U_data[NX-3,:]
   U_data[:,0]=U_data[:,2]
   U_data[:,NY-1]=U_data[:,NY-3]

## PERIODIC BC
#   U_data[0,:]=U_data[NX-2,:]
#   U_data[NX-1,:]=U_data[1,:]
#   U_data[:,0]=U_data[:,NY-2]
#   U_data[:,NY-1]=U_data[:,1]

   if (n%10==0):
     plotlabel= "N = " + str(n+1)
     plt.pcolormesh(xx,yy,U_data)
     plt.axis('image')
     plt.clim(-0.1,0.1)
     plt.title(plotlabel)
     plt.draw()
     plt.pause(0.001)

plt.show()