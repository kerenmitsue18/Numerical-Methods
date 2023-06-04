"""
Created on Wed Mar 24 13:12:19 2021
UA:Métodos numericos
Tema: Main del método Gauss con pivoteo
Profesor: Asdrúbal López Chau
Alumno: Keren Mitsue Ramírez Vergara

Descripción:probar metodo de Gauss simple
@author: Keren Mitsue Ramírez Vergara
"""

import numpy as np
from GaussPivoteo import GaussPivoteo


#A = np.array([ [3,-0.1,-0.2],[0.1,7,-0.3], [0.3, -0.2, 10] ])
#b = np.array ( [7.85,-19.3,71.4])

A = np.array([ [3.0,-0.1,-0.2],[0.1,7.0,-0.3], [0.3, -0.2, 10.0] ])
b = np.array ( [7.85,-19.3,71.4])





n = A.shape[1] # numero de variables
x = np.zeros( (n,1))


tol = 0.00001
er = 0.00001

g = GaussPivoteo();
res = g.gauss(A, b, n , x, tol, er)
print("La solución es: \n ",res) 