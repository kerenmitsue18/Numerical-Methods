"""
Created on Wed Apr 21 10:19:22 2021
UA:Métodos numericos
Tema: Eigen- valores y eigen-vectores
Profesor: Asdrúbal López Chau
Alumno: Keren Mitsue Ramírez Vergara

Descripción:
-Modelo lineal semi-lineal
@author: Keren Mitsue Ramírez Vergara
"""

import numpy as np
from matplotlib import pyplot as plt

# definir parametros del modelo lineal 
m = 1 # pediente
b = 0 # cruce con el eje y
x = np.arange(-1,10,0.5)
y = m * x + b
fig, axis =  plt.subplots(2)
axis[0].plot(x,y,'-b')
axis[0].grid()
axis[0].axis('equal')

# modelo con datos no lineales
epsilon = np.random.randn(len(x))
y2 = m * x + b + epsilon
axis[1].plot(x,y2,'-ob')
axis[1].grid()
axis[1].axis('equal')


