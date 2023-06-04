
"""
Created on Fri Apr 16 08:42:51 2021
UA:Métodos numericos
Tema: Eigen- valores y eigen-vectores
Profesor: Asdrúbal López Chau
Alumno: Keren Mitsue Ramírez Vergara

Descripción:Metodo de las potencias 
@author: Keren Mitsue Ramírez Vergara
"""


import numpy as np

A = np.array([[4,-1,1],
             [-1,3,-2],
             [1,-2,3]])

x = np.array([1,0,0])
"""
x1= np.matmul(A,x0)
x2= np.matmul(A,x1)
x3= np.matmul(A,x2)
x4= np.matmul(A,x3)
x5= np.matmul(A,x4)
x6= np.matmul(A,x5)
# El valor caracteristico es 
lamda1 = x6[0]/x5[0]
b1 = x6/np.max(x6)
"""
n = 6
for i in range (n):
    x0 = x.copy()
    x0 = x0/np.matmuL(x0)
    x = np.matmul(A,x)
    
    
lambda1 = x[0]/x0[0]
b1 = x/np.max(x)

print (lambda1)
print(b1)