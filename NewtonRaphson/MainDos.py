"""
Created on Wed Feb 10 10:09:19 2021
UA:Métodos númericos
Tema: Método Newton Raphson
Profesor: Asdrúbal López Chau
Alumno: Keren Mitsue Ramírez Vergara

Descripción: clase para implementar el método de Newton Raphson 
@author: Keren Mitsue Ramírez Vergara
"""
import sympy as sym
from NewtonRaphsonSympy import NewtonRaphsonSym

def fx():
    x = sym.Symbol("x")
    return sym.sin(2*x) * sym.exp(-x) - sym.cos(sym.exp (x))


x0 = -3
nr = NewtonRaphsonSym()

xr = nr.root(fx, x0, 3) 
print("La raíz encontrada es: {:.4f}".format(xr))
    