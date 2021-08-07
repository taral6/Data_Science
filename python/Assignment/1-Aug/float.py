#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 16:55:20 2021

@author: taral
"""

a = 10.0
print(f'a = {a},type = {type(a)}, id = {id(a)}\n')

b = 2.4
c = 5.8
print(f'b = {b},type = {type(b)}, id = {id(b)}')
print(f'c = {c},type = {type(c)}, id = {id(c)}\n')


num1 = 5.9
num2 = 10.6

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
pow = num1**num2
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

print('\n')

print(f'10.0 and 20.2 ---> {10.0 and 20.2}')
print(f'0 and 20.1 ---> {0 and 20.1}')
print(f'20.5 and 0 ---> {20.5 and 0}')
print(f'0 and 0 ---> {0 and 0}')
print('\n')
print(f'10.9 or 20.5 ---> {10.9 or 20.5}')
print(f'0 or 20.6 ---> {0 or 20.6}')
print(f'20.7 or 0 ---> {20.7 or 0}')
print(f'0 or 0 ---> {0 or 0}')
print('\n')

#print(f'bool(0.0) ---> {bool(0.0)}')
print(not 10.20)
print(not 0.0)

#Bitwise operation does not work with float
#print(10.0 & 20.0)
#print(10.1 | 20.3)
#print(10.4 ^ 20.2)
#print(~10.2)
#print(10.2<<2)
#print(10.8>>2)

print('\n')

#True or False? True
#print​ (a ​ is​ ​ not​ b)
a = 1.1
b = 1.1
print(f'a = {a}, b= {b}, a is b  ---> {a is b}')
print(f'a = {a}, b= {b}, a is not b  ---> {a is not b}\n')
#True or False?
#Not working
print(f'a = {a}, b= {b}, id(a)-->{id(a)}, ib(b)-->{id(b)}\n')



print(2.1 in [1,2.1,3,True])
print(1.1 in [0])
print(4.1 in [1,2,3])
print(f'{False in (1,2,3,False)}\n')

print(4.2 in {1:10, 4.2:20, 3:30})
print(2.1 in {1:10, 2:20, 3:30})
print(10.1 in range(20))