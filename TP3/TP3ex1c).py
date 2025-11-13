#c)
for i in range(10):
    x = int(input("Saisir un nb entre 0 et n :"))
    if x >= 15:
        print(f"{x} est supérieur ou égale à 15 ")
    else :
        if x < 10 :
            print(f"{x} est strictement inférieur à 10")
        else :
            print(f"{x} est supérieur ou égale à 10 et strictement inférieur à 15")