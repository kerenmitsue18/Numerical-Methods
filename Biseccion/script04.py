# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 10:09:19 2021
UA:Métodos númericos
Tema: Método gráfico 
Profesor: Asdrúbal López Chau
Alumno: Keren Mitsue Ramírez Vergara

Descripción: Personalización de gráficas
@author: Keren Mitsue Ramírez Vergara
"""


import matplotlib.pyplot as plt  # Clase para graficar
import numpy as np  # Clase para realizar cálculos numéricos

x=np.arange(-10,10,0.1) # Colocar un rango de intervalo
fx= 5* x**2 +3*x -2   #Función a graficar

fig, axes=plt.subplots() # graficador, return figure and axes

axes.grid()  # Propiedad de cuadriculado 
axes.plot(x, fx, '+:m')  # markers, line styles, color
axes.set_title ("Grafica f(x)= 5x^2+3x-2")
axes.set_xlabel('x')
axes.set_ylabel ('Y')

axes.set_xlim(-4.0,4)  # Simula zoom en eje x
axes.set_ylim(-10,80)  # Simula zoom en eje y

