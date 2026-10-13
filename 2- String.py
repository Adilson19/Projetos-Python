Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s = 'minha primeira string'
>>> s
'minha primeira string'
>>> 'algomania'.lower()
'algomania'
>>> 'algomania'.upper()
'ALGOMANIA'
>>> 'algomania'.startswith(mania)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    'algomania'.startswith(mania)
NameError: name 'mania' is not defined
>>> 'algomania'.startswith('mania')
False
>>> ''
KeyboardInterrupt
>>> 'algomania'.endswith('mania')
True
>>> 'algomania'.endswith('algo')
False
>>> d = 'teste1', 'teste2', 'teste3'
>>> d.split(',')
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    d.split(',')
AttributeError: 'tuple' object has no attribute 'split'
>>> d = 'teste1,teste2, teste3'
>>> d.split(',')
['teste1', 'teste2', ' teste3']
>>> ' teste '.strip()
'teste'
>>> ' teste '.rstrip()
' teste'
>>> ' teste '.lstrip()
'teste '
>>> 'teste'.title()
'Teste'
>>> s = '0123456789'
>>> s[0]
'0'
>>> s[5]
'5'
>>> s[0:5]
'01234'
>>> s[1:5]
'1234'
>>> s[::-1]
'9876543210'
>>> 
