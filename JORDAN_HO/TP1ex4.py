Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> x = "Sa"
>>> print (x,y)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    print (x,y)
NameError: name 'y' is not defined
>>> y = x + "lut"
>>> print(x,y)
Sa Salut
>>> y = y+"\n\tCesar"
>>> print(x,y)
Sa Salut
	Cesar
>>> x+= "lut"+"Jules"
>>> print(x,y)
SalutJules Salut
	Cesar
>>> y=len(x)
>>> print(x,y)
SalutJules 10
>>> y = len("BonjourJuju")
>>> print(x,y)
SalutJules 11
>>> y = "Salut"*2
>>> print(x,y)
SalutJules SalutSalut
>>> x = len(y)
>>> print(x,y)
10 SalutSalut
>>> y.strip()
'SalutSalut'
>>> print(x,y)
10 SalutSalut
>>> y = y.strip()
>>> print(x,y)
10 SalutSalut
>>> print(y)
SalutSalut
