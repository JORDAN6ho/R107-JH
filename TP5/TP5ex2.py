notes = []
coeffs = []
for i in range(1, 6):
    entree = input(f"Veuillez entrer la note du module {i} et le coefficient correspondant : ")
    valeurs = entree.split(" ")
    note = float(valeurs[0])
    coef = int(valeurs[1])
    notes.append(note)
    coeffs.append(coef)
somme = 0
coef_total = 0
for n, c in zip(notes, coeffs):
    somme += n * c
    coef_total += c
moyenne = somme / coef_total
admis = moyenne >= 10 and all([n >= 8 for n in notes])
print("Moyenne générale :", moyenne)
if admis:
    print("L’étudiant est admis.")
else:
    print("L’étudiant n’est pas admis.")