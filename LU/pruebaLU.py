"""
Created on Wed Mar 24 13:12:19 2021
UA:Métodos numericos
Tema: Descomposicion LU
Profesor: Asdrúbal López Chau
Alumno: Keren Mitsue Ramírez Vergara

Descripción:pruebas a descomposición LU
@author: Keren Mitsue Ramírez Vergara
"""
import numpy as np
from LUDecomposition import LUDecomposition as LU

lu = LU()
'''
A = np.array( [[3, -0.1, -0.2],
               [0.1, 7.0, -0.3],
               [0.3, -0.2, 10]])

b = np.array([7.85, -19.3, 71.4 ])
'''
A = np.array( [[3, -1, 2],
               [1, 2, 3],
               [3, -2, -1]], float)

b = np.array([12, 7, 2 ], float)

x = lu.ludecomp( A, b, 1e-6)
print (x)

