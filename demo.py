#!/usr/bin/python3
 
# 第一个注释
print ("Hello, Python!") # 第二个注释
print ()
print (3E-2 , end = " ")
print (1 + 2j)
input ("\n\n按下 enter 键后退出。")
print ()
"""
import sys
print ('================Python import mode==========================')
print ('命令行参数为:')
for i in sys.argv:
    print (i)
print ('\n python 路径为' , sys.path)
"""
'''
from sys import argv,path

print ('path:', path)
'''
a, b, c, d = 20, 5.5, True, 4+3j
print(type(a), type(b), type(c), type(d))
a = 111
print ( isinstance(a, int) )
print (2 ** 5)