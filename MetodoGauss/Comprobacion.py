"""
Created on Wed Mar 24 13:12:19 2021
UA:Métodos numericos
Tema: Descomposicion LU
Profesor: Asdrúbal López Chau
Alumno: Keren Mitsue Ramírez Vergara

Descripción:probar metodo de Gauss simple
@author: Keren Mitsue Ramírez Vergara
"""
import numpy as np 

A = [[3,-0.1,-0.2], [0.1,7,-0.3], [0.3, -0.12, 10]]
A = np. array(A)
U = [[3, -0.1, -0.2], [0,7.003,-0.29], [0,0,10.02]]
U = np.array(U)
L = [[1,0,0], [0.0333,1,0], [0.1,-0.02713,1]]

L = np.array(L)

A = np.matmul(L,U)
print (A)
er = A - np.matmul(L,U)
print ("Error: ")
print(er)