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

x = np.arange(-5, 5, 0.01)

f1= 4*x**2 + 4*x -1
f2= np.sin(3*x) - np.cos(8*x)

fig, axes = plt.subplots(2,1)

  # Generar la función f1(x)
axes[0].plot(x,f1, 
             linestyle = '-',
             linewidth = 0.5, 
             color = "#fc0f03",
             marker = '.',
             markersize = 1, 
             label = "f1(x)"
             )

  #Propiedades de la gráfica f1(x)
axes[0].set_title("Gráfica f(x)= 4x^2+ 4x-1",
                  family = "monospace",
                  color = "#ad0000", 
                  fontsize = 14, 
                  x = 0.5,
                  y = 0.5
    )

  #Generar la función f2(x)
axes[1].plot(x,f2,
             linestyle = '-',
             linewidth = 0.5, 
             color = "#a900f7", 
             marker = '.', 
             markersize = 1, 
             label = 'f2(x)'
             )

   # Propiedades de la gráfica f2(x)
axes[1].set_title("Gráfica f(x)= sin(3x)-cos(8x)", 
                  family = "Monospace", 
                  color = "#47006e",
                  fontsize = 14,
                  x = 0.5,
                  y = 0.5
                 )

  # Agregar cuadricula a cada gráfica
axes[0].grid()
axes[1].grid()

  # Agregar leyenda a cada gráfica
axes[0].legend()
axes[1].legend()


""" Algunos acercamientos para encontrar las raices de f1
   
    Intento 1
axes[0].set_xlim(-1.2,-2.5)
axes[0].set_ylim(-10,50)


    Intento 2
axes[0].set_xlim(-0.1,-1.10)
axes[0].set_ylim(-2,5)  

   Intento 3
axes[0].set_xlim(-0.1,-1.10)
axes[0].set_ylim(-2,5) 

   Intento 4
axes[0].set_xlim(-1.0,-2.0)
axes[0].set_ylim(-2,5)  

  Intento 5
axes[0].set_xlim(0,2)
axes[0].set_ylim(-2,5)  

  Intento 6
axes[0].set_xlim(0,0.4)
axes[0].set_ylim(-2,5)  

 Acercamientos para encontrar las raices de f2

  Intento 1
axes[1].set_xlim(-2,-3)
axes[1].set_ylim(-1,1)  

  Intento 2
axes[1].set_xlim(-2,-2.2)
axes[1].set_ylim(-1,1)  

  Intento 3
axes[1].set_xlim(-2.6,-2.9)
axes[1].set_ylim(-1,1)  

  Intento 4
axes[1].set_xlim(-0.5,0.2)
axes[1].set_ylim(-1,1)  


"""

   #Imprimir las raíces de las funciones 
print ("\nPara la función f(x)= 4x^2+ 4x-1")
print ("Las raíces se encuentran en: ", "\n r1: -1.2", "\n r2: 0.2")


print ("\nPara la función f(x)= sin(3x)-cos(8x)")
print ("Las raíces se encuentran en: ", 
       "\n r1: -5.000",
       "\t r2: -0.590", 
       "\t r3: -4.250",
       "\t r4: -4.080",
       "\t r5: -3.850",
       "\n r6: -2.820",
       "\t r7: -2.720",
       "\t r8: -2.175",
       "\t r9: -1.000",
       "\t r10: 0.940",
       "\n r11: -0.715",
       "\t r12: -0.418",
       "\t r13: -0.330",
       "\t r14: 0.140",
       "\t r15: 1.855",
       "\n r16: 2.200",
       "\t r17: 2.243",
       "\t r18: 3.450",
       "\t r19: 3.540",
       "\t r20: 3.551",
       "\n r11: 4.140",
       "\t r22: 4.700"
        )