#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 16:11:14 2021

@author: taral
"""
comp = 2+3j
comp_1 = 0+2j
comp_2 = 1+2j
print(f'''real={comp.real}, type(real)={type(comp.real)}, imag={comp.imag},type(imag)={(type(comp.imag))}\n''')

comp_add = comp_1+comp_2
print(f'add = {comp_add}\n')


comp_sub = comp_1-comp_2
print(f'sub = {comp_sub}\n')


comp_mul = comp_1*comp_2
print(f'mul = {comp_mul}\n')


comp_div = comp_1/comp_2
print(f'div = {comp_div}\n')

comp_pow = comp_1**comp_2
print(f'pow = {comp_pow}\n')

print(comp_1 == comp_2)
print(comp_1 != comp_2)
print('\n')

print(10+20j and 20+30j)
print(0+0j and 20+30j)
print(20+30j and 0+0j)
print(0+0j and 0+0j)
print(10+20j or 20+30j)
print(0+0j or 20+30j)
print(20+30j or 0+0j)
print(0+0j or 0+0j)
print(not 20+30j)
print(not 0+0j)
print('\n')

a = 10+20j
b = 10+200j
print(a is b)
print(a is not b)

print('\n')
print('3.0' in 'Python3.0.0')
print(10 in range(20))
print(10+2j in [10,12.33,'Python',10+2j])
print(10+2j in (10,12.33,'Python',10+2j))
print(10+2j in {10,12.33,'Python',10+2j})
print(10+2j in {10:0,12.33:9,'Python':23,10+2j:1})

