dic = {
    "firstname": "titi",
    "name": "toto",
    "promo": 2022,
    "group": 202
}
print(f"votre nom est '{dic['name']}', prénom est '{dic['firstname']}', "
      f"vous faites partie de la promo '{dic['promo']}' et votre groupe est '{dic['group']}'.")

print("Les clés du dictionnaire sont :")
for k in dic.keys():
    print("-", k)
print("Les valeurs du dictionnaire sont :")
for v in dic.values():
    print("-", v)
print("Les tuplets du dictionnaire sont :")
for item in dic.items():
    print("-", item)

perso1 = dic
perso2 = {
    "firstname": "tata",
    "name": "tutu",
    "promo": 2023,
    "group": 102
}
binome = {
    "id1": perso1,
    "id2": perso2
}
print("\nLes étudiants formants le binôme sont :")
for etu in binome.values():
    print(f"- L'étudiant {etu['name']} {etu['firstname']} du groupe {etu['group']}")
