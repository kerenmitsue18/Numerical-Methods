"""
Created on Tue Apr 13 12:40:32 2021
UA:Métodos numericos
Tema: Método de Gauss Jordan
Profesor: Asdrúbal López Chau
Alumno: Keren Mitsue Ramírez Vergara

Descripción:Test de prueba a metodo de Gauss Jordan 
@author: Keren Mitsue Ramírez Vergara
"""


import numpy as np
from GaussJordan import GaussJordan as Jordan

a = np.array( [ [0,2,0,1],[2,2,3,2], [4,-3,0,1], [6,1,-6,-5] ], float)
b = np.array( [0,-2,-7,6], float )

g = Jordan()
X,A = g.gauss(a,b)

print("Solucion:\n ", X)
print("El arreglo A queda: \n", A)
