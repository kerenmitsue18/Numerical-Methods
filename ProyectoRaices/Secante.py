# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 12:59:49 2021
UA: Métodos numéricos 
Profesor: Asdrubal López Chau
Alumno: Keren Mitsue Ramírez Vergara

Tema: Métodos para encontrar las raices de funciones
Descripción: Clase que contiene el metodo de la secante

@author: Keren Mitsue Ramírez Vergara
"""

import numpy as np

class MiSecante:
    
    
    def __init__(self):
        pass

    #  fx la función a determinar raíz
    #  x_ant x0 x anterior
    #  x_act x1  x actual
    #  N número de iteraciones
    def root(self, fx, x_ant, x_act, tol):
        
          # formato del archivo csv
        archivo = open("Resultados.csv","w") # w -> indica que se escribe sobre el archivo nuevo
        archivo.write("\n\n******** MÉTODO DE LA SECANTE **********\n") 
        archivo.write("\n\n Valores iniciales: ")
          # mostrar en el archivo valores iniciales
        archivo.write("\n1° punto inicial: {} \n2° punto inicial: {} \ntolerancia de error: {} ".format(x_ant, x_act, tol))
        titulo = "Iteración,x, error \n"
        archivo.write(titulo)
        
        # e: iniciar valor de error con 100% sin realizar calculos
        # i: iteraciones
        # xnext: valor aproximado de raiz
        e = 100 
        i = 0
        xnext = 0 
        
        
        while e >= tol: # si el error es mayor a la tolerancia permitida, seguir ejecutando
            i+=1 # incremento de iteraciones
            fx_ant = fx(x_ant) # evaluacion de x_ant en la función
            fx_act = fx(x_act) # evaluacion de x_act en la función 
            
            #  Implementación de la formula
            xnext = x_act - (fx_act*(x_ant - x_act) / (fx_ant-fx_act))
            
            # calculo de error en el algoritmo
            e= np.abs(xnext - x_act)/xnext
            
            # mostrar en el archivo los resultados de cada iteración
            archivo.write("{:.0f}, {:.3f},{:.3f} \n".format(i, xnext, e))
            
            #  Actualización de los puntos x
            x_ant = x_act
            x_act = xnext
        
        # mostrar en el archivo la raíz aproximada 
        archivo.write("\niteraciones: {:.0f}\n Raíz aproximada: {:.3f}\n error: {:.3f}".format(i,xnext,e))
        archivo.close() # cerrar el archivo 
             
            
        