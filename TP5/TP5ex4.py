somme = int(input("Entrez une somme en euros : "))
billet100 = somme // 100
reste = somme % 100
billet50 = reste // 50
reste %= 50
billet10 = reste // 10
reste %= 10
piece2 = reste // 2
piece1 = reste % 2
print(f"{somme} euros, c’est donc {billet100} billets de 100, {billet50} de 50, "
      f"{billet10} de 10, {piece2} pièces de 2 et {piece1} pièce 1.")