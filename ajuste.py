# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 22:24:17 2017

@author: LuisOsvaldo

Prueba para ajustar curvas.
"""
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import math 
from scipy import optimize

data=pd.read_csv('muon2.txt',header=0)
x = data.ix[:,0]
x2 = x*2
#print(data)
#print(x)
#print(x2)
#plt.close('all') #Cierra todas las figuras abiertas
bins=50 #número de bins
"""Se grafica el histograma y se guardan algunos parámetros de este.
Se guardan en n, bin_positions y p"""
n, bin_positions, p = plt.hist(x2, bins, normed=False, label='datos 1',histtype="step", color="black", linewidth=1)

print(n)
#Se nombran los ejes
plt.xlabel('Tiempo (ns)')

#print(n)

"""Intentaremos otro ajuste"""
fitfunc = lambda p, x: np.exp(p[0]*x)
errfunc = lambda p, x,y: fitfunc(p,x) - y



"""Valor inicial"""
p0 = [-4.5e-4]


"""Time"""
time = np.linspace(x2.min(),x2.max(), 50)



"""Ajuste"""
p1, success = optimize.leastsq(errfunc,p0[:], args=(time, n))

print(p1)
"""Graficar el ajuste"""
plt.plot(time,n,time,fitfunc(p1, time))


