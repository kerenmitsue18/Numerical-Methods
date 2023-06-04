# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 09:12:19 2021

@author: Keren Mitsue Ramírez Vergara
"""

import numpy as np

#Función para calcular el error absoluto
def errorAbsoluto(valorReal, valorAproximado):
    return np.abs(valorReal - valorAproximado)


def errorRelativo (valorReal, valorAproximado):
    return errorAbsoluto(valorReal, valorAproximado)/np.abs(valorReal)


#Probando la función errorAbsoluto
print ("Error absoluto: ", errorAbsoluto(0.5,0.4))

#Probando la función errorRelativo
print ("Error relativo:", errorRelativo(0.5,0.4))

#como controlar el número de digitos después del punto decimal 
print ("Error absoluto: {:.5f} ".format( errorAbsoluto(0.5,0.4)))



