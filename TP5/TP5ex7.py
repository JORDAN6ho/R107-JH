import os.path
import datetime

f1 = input("Entrez le nom du premier fichier : ")
f2 = input("Entrez le nom du deuxième fichier : ")
if os.path.isfile(f1):
    print(f"{f1} existe, taille :", os.path.getsize(f1), "octets")
else:
    print(f"{f1} n'existe pas.")
if os.path.isfile(f2):
    print(f"{f2} existe, taille :", os.path.getsize(f2), "octets")
else:
    print(f"{f2} n'existe pas.")
if os.path.isfile(f1) and os.path.isfile(f2):
    t1 = os.path.getmtime(f1)
    t2 = os.path.getmtime(f2)
    if t1 > t2:
        print(f"{f1} est le plus récent :", datetime.datetime.fromtimestamp(t1))
    else:
        print(f"{f2} est le plus récent :", datetime.datetime.fromtimestamp(t2))
