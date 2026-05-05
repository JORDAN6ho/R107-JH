
nbmensualites =
mensualites = (montant*taux*((1+taux)**len()))/((1+taux)**len())-1
interets =

print(f"Calcul d'un prêt immobilier ou d'un crédit à la consommation")
montant = int(input("Entrer le montant du prêt ou crédit : "))
taux = int(input("Entrer le taux annuel en % : ")
print(f"La mensualité avec intérêts est de {mensualites} "))
print(f"Le montant des intérêts remboursés sont de {interets} euros")
print(f"le taux annuel est de {(taux/12)/100}")
