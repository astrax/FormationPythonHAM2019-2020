from pylab import *

print("Loi de Snell-Descartes pour la réfraction.")
n1 = float(input("Entrez l'indice de réfraction du premier milieu: "))
n2 = float(input("Entrez l'indice de réfraction du deuxième milieu: "))
choix = "o"
k = 0
theta1, theta2 = [],[]
while choix == "o":
    theta1.append(float(input("Entrez l'angle d'incidence en degrés: ")))
    if (n1*sin(deg2rad(theta1[k])))/n2 < -1 or n1 * (n1*sin(deg2rad(theta1[k])))/n2 > 1:
        print("Il y aura une réflexion totale pour l'angle d'incidence donné. Essayez d'autres valeurs.")
        theta1.append(float(input("Entrez l'angle d'incidence en degrés: ")))
    theta2.append(rad2deg(arcsin(n1*sin(deg2rad(theta1[k]))/n2)))
    print("L'angle d'incidence est de {:.2f} degrés et l'angle de réfraction de {:.2f} degrés.".format(theta1[k], theta2[k]))
    choix = input("Voulez-vous entrer plus de valeurs (o / n)?: ")
    while (choix!='o') and (choix!='n'):
        print("Entrée invalide. Tapez o ou n. ")
        choix = input("Voulez-vous entrer plus de valeurs (o / n)?: ")
        
    k +=1

if choix == "n":
    scatter(theta1, theta2)
    suptitle("Loi de Snell-Descartes", fontweight='bold')
    title("Angle de réfraction en fonction de l'angle d'incidence")
    xlabel("Angle d'incidence" + r" $\theta_1$")
    ylabel("Angle de réfraction" + r" $\theta_2$")
    savefig("snell.png")
    show()