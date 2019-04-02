#!/usr/bin/python3
 
# 第一个注释
print ("Hello, Python!") # 第二个注释
print (3E-2 , end = " ")
a, b, c, d = 20, 5.5, True, 4+3j
print(type(a), type(b), type(c), type(d))
a = 111
print ( isinstance(a, int) )
print (2 ** 5)
t = ('a', 'b', 'c', 'd', 'e', ['a', 'b', 'c'], 'f', 'g')
#t[2] = 't'
print (t[5][1])
student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
print (student)
if 'Rose' in student :
    print('Rose在集合中')
else :
    print('Rose不在集合中')
a = set('abracadabra')
b = set('alacazam')
print(a ^ b)
dict = {x: x**2 for x in (2, 4, 6)}
print(tuple(b))
a = 60
b = 13
print (a<<2)