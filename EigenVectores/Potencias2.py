
"""
Created on Fri Apr 16 08:42:51 2021
UA:Métodos numericos
Tema: Eigen- valores y eigen-vectores
Profesor: Asdrúbal López Chau
Alumno: Keren Mitsue Ramírez Vergara

Descripción:Metodo de las potencias Version 2
@author: Keren Mitsue Ramírez Vergara
"""


import numpy as np

A = np.array([[4,-1,1],
             [-1,3,-2],
             [1,-2,3]])

x0 = np.array([1,0,0])

N = 50
x = x0
for i in range (N):
    domx = np.max(np.abs(x))
    x = x/ domx # Normalizando el vector
    x = np.matmul(A, x)
evalor = x/np.max(np.abs(x))
print('Eigen-valor: ', np.max(np.abs(x)))
print('Eigen-Vector: ', evalor)

evector = x
# Comprobacion 
c = np.matmul(A,evector) - evalor * evector 
c = np.linalg.norm(c)
if (c < 1e-6):
    print ('si es eigen vector')

# print (c);
