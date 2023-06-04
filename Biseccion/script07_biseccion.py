# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 10:09:19 2021
UA:Métodos númericos
Tema: Método gráfico 
Profesor: Asdrúbal López Chau
Alumno: Keren Mitsue Ramírez Vergara

Descripción: Probando método de biseccion 
@author: Keren Mitsue Ramírez Vergara
"""
import matplotlib.pyplot as plt
from script06_poo import MiBiseccion
import numpy as np

def fx(x):
    return x**2 + x -1

x = np.arange (-3, 3, 0.1)
f = fx(x)
plt.plot(x,f)
plt.grid()

biseccion= MiBiseccion()

biseccion.root(fx, -2, -1, 0.0001)