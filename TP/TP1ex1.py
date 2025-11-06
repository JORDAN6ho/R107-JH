Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> nom = "HO"
>>> prenom = "JORDAN"
>>> math = 20
>>> anglais = 17
>>> info = 15
>>> promotion = 10
>>> 
>>> type(nom)
<class 'str'>
>>> type(prenom)
<class 'str'>
>>> type(math)
<class 'int'>
>>> type(anglais)
<class 'int'>
>>> type(info)
<class 'int'>
>>> type(promotion)
<class 'int'>
>>> m
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    m
NameError: name 'm' is not defined
>>> m =
SyntaxError: invalid syntax
>>> m = 0
>>> m = (math + anglais + info)/3
>>> print('L étudiant', nom , prenom, 'de la promotion', promotion , 'a une moyenne de', m)
L étudiant HO JORDAN de la promotion 10 a une moyenne de 17.333333333333332
>>> promotion = 2025
>>> print('L étudiant',nom,prenom,'de la promotion',promotion,'a une moyenne de', m)
L étudiant HO JORDAN de la promotion 2025 a une moyenne de 17.333333333333332
