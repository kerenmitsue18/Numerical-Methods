# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 10:09:19 2021
UA:Métodos númericos
Tema: Método gráfico 
Profesor: Asdrúbal López Chau
Alumno: Keren Mitsue Ramírez Vergara

Descripción: Segunda práctica con pyplot
@author: Keren Mitsue Ramírez Vergara
"""


import matplotlib.pyplot as plt 
import numpy as np
 
start = -10  # inicio de x
end = 10  # fin de x
step = 0.01  # paso
 
x = np.arange(start, end, step)
fx= 5 * x ** 2 + 3 * x - 2 
 
fig, axes = plt.subplots()
axes.plot(x, fx)
axes.grid()
axes.set_title("Grafica de f (x)= 5x^2+3x-2")
axes.set_xlabel("x")
axes.set_ylabel("f (x)")
axes.set_xlim(-1.12,0.50)  # Simula zoom en x 
axes.set_ylim(-2.5,2.5)  # Simula zoom en y

