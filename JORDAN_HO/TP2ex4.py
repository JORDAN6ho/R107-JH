BASE = 4
fromage = 800
eau = 2
pain = 400
ail = 2
nbConvives =int(input("Entrez le nombre de personne(s) conviées à la fondue :"))
fromage = fromage * nbConvives / BASE
eau = eau * nbConvives / BASE
pain = pain * nbConvives / BASE
ail = ail * nbConvives / BASE
print(f"Pour faire une fondue fribourgeoise pour {nbConvives} personnes il vous faut: \n-{fromage} gr de fromage \n-{eau} dl d'eau \n-{ail} gousse(s) d'ail \n-{pain} gr de pain")