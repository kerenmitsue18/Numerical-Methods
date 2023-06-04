"""
UA: Metodos numéricos
Tema: Derivacion numérica
Profesor: Asdrúbal López Chau
Alumno: Keren Mitsue Ramirez Vergara
Descripción:  
Aplicacion para encontrar mínimos de funciones
Created on Wed May 19 10:12:13 2021

@author: Keren Mitsue Ramirez Vergara
"""

import numpy as np
from Deriva import Deriva

def fx(x):
    return np.power(x,2)

def fx2(x):
    return 2* np.sin(4*x* np.cos(7 * x-1))

d = Deriva()
xn = 0.5
alpha = 0.01
for i in range(100):
    xn = xn - alpha * d.derivar(fx, xn)
    print("f({:.3f}) = {:.4f} ".format(xn,fx(xn)))
    
    
for i in range(100):
    xn = xn - alpha * d.derivar(fx2, xn)
    print("f({:.3f}) = {:.4f} ".format(xn,fx(xn)))
    
    

