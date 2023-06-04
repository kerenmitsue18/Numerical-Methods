"""
Created on Wed Feb 10 10:09:19 2021
UA:Métodos numericos
Tema: Sistema de ecuaciones lineales
Profesor: Asdrúbal López Chau
Alumno: Keren Mitsue Ramírez Vergara

Descripción: metodo grafico 
@author: Keren Mitsue Ramírez Vergara
"""

import matplotlib.pyplot as plt
import numpy as np
import time


def ft(t):
    return np.sin(t*3)+np.cos(t)
t = np.arange(-2, 2, 0.1)


fig, axs = plt.subplots(1, 1)
axs.plot(t, ft(t))
axs.grid()
# Agregando texto
axs.text(-1.5, 1+.1, "Raiz")

for k in range(len(t)):
    i = t[k]
    axs.clear()
    axs.plot(t, ft(t))
    axs.text(-2, 1.5, "Iteración: {:.1f}".format(k))
    circulo = plt.Circle((i, ft(i)), 0.09, color='r')
    axs.text(i, ft(i)+.1, "Raiz")
    axs.add_patch(circulo)    
    plt.pause(0.3)
    
