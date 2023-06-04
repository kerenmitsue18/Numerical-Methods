# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 10:09:19 2021
UA:Métodos númericos
Tema: Método gráfico 
Profesor: Asdrúbal López Chau
Alumno: Keren Mitsue Ramírez Vergara

Descripción: Agregando elementos de la grafica 
@author: Keren Mitsue Ramírez Vergara
"""

import matplotlib.pyplot as plt
import numpy as np 
import time

def ft(t):
    return np.sin(t*3) + np.sin(t)
t= np.arange(-2,2,0.1)

fig, axs = plt.subplots(1,1)
axs.plot(t,ft(t))
axs.grid()

axs.text(-1.5,1.1, "raiz")


for k in range ( len(t) ):
    i = t[k]
    axs.clear()
    axs.text(0,1, "iteracion: {:.1f} ".format(k))
    axs.text(i, ft(i)+.1, "Raíz")
    plt.pause(0.5)
    circlulo = plt.Circle( (i,ft(i)), 0.09, color= 'r')
    
    
    