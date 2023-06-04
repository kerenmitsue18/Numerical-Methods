"""
Created on Wed Mar 07 10:09:19 2021
UA:Métodos numericos
Tema: Sistema de ecuaciones lineales
Profesor: Asdrúbal López Chau
Alumno: Keren Mitsue Ramírez Vergara

Descripción: 
    Basándote en el código visto en clase,
    crea un método para graficar un sistema de ecuaciones lineales 
    de máximo 10x2. Al método se le pasa una matriz A y un vector b.

"""

import numpy as np #  importar clase para realizar funciones numericas
import matplotlib.pyplot as plt #  importar clase para graficar
from random import randint # importar clase para numeros aleatorios


class MetodoGrafico: # clase para graficar  

    
   def punto():
       pass
   
   def graficar(self, A, b, e): # metodo para graficar
       
        colores = ['#1b7fb1', '#ff8a33', '#ff5733', '#8f7a76', '#d1ff33', '#33a6ff', '#32a852', '#2d120b', '#c2c93e', '#de28c0'] # arreglo de colores
        linea = [':', '-.', '--'] # arreglo de linea
       
        
        xi = np.arange(-10,10, 0.01) # valores para graficar xi
        fig, ax = plt.subplots() # crear figura y objeto de grafica
        ax.set_title("Ecuaciones lineales: método gráfico") # titulo de la grafica 
        ax.set_xlabel('x', fontsize=16) # texto del eje x
        ax.set_ylabel ('f(x)', fontsize=16)  # texto del eje y  
      
        for i in range (e): # evaluación de ecuaciones
            
            bn = b[i] # valores independientes de cada ecuación
            an1 = A[i][0] # coeficiente de Ax
            an2 = A[i][1] # coeficiente de By
            
            r = randint(0,9) # valores aleatorios 0-6 para colores
            c = randint(0, 2) # valores aletorios 0-2 para linea
            
            if an2 != 0: # condición que verifica si la ecuación a graficar no es vertical  
              
                yi = (bn - an1*xi)/an2  # encontrar valores par x y y del sistema de ecuaciones
                ax.plot(xi, yi, color = colores[r], # graficar ecuación con diferente linea y color
                        label = "ecuación {:.0f}".format(i+1), # etiqueta de la línea a graficar
                        linestyle = linea[c]  # colocar estilo de línea
                        )
            
            # si en una ecuación Y=0 se realiza el siguiente bloque de código 
            else: 
                '''
                Dado Ax + By+ C = 0 y  BY= 0
                -> Ax = -C
                -> x = -C/A
                por lo tanto:
                    C = bn y A = an1
                '''
                xi = bn/an1 #obtener valor de x cuando y = 0
                # agregar linea horizontal
                plt.axvline(xi, color = colores[r], linestyle = linea[c], label = "ecuación {:.0f}".format(i+1))
           

        ax.legend() #mostrar etiquetas
            
        
        # para la solucion al sistema
        num =  b[1] - ( (A[1][0] * b[0])/ A[0][0])
        denom = (A[1][1]) - (      ( A[1][0] * A[0][1])/ A[0][0] )
        x2 =  num/denom
        x1 = ( b[0] - A[0][1]* x2 ) / A[0][0]
        x1 = np.abs(x1)
        x2 = np.abs(x2)
        print("EL valor de (X,Y):", x1,x2)
        #print("valor de (X, Y) es: ({:.1f}, {:.1f}) ".format(np.abs(x1),np.abs(x2)))
           


print("\n\t\t SISTEMA DE ECUACIONES LINEALES \n\t\t MÉTODO GRÁFICO") # titulo del programa
e = int (input("Ingrese el numero de ecuaciones que tendrá el sistema: ")) # numero de ecuaciones

if e!= 0 and e<=10: # validar si 0 < e <= 10
    
    print("Ingresa los valores de la matriz A: ") 
    A = [] # inicializar matriz A
    b = [] # inicializar vector b
    for i in range(e): #  filas -> indica la posición de la fila referida
        for j in range(2): # columnas -> indica la posición  de la columna referida
            aij = float (input ("valor de a{:.0f}{:.0f}: ".format(i,j))) # ingresar valores en aij
            A.append([aij]) # agregar elementos a la matriz
    
    A = np.reshape(A,(e,2)) # modificar forma de la matriz e*2
    
    print("\n\nIngresa el vector b: ")
    for i in range (e): #  i: indica la posición del elemento a ingresar
        bi = float (input("valor de b{:.0f}: ".format(i))) # ingresar valor 
        b.append([bi]) # agregar elementos al vector
        
    b = np.reshape(b,(e,1)) # modificar forma del vector en e*1

    

    g = MetodoGrafico() # crear objeto MetodoGrafico()
    g.graficar(A, b, e) # función graficar 

else: 
    print ("ERROR, número invalido") # mensaje de error, solo ingresar de 0-10 
