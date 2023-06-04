# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 10:09:19 2021
UA:Métodos númericos
Tema: Método gráfico 
Profesor: Asdrúbal López Chau
Alumno: Keren Mitsue Ramírez Vergara

Descripción: POO con python
@author: Keren Mitsue Ramírez Vergara
"""

import numpy as np
# clase bisección
class MiBiseccion:
    
    def __init__(self):   # constructor  self==this 
        print ("Constructor")
        
    def root(self, fx, a, b, tol):
          # pass  se coloca para indicar que no hay nada en la función 
          print (fx(a))
          print (fx(b))
          if fx(a)* fx(b) < 0:
              print ("Existe raiz en el intervalo [", a, ",", b,"]")
              
          else: 
              print ("No se encuentra en el intervalo")
              return
          
          i = 0
          xr = a
          xr_old = b
          while np.abs(xr - xr_old) > tol:
            i = i + 1
            # Mostrar el invervalo de búsqueda  con 4 decimales
            #print("Buscando en [",a, " , ", b, "]")
            print('Buscando en [{:.4f}, {:.4f}]'.format(a, b))
            xr_old = xr # Penúltima aproximación de la raíz
            xr = (a + b)/2.0 #  Aproximación de la raíz 
            fa = fx(a)
            fr = fx(xr)
            if fa*fr < 0:   # Mitad izquierda
                print('Buscar en mitad izquierda')
                #a = a
                b = xr
            elif fa*fr > 0: # Mitad derecha
                print('Buscar en mitad derecha')
                a = xr
                #b = b
            else: #fa(a)*f(xr) == 0
                # Ya encontró la raíz
                print("Raíz encontrada: ", xr)
          print("Raíz encontrada: ", xr)                
              
              