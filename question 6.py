Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> len1 = float(input("Enter length of side 1: "))
... len2 = float(input("Enter length of side 2: "))
... len3 = float(input("Enter length of side 3: "))
... if len1 + len2 > len3 and len2 + len3 > len1 and len1 + len3 > len2:
...     print("Yes")
... else:
