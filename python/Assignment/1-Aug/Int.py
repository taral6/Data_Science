#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 16:55:20 2021

@author: taral
"""

a = 10
print(f'a = {a},type = {type(a)}, id = {id(a)}\n')

b = 200
c = 200
print(f'b = {b},type = {type(b)}, id = {id(b)}')
print(f'c = {c},type = {type(c)}, id = {id(c)}\n')

p = -4
q = -4
print(f'p = {p},type = {type(p)}, id = {id(p)}')
print(f'q = {q},type = {type(q)}, id = {id(q)}\n')



num1 = 4
num2 = 5

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

print(f'10 and 20 ---> {10 and 20}')
print(f'0 and 20 ---> {0 and 20}')
print(f'20 and 0 ---> {20 and 0}')
print(f'0 and 0 ---> {0 and 0}')
print('\n')
print(f'10 or 20 ---> {10 or 20}')
print(f'0 or 20 ---> {0 or 20}')
print(f'20 or 0 ---> {20 or 0}')
print(f'0 or 0 ---> {0 or 0}')
print('\n')


print(10 & 20)
print(10 | 20)
print(10 ^ 20)
print(~10)
print(10<<2)
print(10>>2)

print('\n')

#print(int(False))
a = 10
b = 10
print(a is b)
print(a is not b)
#True or False? True
#print​ (a ​ is​ ​ not​ b)
a = 1000
b = 1001
print(f'a = {a}, b= {b}, a is b  ---> {a is b}')
print(f'a = {a}, b= {b}, a is not b  ---> {a is not b}\n')
#True or False?
#True or False?
#True or False?
print(2 in [1,2,3,True])
print(1 in [0])
print(4 in [1,2,3])
print(f'{False in (1,2,3,False)}\n')

print(4 in {1:10, 2:20, 3:30})
print(2 in {1:10, 0:20, 3:30})
print(10 in range(20))

print(10+(10*32)//2**5&20+(~(-10))<<20)
print(5&20)
#print(5&20)

a = 0b1010000
print(a)