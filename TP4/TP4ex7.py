binome = ("login1", "login2")
print(f"L’étudiant {binome[0]} est en binome avec l’étudiant {binome[1]}")
nouveau = input("Nouveau login : ")
try:
    binome[1] = nouveau
except:
    print("Impossible : les tuplets ne sont pas modifiables !")
try:
    del binome[1]
except:
    print("Impossible : un tuplet ne peut pas être modifié ou supprimé élément par élément.")
binome = binome + (nouveau,)
print("Nouveau tuplet :", binome)
