L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]

courant = L1[0]
autre = L1.count(L1[0])

for i in L1:
    c = L1.count(i)

    if c > autre :
        courant = c