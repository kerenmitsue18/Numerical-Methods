"""
Created on Wed Feb 10 10:09:19 2021
UA:Métodos numericos
Tema: Sistema de ecuaciones lineales
Profesor: Asdrúbal López Chau
Alumno: Keren Mitsue Ramírez Vergara

Descripción: Repaso de listas, vectores y matrices
@author: Keren Mitsue Ramírez Vergara

Ax + By + C = 0 ----(1)
Dx + Ey + f = 0 ---(2)

Las ecuaciones (1) y (2) pueden escribirse en forma matricial 

Ax = b

A es una matrix con los coeficientes de X, Y 
B es un vector columna

2x - 4y + 2 = 0
5x+3y -1 = 0
"""

import numpy as np
# lista 

a =[1,2,3] # crear una lista 
len(a) # numero de elementos de la lista
a[0] # acceder a un elemento en una lista
a[2] 

#matrices
A=[[1, 2], [3, 4]]
A[0] # lista [1,2]
A[1]
A[0][1] # accede al 2
A[1][0] # accede al 3


# para realizar operaciones matriciales usamos numpy
x= np.array([3,4])
type(x) # tipo de dato
x.shape # forma del vector 1 renglón, 2 columnas
np.reshape(x, (2,1)) # cambiando la forma del vector ->vector columna

# creacion de una matriz en numpy

A = np.array([1,5,2,6])
np.reshape(A,(2,2))

#  Otra forma 
A = np.matrix([[1,5], [2,6]]) #objeto de tipo matriz

