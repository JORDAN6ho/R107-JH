L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]

""" ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Completez le programme a partir d'ici.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * / """

courant = L1[0]
autre = 1

for i in range(len(L1)):
    cherche = L1[i]

    c = 0
    for i in range(1, len(L1)) :
        if L1[i] == cherche :
            c = c + 1

    if c > autre :
        autre = c
        courant = cherche




print(f"Le nombre le plus fréquent dans la liste est le : {courant} ({autre} x)")


""" ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Ne rien modifier apres cette ligne.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * / """
