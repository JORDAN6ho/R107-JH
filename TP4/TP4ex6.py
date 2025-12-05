tab = [5, 2, 4, 8, 1, 3]
print(tab)
for i in range(len(tab)):
    m = i
    for j in range(i+1, len(tab)):
        if tab[j] < tab[m]:
            m = j
    tab[i], tab[m] = tab[m], tab[i]
    print(tab)
