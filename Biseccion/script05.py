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

import matplotlib.pyplot as plt
import numpy as np

x = np.arange (-7.5, 7.5, 0.5)
f1 = 5 * x**2 + 3*x -2
f2 = np.sin(x)

fig, axes = plt.subplots(2,1)  # función para multiples tablas

  # Modificando el diseño de grafica f1
axes[0].plot(x, f1, 
             linestyle = '--',
             linewidth = 1,
             color = "#fceb26",
             marker ='*',
             markersize = 4,  
             markerfacecolor = "#cb82f5", # Color del marcador
             markeredgecolor = "#621d8a",
             label = 'f1(x)'
             )

  # Modificar las propiedades del titulo 
axes[0].set_title("f1 (x) = 5x2+3x-2",
                  fontsize = 14,
                  fontfamily = 'times',
                  color = "#621d8a",
                  rotation = 10,
                  x = 0.5,  # Controla el titulo de la gráfica en x
                  y= 0.5,  # Controla el titulo de la gráfica en y
                  )

axes[0].legend(loc={0.8, 0.1}, 
               labelcolor= "#621d8a") #Colocar leyenda en gráfica en (x,y)

axes[1].plot(x,f2,
             linestyle = "--",
             linewidth = 1,
             color = "#1d8a7d",
             marker = 'p',
             markersize = 6,
             markerfacecolor ="#d5ed4d" ,  # color interno de la marca
             markeredgecolor= "#0b8a00",  # Color de contorno de la marca
             label= 'f2(x)= sin(x)'
             )

for xlab in axes[0].get_xticklabels() :
    xlab.set_color("blue")
    xlab.set_fontsize(14)
    xlab.set_rotation(90)


for ylab in axes[0].get_yticklabels() :
    ylab.set_color("blue")
    ylab.set_fontsize(14)
    ylab.set_rotation(0)

