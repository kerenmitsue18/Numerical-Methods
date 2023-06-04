"""
Created on Wed Feb 10 10:09:19 2021
UA:Métodos númericos
Tema: Método de regla falsa
Profesor: Asdrúbal López Chau
Alumno: Keren Mitsue Ramírez Vergara

Descripción: prueba del metodo de la regla falsa
@author: Keren Mitsue Ramírez Vergara
"""

import matplotlib.pyplot as plt
import numpy as np
from ReglaFalsa import MyReglaFalsa


def fx(x):
    return x**2 + x -1

x = np.arange (-3, 3, 0.1)
f = fx(x)
plt.plot(x,f)
plt.grid()

ReglaFalsa= MyReglaFalsa()

ReglaFalsa.root(fx, -2, -1, 0.0001)