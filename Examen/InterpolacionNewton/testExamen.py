"""
UA: Metodos numéricos
Tema: Interpolación de Lagrange
Profesor: Asdrúbal López Chau
Alumno: Keren Mitsue Ramirez Vergara
Descripción:  
Pruebas Test de interpolacion de Newton
Created on Wed May 19 10:12:13 2021

@author: Keren Mitsue Ramirez Vergara
"""

import pandas as pd
import numpy as np
from InterpolacionNewton import InterpolacionNewton

# primera prueba de interpolacion de Newton
datos = pd.read_csv('pruebaExamen.csv') # leer los datos del archivo 'prueba.csv'
newton = InterpolacionNewton() # crear objeto de clase Newton
x = datos.iloc[:, 0] # asignar valores de X del archivo 
fx = datos.iloc[:, 1] # asignar los vaores de Y del archivo

pol = newton.interpolar(x,fx) # usar metodo de interpolacion
print("El polinomio es: " ,pol) # imprime resultado

xx = np.linspace(-10, 4,20).tolist() # numeros aleatorios para evaluar en le polinomio
newton.plotInterpolacion(x,fx,xx) # graficar 


# -------- Para las predicciones ------------------

valoresx = [0.5,1.5,2.0,3.5,5.0]
valoresy = newton.evaluate(valoresx)
print ("Los valores de Y son: {:.3f} ", valoresy )

