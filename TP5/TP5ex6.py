chaine = input("Entrez une chaîne : ")
taille = 0
for c in chaine:
    taille += 1
print("Taille de la chaîne :", taille)
voyelles = "aeiouyAEIOUY"
nb_voyelles = 0
for c in chaine:
    if c in voyelles:
        nb_voyelles += 1
pourcentage = (nb_voyelles / taille) * 100
print("Pourcentage de voyelles :", pourcentage, "%")
mot = "wagon"
index = -1
for i in range(taille - len(mot) + 1):
    ok = True
    for j in range(len(mot)):
        if chaine[i + j].lower() != mot[j]:
            ok = False
            break
    if ok:
        index = i
        break
if index != -1:
    print(f'"wagon" apparaît à la position : {index}')
else:
    print('"wagon" n’apparaît pas.')
occur = 0
for i in range(taille - len(mot) + 1):
    ok = True
    for j in range(len(mot)):
        if chaine[i + j].lower() != mot[j]:
            ok = False
            break
    if ok:
        occur += 1
print("Nombre d'occurrences :", occur)