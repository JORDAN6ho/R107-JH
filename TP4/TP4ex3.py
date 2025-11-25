nMax = 3
v1 = []
v2 = []
n = int(input("Quelle est la taille de vos vecteurs [entre 1 et 10] ?"))
while 1 < n or x < nMax :
    print("Erreur, saisir une nouvelle valeur :")
    x = int(input("Quelle est la taille de vos vecteurs [entre 1 et 10] ?"))

print("Saisir valeur de v1 :")
for i in range(n):
    valeur = int(input(f"v1{i} = "))
    v1.append(valeur)

print("Saisir valeur de v2 : ")
for i in range(n):
    valeur = int(input(f"v2{i} = "))
    v2.append(valeur)

scalaire = 0
for i in range(n):
    scalaire = scalaire + v1[i] + v2[i]

print(f"Le prorduit scalaire de v1 par v2 vaut {scalaire}")
