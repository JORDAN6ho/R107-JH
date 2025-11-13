jour = int(input("Saisir un jour :"))
heure = int(input("Saisir une heure :"))
minute = int(input("Saisir une minute :"))
minute_total = 0
minute_total = minute + (heure*60) +((jour - 1) * 1440)
print(minute_total)
