Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
my_array[-1, 2, 3, 5, 456]
Traceback (most recent call last):
  File "<pyshell#0>", line 2, in <module>
    my_array[-1, 2, 3, 5, 456]
NameError: name 'my_array' is not defined
>>> my_array = [-1, 2, 3, 5, 456]
>>> my_array = [1, 2, 3, 4, 'true', False, True, 0.1]
>>> my_array
[1, 2, 3, 4, 'true', False, True, 0.1]
>>> my_array[0]
1
>>> my_array[-1]
0.1
>>> my_array[1:3]
[2, 3]
>>> len(my_array)
8
>>> my_array.sort()
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    my_array.sort()
TypeError: '<' not supported between instances of 'str' and 'int'
>>> my_array = [7,6,5,4,3,2,1]
>>> my_array.sort()
>>> my_array
[1, 2, 3, 4, 5, 6, 7]
>>> sorted(7,6,5,4,3,2,1)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    sorted(7,6,5,4,3,2,1)
TypeError: sorted expected 1 arguments, got 7
>>> my_array = [3,5,2,1,-1]
>>> sorted(my_array)
[-1, 1, 2, 3, 5]
>>> my_array
[3, 5, 2, 1, -1]
>>> my_array.sort()
>>> my_array
[-1, 1, 2, 3, 5]
>>> my_array.insert(0, 999)
>>> my_array
[999, -1, 1, 2, 3, 5]
>>> my_array.append(456)
>>> my_array
[999, -1, 1, 2, 3, 5, 456]
>>> my_array.remove(999)
>>> my_array
[-1, 1, 2, 3, 5, 456]
>>> my_array[1] = none
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    my_array[1] = none
NameError: name 'none' is not defined
>>> my_array[1] = None
>>> my_array
[-1, None, 2, 3, 5, 456]
>>> del my_array[1]
>>> my_array
[-1, 2, 3, 5, 456]
>>> min(my_array)
-1
>>> max(my_array)
456
>>> my_array.sort()
>>> my_array
[-1, 2, 3, 5, 456]
>>> import bisect
>>> bisect.bisect(my_array, 5)
4
>>> # O(n log n)
>>> # O (log n)
>>> bisect.insort(my_array,888)
>>> bisect.bisect(my_array,888)
6
>>> my_array
[-1, 2, 3, 5, 456, 888]
>>> my_array
[-1, 2, 3, 5, 456, 888]
>>> my_array range(0, 100)
SyntaxError: invalid syntax
>>> my_array.range(0, 100)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    my_array.range(0, 100)
AttributeError: 'list' object has no attribute 'range'
>>> my_array
[-1, 2, 3, 5, 456, 888]
>>> range(0, 100)
range(0, 100)
>>> my_array = range(100)
>>> my_array
range(0, 100)
>>> list(my_array)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
>>> two_dimentions_array = [[123, 456], [789, 321]]
>>> two_dimentions_array[0][0]
123
>>> two_dimentions_array[1]
[789, 321]
>>> A = [1, 2, 3]
>>> B = A
>>> A
[1, 2, 3]
>>> B
[1, 2, 3]
>>> B[0] = 999
>>> B
[999, 2, 3]
>>> A
[999, 2, 3]
>>> a = [1, 2, 3]
>>> b = list(a)
>>> b[0] = 999
>>> a
[1, 2, 3]
>>> b
[999, 2, 3]
>>> a = [1, 2, 3]
>>> b = a
>>> b = list(a)
>>> a = [{'test':123, 'bbb':456}]
>>> a
[{'test': 123, 'bbb': 456}]
>>> b = a
>>> b[0]['test'] = 999
>>> a
[{'test': 999, 'bbb': 456}]
>>> b
[{'test': 999, 'bbb': 456}]
>>> a = [{'test':123, 'bbb':456}]
>>> import copy
>>> b = copy.copy(a)
>>> b[0]['test'] = 999
>>> a
[{'test': 999, 'bbb': 456}]
>>> a = [{'test':123, 'bbb':456}]
>>> b = copy.deepcopy(a)
>>> b[0]['test'] = 999
>>> a
[{'test': 123, 'bbb': 456}]
>>> a = [1, 2, 3, 4]
>>> tmp1 = a[1]
>>> tmp2 = a[2]
>>> a[2]
3
>>> a[2] = tmp1
>>> a[1] = tmp2
>>> a
