n = float(input("Vous cherchez la table de multiplication de quel nombre:"))
list = []
c = 0
multi = 0
for i in range(9):
    c = c + 1
    multi = n * c
    list.append(multi)
print(list)