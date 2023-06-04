"""
Created on Wed Mar 24 13:12:19 2021
UA:Métodos numericos
Tema: Descomposicion LU
Profesor: Asdrúbal López Chau
Alumno: Keren Mitsue Ramírez Vergara

Descripción:Explicacion de paso de valor y paso por referencia
@author: Keren Mitsue Ramírez Vergara
"""


import numpy as np

class B:
    
    def __init__(self):
        pass
    
    # con listas o arreglos np es paso por referencia
    def metodo1(self,x):
        x[0] = -1


y = [0, 0, 0, 0]
y = np.zeros(4)
print(y)
b = B()
b.metodo1(y)
print(y)

