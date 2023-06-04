"""
Created on Wed Feb 10 10:09:19 2021
UA:Métodos númericos
Tema: Método Newton Raphson
Profesor: Asdrúbal López Chau
Alumno: Keren Mitsue Ramírez Vergara

Descripción: clase para implementar el método de Newton Raphson 
@author: Keren Mitsue Ramírez Vergara
"""

class NewtonRaphson:
    
    def __init__(self):
        pass
    # fx: funcion 
    # dfx: derivada fx
    # x0: valor inicial 
    # N: numero de iteraciones
    
    def root (self, fx, dfx, x0, N):
        xn = x0
        for n in range (0, N):
            xn = xn - fx(xn)/dfx(xn)
        return xn