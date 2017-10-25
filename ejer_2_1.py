# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 17:23:43 2017

@author: LuisOsvaldo
Ejercicio 2 Mark II
Esta ya es la versión chidori. Hace la suma de los número pares mientras el 
número en la serie de fibonacci sea menor que 4000000.
"""

from time import time
suma = 0
ti = time()
def fib_iterative(n):
    a, b = 1, 2
    while n > 0:
        a, b = b, a + b
        n -= 1
    return a

#print([fib_iterative(i) for i in range(10)])

for j in range(2340):
    x = fib_iterative(j)
    if x >= 4000000:
        print('El primer elemento mayor que 4000000 es: ',j+1)
        break
    if x%2 == 0:
        suma = suma + x
    
print('La suma de los números pares es: ',suma)        
tf = time()
te = tf - ti
print('El tiempo que tarda es ', te, ' s')