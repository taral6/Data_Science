#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 14:43:01 2021

@author: taral
"""

a = bool(0)
print(f'a = {a},type = {type(a)}, id = {id(a)}\n')

b = bool(10)
c = bool(11)
print(f'b = {b},type = {type(b)}, id = {id(b)}')
print(f'c = {c},type = {type(c)}, id = {id(c)}\n')

num1 = bool(0)
num2 = bool(3)

print(f'num1 = {num1},type = {type(num1)}, id = {id(num1)}')
print(f'num2 = {num2},type = {type(num2)}, id = {id(num2)}\n')
add = num1+num2
print(f'add = {add},type = {type(add)}, id = {id(add)}')
sub = num1-num2
print(f'sub = {sub},type = {type(sub)}, id = {id(sub)}')
mul = num1*num2
print(f'mul = {mul},type = {type(mul)}, id = {id(mul)}')
div = num1/num2
print(f'div = {div},type = {type(div)}, id = {id(div)}')
rem = num1//num2
print(f'rem = {rem},type = {type(rem)}, id = {id(rem)}')
quo = num1%num2
print(f'quo = {quo},type = {type(quo)}, id = {id(quo)}')
pow = num1/num2
print(f'pow = {pow},type = {type(pow)}, id = {id(pow)}\n')

great = num1>num2
print(f'great = {great},type = {type(great)}, id = {id(great)}')
less = num1<num2
print(f'less = {less},type = {type(less)}, id = {id(less)}')
great_e = num1>=num2
print(f'great_e = {great_e},type = {type(great_e)}, id = {id(great_e)}')
less_e = num1<=num2
print(f'less_e = {less_e},type = {type(less_e)}, id = {id(less_e)}\n')

eq = num1>=num2
print(f'eq = {eq},type = {type(eq)}, id = {id(eq)}')
n_eq = num1<=num2
print(f'n_eq = {n_eq},type = {type(n_eq)}, id = {id(n_eq)}\n')

print(True & True)
print(True | True)
print(True ^ False)
print(~True)
print(True<<2)
print(True>>2)

#print(int(False))
a = True
b = True
print(a is b)
print(a is not b)
#True or False? True
#print​ (a ​ is​ ​ not​ b)
a = False
b = True
print(a is b)
print(f'{a is not b}\n')
#True or False?
#True or False?
#True or False?
print(True in [1,2,3,True])
print(True in [0])
print(False in [1,2,3])
print(f'{False in (1,2,3,False)}\n')

print(False in {True:10, False:20, True:30})
print(False in {True:10, 0:20, True:30})
