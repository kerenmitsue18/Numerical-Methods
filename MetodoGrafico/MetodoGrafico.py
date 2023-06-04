"""
Created on Wed Feb 10 10:09:19 2021
UA:Métodos numericos
Tema: Sistema de ecuaciones lineales
Profesor: Asdrúbal López Chau
Alumno: Keren Mitsue Ramírez Vergara

Descripción: metodo grafico 
@author: Keren Mitsue Ramírez Vergara
Ax + By + C = 0---(1)
Dx + Ey + F = 0---(2)

Las ecuaciones (1) y (2) pueden escribirse en forma matricial

Ax = b

A es un matriz con con los coeficientes de x, y
b es un vector columna


Solución de este sistema de ecuaciones.

Participación: Dado el siguiente sistema de ecuaciones, escribirlo en 
forma matricial usando numpy
2x - 4y + 2 = 0
5x + 3y - 1 = 0

"""

import numpy as np
import matplotlib.pyplot as plt

A = np.array([[2, -4], [5, 3]])
b = np.array([-2, 1])
b = np.reshape(b, (2, 1))

'''
Participación: Dado el siguiente sistema 
de ecuaciones, escribirlo en 
forma matricial usando numpy
1x - 2y + 5z + 3 = 0
4x + 1y + 2z + 7 = 0
-2x + 3y + 6z + 8 = 0
'''


class MetodoGrafico:

    def graficar(self, A, b):
        colores = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
        linea = ['_', '-', '.']
        r, c = A.shape
        b1 = b[0]
        a11 = A[0][0]
        a12 = A[0][1]
        x1 = np.arange(-5, 5, 0.01)
        y1 = (b1 - a11*x1)/a12
        
        fig, ax = plt.subplots()
        ax.plot(x1, y1, color = colores[0], marker=linea[0])
        b2 = b[1]
        a21 = A[1][0]
        a22 = A[1][1]
        x2 = x1
        y2 = (b2-a21*x2)/a22
        ax.plot(x2, y2)
'''
Modifcar la clase para que grafique automáticamente hasta
10 lineas.
'''
A = np.random.randint(-5, 5, (4,2))
b = np.random.randint(-3, 3, (4,1))
g = MetodoGrafico()

g.graficar(A, b)

