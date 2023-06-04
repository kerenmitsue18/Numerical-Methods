#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UA: Metodos numéricos
Tema: Interpolación de Lagrange
Profesor: Asdrúbal López Chau
Alumno: tu nombre
Descripción:  
Multiplicación de polinomios

Created on Fri May 14 08:21:54 2021

@author: asdruballopezchau
"""
import numpy as np

def multPolinomios(coefP1, coefP2, ascending = True):
    if len(coefP1)> len(coefP2):
        p1 = coefP1
        p2 = coefP2
    else:
        p1 = coefP2
        p2 = coefP1
    if (not ascending ):
        p1.reverse();
        p2.reverse();
    

    p1 = np.array(p1)
    p2 = np.array(p2)
    ncoefs = len(p1) + len(p2) - 1
    matriz = np.zeros((ncoefs, ncoefs))
    j = 0
    for idxP2 in range(len(p2) - 1, -1, -1):
        renglon = p2[idxP2]*p1
        renglon = renglon.tolist()
        numZeros = ncoefs - len(p1) - j
        for i in range(len(renglon)):
            matriz[j, i + numZeros] = renglon[i]
        j += 1
    producto = np.sum(matriz, axis=0)
    producto = producto.tolist()
    if not ascending:
        producto.reverse()
    return producto

# prueba 1: (-x^4 + 2x^3 + 2x + 1) (x^2 - 3x)
p = multPolinomios([1, 2, 0, 2, -1], [0, -3, 1], ascending = True)
print(p)

# prueba 2: (x^2 - 3x) (-x^4 + 2x^3 + 2x + 1) 
p = multPolinomios([1, 2, 0, 2, -1], [0, -3, 1], ascending = False)
print(p)
# prueba 3: (7x^9 + 12x^3 + 1)(8x^5 + 3x^2 + 2x)

p = multPolinomios([7 , 0, 0, 0, 0, 0, 12, 0, 0, 1], [8 ,0 , 0, 3, 2, 0], ascending = True)
print(p)

p = multPolinomios([7 ,2], [8 ,4], ascending = True)
print(p)
    