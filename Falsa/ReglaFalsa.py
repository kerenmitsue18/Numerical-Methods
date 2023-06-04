# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 10:09:19 2021
UA:Métodos númericos
Tema: Método de regla falsa
Profesor: Asdrúbal López Chau
Alumno: Keren Mitsue Ramírez Vergara

Descripción: clase que implementa metodo regla falsa 
@author: Keren Mitsue Ramírez Vergara
"""
import numpy as np
class MyReglaFalsa:
    
    def __init__(self):
       pass
       
    
    def root(self, fx, a, b, tol): 
        if fx(a)*fx(b) > 0:
            print("No se encuentra en el intervalo proporcionado: {:.3f}, {:.3f}".format(a, b))
            return 
    
        xr = a
        xr_old = b
        while (np.abs(xr - xr_old) > tol): 
            xr_old = xr
            fa = fx(a)
            fb = fx(b)
            xr = b - fb * ( a - b )/ (fa - fb)
            fxr = fx (xr)
            if fa* fxr < 0: #  Izquierda
                b = xr
            elif fa * fxr >0: #Derecha
                a = xr
        print ("Raiz encontrada: {:.3f}".format(xr))
                
            
            