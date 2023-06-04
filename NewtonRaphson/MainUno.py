"""
Created on Wed Feb 10 10:09:19 2021
UA:Métodos númericos
Tema: Método Newton Raphson
Profesor: Asdrúbal López Chau
Alumno: Keren Mitsue Ramírez Vergara

Descripción: clase para implementar el método de Newton Raphson 
@author: Keren Mitsue Ramírez Vergara
"""
import matplotlib.pyplot as plt
import sympy as sym
import numpy as np
from NewtonRaphson import NewtonRaphson

def fx(x):
    return np.sin (2* x) * np.exp(-x) - np.cos(np.exp(x))

def dfx(x):
    return -np.exp(-x) - 1


fig, axs= plt.subplots(1,1)
x = np.arange(-5,5, 0.1)
axs. plot(x,fx(x))




nr = NewtonRaphson()
x0 = 0

xr = nr.root(fx, dfx, x0, 3) 
print("La raíz encontrada es: {:.4f}".format(xr))
    
