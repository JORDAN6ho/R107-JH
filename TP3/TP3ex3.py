import random
x = random.randint(0,100)
c = 0
for i in range(0,100):
    n = int(input("Saisir un nb entre 0 et 100 :"))
    if not x == n:
        c = c + 1
        if x > n :
            print(f"la valeur est plus grande")
        else :
            if x < n :
                print(f"la valeur est plus petite")
    else :
        break
print(f"La valeur est égale à {x}")
print(f"Le nombre de tours est de {c}")

