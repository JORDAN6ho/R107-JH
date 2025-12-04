chaine = input("Entrez un mot ou une phrase : ")

chaine = chaine.lower()

filtre = ""
for c in chaine:
    if c.isalpha():
        filtre += c

if filtre == filtre[::-1]:
    print("C'est un palindrome !")
else:
    print("Ce n'est pas un palindrome.")
