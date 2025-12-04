nom1 = input("Entrer un nom :")
prenom1 = input("Entrer un prenom :")

nom2 = input("Entrer un nom :")
prenom2 = input("Entrer un prenom :")

personne1 = (nom1.upper(),prenom1.capitalize())
personne2 = (nom2.upper(),prenom2.capitalize())

liste = [personne1, personne2]
liste.sort()

for nom, prenom in liste :
    print(prenom,nom)

# Notez que str.upper().isupper() pourrait être False si la chaine contient des
# caractères non capitalisables