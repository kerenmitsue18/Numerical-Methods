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

import sympy as sympy
from NewtonRaphsonSympy import NewtonRaphsonSym



fx = sym.sin(2*x)
nrs= NewtonRaphsonSym()
x0= -2.0
N= 5;
raiz= nrs.roo(fx, x0, N)
print ("La raiz es {:.3f}",format(raiz))