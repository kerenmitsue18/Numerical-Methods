
"""
Created on Fri Apr 16 08:42:51 2021
UA:Métodos numericos
Tema: Eigen- valores y eigen-vectores
Profesor: Asdrúbal López Chau
Alumno: Keren Mitsue Ramírez Vergara

Descripción:Comprobar ejercicio de clse
@author: Keren Mitsue Ramírez Vergara
"""


import numpy as np

A= np.array([[4,1],[-6,-3]])

lamba1 = 3 # eigen-valor 

b1 = np.array([1,-1])

np.matmul(A,b1)
x = np.matmul(A,b1) - b1* lamba1

lamba2 = -2 # eigen-valor 
b2 = np.array([-1,6])
y = np.matmul(A,b2) - b2* lamba2
