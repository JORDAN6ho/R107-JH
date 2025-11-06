Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> jour = int(input("Saisir un jour :"))
Saisir un jour :3
>>> heure = int(input("Saisir une heure :"))
Saisir une heure :9
>>> minute = int(input("Saisir une minute :"))
Saisir une minute :18
>>> minute_total = 0
>>> minute_total = minute + (heure*60) +((jour - 1) * 1440)
>>> print(minute_total)
3438
