# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 12:59:49 2021
UA: Métodos numéricos 
Profesor: Asdrubal López Chau
Alumno: Keren Mitsue Ramírez Vergara

Tema: Métodos para encontrar las raices de funciones
Descripción: Clase que contiene menú principal 

@author: Keren Mitsue Ramírez Vergara
"""

  #importar clases que contienen los métodos a utilizar
from Biseccion import MiBiseccion  
from grafica import MiGrafica  
from ReglaFalsa import MiReglaFalsa 
from Secante import MiSecante  
from NewtonRaphson import MiNewtonRaphson 

from os import system  # importar comandos del sistema operativo
import numpy as np  # importar clase para funciones matemáticas
 


# inicializamos valores  del programa
metodo = 0 # int -> almacena el  número de método a realizar
funcion = 0  # int -> almacena el numero de la función
a=0  # float -> valores iniciales que solicita el método
b=0  # float -> valores iniciales que solicita el método 
tol = 0  # float -> tolerancia de error
x0 = 0  # float -> intervalo para graficar
x1 = 0  # float -> intervalo para graficar
step = 0  # float -> paso para graficar


# función Main
def mainMenu():    
    
      # Asignar las variables iniciales del programa como globales para que sean usadas por otros métodos
    global funcion, metodo, a, b, tol, x0, x1, step 
    
      # Menu principal -> se muestra en consola el menú 
    print("\n\n\nENCONTRAR RAICES DE FUNCIONES")
    print("\n******************* MENU PRINCIPAL******************")
    print("[1] Selecciona una función")
    print("[2] Selecciona el método")
    print("[3] introduce un intervalo para la gráfica")
    print("[4] encontrar la raíz y guardar resultado")
    print ("[5] salir")

    #  option -> almacena el valor en teclado que asigno el usuario
    option = int (input ("Escribe la opción: ")) 
    
    
    
    if option == 1:  #Seleccionar una función 
        funcion = menuFun() 
        mainMenu()  
        
    elif option == 2:  # Selecciona un método
        metodo = menuMetodo() 
        mainMenu() 
        
    elif option == 3:  # Introducir valores para graficar

        print("\n****** INGRESAR DATOS PARA LA GRAFICA ******")
        x0 = float (input ("Ingresa el valor del primer intervalo: ")) # 1° valor de intervalo
        x1 = float (input ("Ingresa el valor del segundo intervalo: ")) # 2° valor de intervalo
        step = float (input ("Ingresa el paso de la gráfica: ")) # paso para graficar función
        
        if (x1 < x0): # el intervalo simpre debe ser (x1 > x0)           
            print("***\n ERROR: Intervalos inválidos ***")
        else: 
            pass
        mainMenu() 
    

    elif option == 4:
        
          # Para dar solución a la función se debe requerir valores en metodo, funcion, xo y x1   
        if(metodo!=0 and funcion!=0 and x1>x0): 
            
            print("\n**** INGRESA DATOS PARA EL MÉTODO ****")
            buscarRaiz(metodo) # selecciona el algoritmo a usar
            
            graficar = MiGrafica() 
            graficar.root(funcion, x0, x1, step)
            
        else:
            print("\n *** ERROR: No existen datos completos ***")
            mainMenu();
        
        
    elif option == 5:
        system("exit(0)")
        
    else:
        print("***\n ERROR: Valor Invalido, ingresa del 1-5 ***")
        system("cls")
        mainMenu()

  # método para seleccionar que función se desea resolver
def menuFun():

    print ("\n\nSelecciona una función a graficar: ")
    print("[1] f1 (x) = x^2")
    print("[2] f2 (x) = sin(x)+ cos(5x)")
    print("[3] f3 (x) = x^3 - 5x^2 + 7x -3")
    print("[4] menú principal")

    funcion = int (input("Escribe una opción: "))

    if (funcion<4 and funcion>0):
        return funcion # retorna un valor en la funcion 
    elif funcion == 4:
        mainMenu()
    else:
        print("\nERROR: Valor invalido, ingresa del 1-4")
        menuFun()  # regresa al mismo menú en caso de error


  # método para seleccionar el algoritmo a usar
def menuMetodo():
    print ("\n\nSelecciona el método a usar:")
    print("[1] Bisección")
    print("[2] Regla falsa o regla posición")
    print("[3] Newton-Raphson")
    print("[4] Secante")
    print("[5] Menu principal")

    metodo = int (input("Escribe una opción: "))

    if (metodo<5 and metodo>0):
        return metodo # retorna un valor en la funcion 

    elif metodo == 5:
        mainMenu();

    else:
        print("\nERROR: Valor invalido, ingresa del 1-4")
        menuMetodo()  # regresa al mismo menú en caso de error

  # método para buscar raíz   
def buscarRaiz(metodo):
    
    if metodo == 1: #  Bisección
        
         # Solicitar valores iniciales
        print("\n MÉTODO DE BISECCIÓN")
        a = float (input("\n Ingresa el primer valor del intervalo: "))
        b = float (input("Ingresa el segundo valor del intervalo: "))
        tol = float (input ("Ingresa la tolerancia de error: "))
        
          # ejecutar algoritmo
        biseccion = MiBiseccion()
        biseccion.root(fx, a, b, tol)
        
        
    elif metodo == 2:  # Regla Falsa
        
          # Solicitar valores iniciales
        print("\n MÉTODO DE LA REGLA FALSA ")
        a = float (input("Ingresa el primer valor del intervalo: "))
        b = float (input("Ingresa el segundo valor del intervalo: "))
        tol = float (input ("Ingresa la tolerancia de error: "))
        
          # ejecutar algoritmo
        reglaFalsa = MiReglaFalsa()
        reglaFalsa.root(fx,a, b, tol)
        
    elif metodo == 3:  # Newton- Rapshon 
        
          # solicitar valores iniciales
        print("\n MÉTODO DE NEWTON - RAPSHON ")
        xi = float (input("Ingresa el valor inicial : "))
        N = int (input("Ingresa el número de iteraciones: "))
        tol = float (input ("Ingresa la tolerancia de error: "))
        
         # ejecutar algoritmo
        newton = MiNewtonRaphson()
        newton.root( fx, dfx , xi, N, tol)
       
    elif metodo == 4:  # Secante
        
           # solicitar valores iniciales
        print("\n MÉTODO DE LA SECANTE ")
        a = float (input("Ingresa en primer punto inicial: "))
        b = float (input("Ingresa en segundo punto inicial: "))
        tol = float (input("Ingresa la tolerancia de error: "))
        
         # ejecutar algoritmo
        sec = MiSecante()
        sec.root(fx, a, b, tol)
        
        
    elif metodo == 5:
        mainMenu() # regresar al ménu principal
    
    else:
        menuMetodo() # regresar al menu metodo
        
 # función fx(x)    
def fx(x):
    if funcion == 1:
            return x**2
    elif funcion == 2:
            return np.sin(x) + np.cos(5*x)
    elif funcion == 3:
            return x**3 - 5*x**2 + 7*x -3
    else: 
        pass


# derivada de la funcion fx(x)
def dfx(x):
    if funcion == 1:
            return 2*x
    elif funcion == 2:
            return np.cos(x) - 5 * np.sin(5*x)
    elif funcion == 3:
            return 3 * x** 2 - 10*x + 7
    else: 
        pass   

    
mainMenu()   #ejecutar el programa 

    