Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> x = 3
>>> y = 0
>>> print(x,y)
3 0
>>> y = 2*x
>>> print(x,y)
3 6
>>> y = 5*y + x
>>> print(x,y)
3 33
>>> y = y%7
>>> print(x,y)
3 5
>>> y = 4 + x
>>> print(x,y)
3 7
>>> x += 4
>>> print(x,y)
7 7
>>> y += x
>>> print(x,y)
7 14
>>> y %= x+1
>>> print(x,y)
7 6
>>> y = 5*(x+y)
>>> print(x,y)
7 65
