# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 10:00:12 2017

@author: LuisOsvaldo
"""

import numpy as np
print('Ingrese números separados por espacios: ')
arreglo = input()
new = arreglo.split(' ')
n = len(new)
#print(new)
#print(n) 
i = n-1
while i>=0:
    print(new[i])
    i -= 1
#Ahora lo haremos usando numpy.
print(' ')
print('Ahora lo haremos con numpy.')
aux=np.array(new)
y = aux[::-1]
print(y)

