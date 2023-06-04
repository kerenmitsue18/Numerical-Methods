# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 12:59:49 2021
UA: Métodos numéricos 
Profesor: Asdrubal López Chau
Alumno: Keren Mitsue Ramírez Vergara

Tema: Métodos para encontrar las raices de funciones
Descripción: Clase con el método bisección 

@author: Keren Mitsue Ramírez Vergara
"""


import numpy as np


class MiBiseccion:

    def __init__(self):  # constructor 
        pass
    

    #  fx: la función a determinar raíz
    #  a: primer punto de intervalo
    #  b: segundo punto de intervalo
    #  tol: tolerancia de error para el algoritmo
    def root(self, fx, a, b, tol):
       
          # formato del archivo csv
        archivo = open("Resultados.csv","w")  # w -> indica que se escribe sobre el archivo nuevo
        archivo.write("\n\n******** MÉTODO DE LA BISECCIÓN**********\n") 
        archivo.write("\n\n Valores iniciales ")
          # mostrar en el archivo valores iniciales
        archivo.write("\nvalor primer intervalo: {} \nvalor segundo intervalo: {} \ntolerancia de error: {} ".format(a, b, tol))

          # campos de la tabla a generar
        titulo = "\n\nIteración, buscando, xi, xu, xr, ea, \n"
        archivo.write(titulo)
        
        
        if fx(a)*fx(b) < 0: 
            # si fx(a) * fx(b)< 0 -> la raiz se encuentra dentro de un subintervalo superior o derecho 
            pass
        
        else:
            
              # la raiz no se encuentra dentro del intervalo 
            
            com = fx(a)* fx(b) # com -> valor para comprobar que com < 0
              
             #indicamos en el archivo que no existe un cambio de signo 
            archivo.write("\n\nNo existe raíz en el intervalo proporcionado \n porque:\n"
                  "fx (a) * fx(b) > 0 \n {:.3f}".format(com))
            archivo.write("> 0 \n por lo tanto no hay un cambio de signo y el método no sigue con el algoritmo")
            return 
        
        
        # i: número de iteraciones  
        # xr: valor nuevo del subintervalo a buscar
        # xr_old: valor anterior del subintervalo a buscar
        i = 0 
        xr = a
        xr_old = b
        
        
          # si la distancia de los valores de los intervalos es mayor a la tolerancia indicada, continuar con el algoritmo 
          # de lo contrario, se deduce que los valores del intervalo se aproximan demasiado a la raíz
          
        while np.abs(xr - xr_old) > tol:  
            
            i +=1 # contador de iteraciones
            
            xr_old = xr # Penúltima aproximación de la raíz
            xr = (a + b)/2.0  #  Aproximación de la raíz 
            fa = fx(a) 
            fr = fx(xr)
            
            if (xr!=0):
               ea = np.abs( (xr - xr_old) /xr)*100 # calcular por cada nueva aproximación de la raíz, su error porcentual
               
               
            if fa*fr < 0:   # Buscando en la mitad izquierda
                #a = a
                b = xr  # b toma el nuevo valor de xr -> se recorre el intervalo a la izquierda 
                
                  # mostrar en el archivo cada iteración de busqueda izquierda
                archivo.write('{:.0f}, Izquierda, {:.3f}, {:.3f}, {:.3f},{:.3f} \n'.format(i, a, b, xr,ea))
                
            elif fa*fr > 0: # Bsucando en la mitad derecha 
                
                #b = b
                a = xr # a toma el nuevo valor de xr -> se recorre el intervalo a la derecha 
                
                  # mostrar en el archivo cada iteración de busqueda derecha
                archivo.write('{:.0f}, Derecha, {:.3f}, {:.3f}, {:.3f},{:.3f} \n'.format(i, a, b, xr,ea))
                
                
            else: #fa(a)*f(xr) == 0
                # Ya encontró la raíz
                pass
                ea=0 
            
          # mostrar en el archivo la raíz encontrada con un marco de error mínimo
        archivo.write("\niteraciones: {:.0f} \n raiz aproximada: {:.3f} \n con un marco de error de : {:.3f} ".format(i, xr, ea))
        
        
        archivo.close()  # se cierra el archivo 