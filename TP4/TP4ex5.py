date = input("Entrez une date au format jjmmaaaa : ")
if len(date) != 8 or not date.isdigit():
    print("Format incorrect. Veuillez saisir 8 chiffres.")
else:
    j = int(date[0:2])
    m = int(date[2:4])
    a = int(date[4:8])
    valide = True
    if m < 1 or m > 12:
        valide = False
    else:
        if m in [1,3,5,7,8,10,12]:
            maxj = 31
        elif m in [4,6,9,11]:
            maxj = 30
        elif m == 2:
            if (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0):
                maxj = 29
            else:
                maxj = 28
        else:
            maxj = 0
        if j < 1 or j > maxj:
            valide = False
    if valide:
        print("La date est correcte.")
    else:
        print("La date est incorrecte.")
