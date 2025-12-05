import random

## Fonction generer(nbr, vmin, vmax) pour générer un tableau de 'nbr'
##valeurs
## comprises entre 'vmin' et 'vmax'
"""
## Fonction combienInferieur(table, vseuil) pour compter le nombre de
valeurs
## d'un tableau 'table' inférieures à la valeur 'vseuil'
"""
#a
def generer(nbr, vmin, vmax):
    table = []
    for i in range(nbr):
        table.append(random.randint(vmin, vmax))
    return table

def combienInferieur(table, vseuil):
    c = 0
    for v in range(len(table)):
        if v < vseuil :
            c = c + 1
    return c

nbr =  int(input("Choisir valeur de nbr : "))
vmin = int(input("Choisir valeur de vmin : "))
vmax = int(input("Choisir valeur de vmax : "))

choix = input("Voulez-vous préciser le seuil")
if (choix == "O" or choix == "Oui"):
    vseuil = int(input("Choisir valeur de vseuil : "))
else :
    vseuil == 30

nb = 100
print(f"Générer {nb} nombres entiers entre 0 et 100")
tab = generer(nb, 0, 100)
tab.sort()
print(tab)
total = combienInferieur(tab, 25)
print(f"Il y en a {total} inférieurs à 25")