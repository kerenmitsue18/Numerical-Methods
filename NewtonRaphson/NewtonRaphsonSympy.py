"""
Created on Wed Feb 10 10:09:19 2021
UA:Métodos númericos
Tema: Método Newton Raphson
Profesor: Asdrúbal López Chau
Alumno: Keren Mitsue Ramírez Vergara

Descripción: Método de newton Raphson con Sympy
Actividad: Modificar el método de Newton Raphson 
@author: Keren Mitsue Ramírez Vergara
"""
import sympy as sym
class NewtonRaphsonSym:
    
    def __init__(self):
        pass
    
    # fx: función
    # x0: valor inicial
    #  N: número de iteraciones

    def root (self, fx, x0, N):
        xn = x0
        x = sym.Symbol('x')
        dfx = sym.diff(fx(), x)
        for n in range (0, N):
            a = fx().evalf(subs = {x:xn})
            b = dfx.evalf(subs = {x:xn})
            xn = xn - (a / b)
        return xn