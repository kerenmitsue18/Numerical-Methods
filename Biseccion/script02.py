# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 10:09:19 2021
UA:Métodos númericos
Tema: Método gráfico 
Profesor: Asdrúbal López Chau
Alumno: Keren Mitsue Ramírez Vergara

Descripción: Primera práctica con pyplot
@author: Keren Mitsue Ramírez Vergara
"""


import matplotlib.pyplot as plt   # importar clase para graficar
import numpy as np  # importar clased para cálculos numéricos
 
start = 0  # inicio de x
end = 4  # fin de x
step = 0.1  # paso
 
x = np.arange(start, end, step)
fx= 5 * x ** 2 + 3 * x - 2 
 
plt.plot(x,fx)  # Valores a graficar
plt.grid()  # Agregar cuadricula a la gráfica
plt.xlabel("x")  # 
plt.ylabel("fx")
plt.title("Grafica de la función") 

