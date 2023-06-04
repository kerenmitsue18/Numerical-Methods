# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 12:59:49 2021
UA: Métodos numéricos 
Profesor: Asdrubal López Chau
Alumno: Keren Mitsue Ramírez Vergara

Tema: Métodos para encontrar las raices de funciones
Descripción: Clase que contiene el metodo de Newtow- Raphson
@author: Keren Mitsue Ramírez Vergara
"""


import numpy as np
class MiNewtonRaphson:
    
    def __init__(self):
        pass
    
    # fx: función
    # dfx: derivada fx
    # x0: valor inicial
    # N: Número de iteraciones
    # tol: tolerancia de error
    def root(self, fx, dfx, x0, N, tol):
        
          # formato del archivo csv
        archivo = open("Resultados.csv","w") # w -> indica que se escribe sobre el archivo nuevo
        archivo.write("\n\n******** MÉTODO DE NEWTON - RAPHSON **********\n") 
          # mostrar en el archivo valores iniciales
        archivo.write("\n\n Valores iniciales: ")
        archivo.write("\nvalor inicial: {} \nNo. iteraciones: {} \ntolerancia de error: {} ".format(x0, N, tol))
        
          # campos de la tabla a generar
        titulo = "Iteración,xn, f(xn), dfx(xn), error \n"
        archivo.write(titulo)
        
        
        # i: iteraciones
        # xn: punto de aproximancion a la raíz
        i=0
        xn = x0
        for n in range(0, N): # ejecuta bloque hasta que se realicen N iteraciones
            i += 1 # incremento de iteración
            temp = xn # tem: variable temporal para indicar el punto actual de la raíz

            # la nueva aproximación se encuentra en la interseccion de la tangente de la curva 
            #en el punto y en el eje x
            xn = xn - fx(xn)/dfx(xn)  

            e = np.abs((xn-temp)/xn); # determinar error del algoritmo

              # mostrar en el archivo los datos obtenidos de cada itertación 
            archivo.write("{:.0f}, {:.3f},{:.3f}, {:.3f}, {:.3f} \n".format(i, xn, fx(xn), dfx(xn), e))

            if (e <= tol): # si e <= tol, se ha encontrado una aproximación a la raíz con la tolerancia de error indicada, 
                 # rompemos ciclo 
                 break
           # mostrar en el archivo la raíz encontrada con un marco de error mínimo
        archivo.write("\niteraciones: {:.0f}\n Raíz aproximada: {:.3f}\n error: {:.3f}".format(i,xn,e))
        archivo.close()  # se cierra el archivo 
            