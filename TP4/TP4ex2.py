nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))
moy = 0.0
notes = []
for i in range(nombreEtudiants):
    note = float(input(f"Note étudiant {i+1} : "))
    while note < 0 or note > 20:
        print("Erreur : une note doit être comprise entre 0 et 20 !")
        note = float(input(f"Note etudiant {i} : "))
    notes.append(note)
    moy = moy + note

moy = moy / nombreEtudiants

print(f"Moyenne de classe : {moy}")

print("Numéro de l’Etudiant | note | ecart a la moyenne")
for i in range(nombreEtudiants):
    ecart = notes[i] - moy
    print(f"{i} | {notes[i]} | {round(ecart, 2)}")


