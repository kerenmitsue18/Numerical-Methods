
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 12:59:49 2021
UA: Métodos numéricos 
Profesor: Asdrubal López Chau
Alumno: Keren Mitsue Ramírez Vergara

Tema: Métodos para encontrar las raices de funciones
Descripción: Clase para graficar

@author: Keren Mitsue Ramírez Vergara
"""

import matplotlib.pyplot as plt # importar clase para graficar
import numpy as np # importar clase para funciones matemáticas
import time  # importar clase de tiempo 

class MiGrafica: 
    
    
    def __init__(self):  #constructor
        pass
    

    def root(self, funcion, x0, x1, step): # método para graficar
        
        
        
        
        x = np.arange (x0, x1, step) #genera valores entre x0, x1, con un paso en especifico
        
        fig, axes = plt.subplots(1,1) # generar una figura para graficar
        
          # seleccionar un titulo para la función a graficar
        if funcion == 1:
            text = " f(x) = X^2" 
        elif funcion == 2:
            text = " f(x) = sin(x) + cos(5x)" 
        elif funcion == 3:
            text = " f(x)= x^3 - 5x^2 + 7x -3"
        else: 
            pass
        
          # seleccionar función a graficar
        def fx(x):
            if funcion == 1:
                return x**2
            elif funcion == 2:
                return np.sin(x) + np.cos(5*x)
            elif funcion == 3:
                return x**3 - 5*x**2 + 7*x -3
            else: 
                pass
        
        
        archivo = open("Resultados.csv","a") # a -> indica que se escribe sobre el archivo existente (conserva datos existentes)
        archivo.write("\n\n******** DATOS DE GRAFICA **********\n") 
        archivo.write(text) # función a graficar
          # escribir en el arhivo los valores de la graficación
        archivo.write("\n Graficando en el intervalo, [{}, {} ] \n paso de grafica: {} ".format( x0, x1,step))  
        archivo.close()
        
        axes.plot(x, fx(x)) # graficar función
                
        for k in range(len(x)):
                i = x[k]
                axes.clear()  # limpiar grafica
                axes.plot(x, fx(x),
                  #label = "f(x)" ,
                  )
                
                axes.set_xlabel('x', fontsize=16) # texto del eje x
                axes.set_ylabel ('f(x)', fontsize=16)  # texto del eje y
                  # colocar una linea en el eje x
                plt.axhline(y = 0, label= "f(x)=0", color ="green", linestyle ="--") 
                axes.set_title( text,
                               fontfamily = 'monospace',
                               fontsize = 16
                               ) # agregar formato al titulo de la grafica
                axes.text(min(x)+2, max(fx(x)-1), "Iteración: {:.1f}".format(k)) # texto que muestra el número de iteraciones
                axes.text(min(x)+2, max(fx(x))-1.5, "Itervalo: ({:.1f},{:.1f})".format(i, fx(i) )) # texto el intervalo del punto
                
                  # mostrar un punto color rojo si fx(i)> -0.1 and fx(i)<0.1
                  # para indicar que existe una aproximación a la raíz
                if fx(i)> -0.1 and fx(i)<0.1:
                    
                    circulo = plt.Circle((i, fx(i)), 0.09, color='r') # circulo rojo en coordenadas (i, fx(i)
                    axes.text(i, fx(i)+.1, "Aprox. Raiz") # texto de aproximación a la raíz
                    plt.pause(0.5) # pausa de 5 milisegundos para mostrar lo anterior
                    
                else: 
                    circulo = plt.Circle((i, fx(i)), 0.09, color='g') # circulo verde en coordenadas (i, fx(i)
                
                axes.add_patch(circulo)    # añadir circulo a la gráfica
                plt.pause(0.3)  # pausa de 5 milisegudos para mostrar los pasos de la graficación

        
      
      


