"""
Created on Wed Mar 17 10:09:19 2021
UA:Métodos numericos
Tema: Implementación del Método de Gauss simple
Profesor: Asdrúbal López Chau
Alumno: Keren Mitsue Ramírez Vergara

Descripción:probar metodo de Gauss simple
@author: Keren Mitsue Ramírez Vergara
"""

import numpy as np
from Gauss import Gauss

A = np.array([ [2,3],[3,-1] ])
b = np.array ( [5,2])

# A = np.array([ [0,2,3],[4,6,7], [2,1, 6] ])
# b = np.array ( [0,-3,5])


g = Gauss()
x = g.solve(A, b)
print("La solución es: \n ",x) 