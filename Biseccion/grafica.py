# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 12:59:49 2021
UA: Métodos numéricos 
Profesor: Asdrubal López Chau
Alumno: Keren Mitsue Ramírez Vergara

Descripción: Encontrar las raíces de dos funciones 
con el método gráfico y graficar con pyplot

@author: Keren Mitsue Ramírez Vergara
"""
import matplotlib.pyplot as plt
import numpy as np

x = np.arange (-2.5, 0.5 ,0.01)
fx= x**2 + x -1

fig, axs= plt.subplots()
axs.plot(x,fx)
axs.grid()
