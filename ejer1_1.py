# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 15:55:39 2017

@author: LuisOsvaldo
Versión Mark 2
Este es el bueno.
"""

from time import time
sum2 = 0
ti= time()
for i in range(1000):
    if i%3 == 0 or i%5 == 0:
        sum2 = sum2 + i
print('La suma de los múltiplos de 3 o 5 es: ',sum2)
tf = time()
te = tf - ti
print('El tiempo ', te, ' s')