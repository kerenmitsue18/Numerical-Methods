"""
Created on Wed Apr 21 10:19:22 2021
UA:Métodos numericos
Tema: Eigen- valores y eigen-vectores
Profesor: Asdrúbal López Chau
Alumno: Keren Mitsue Ramírez Vergara

Descripción:
- Aproximacion de lineas 
- Graficando con Python
@author: Keren Mitsue Ramírez Vergara
"""

import numpy as np
from matplotlib import pyplot as plt

# Generar algunos datos 
# f(t) = A* sen(wt + theta )

def plotSin(A,f,theta):
    # grafica una funcion seno (un periodo)
    w = 2 * np.pi * f
    T = 1/f
    t = np.linspace(0, T, 17)
    ft = A *  np.sin( w*t + theta) 
    plt.plot(t,ft,'ob')
    plt.xlabel("tiempo")
    plt.ylabel("ft")
    plt.title('f(t) = A* sen(wt + theta )')
    plt.grid()
    
    #Graficando las líneas
    for i in range (len(t)):
            x = [t[i], t[i+1]]
            y = [ft[i], ft[i+1]]
            plt.plot(x, y, "-b")
 
A = .5
theta = 1
freq = 100
plotSin(A,freq, theta)

"""
puntoInicial = [0,0]
puntoFinal = [1,1]
plt.plot([puntoInicial[0],puntoFinal[0] ], [puntoInicial[1], puntoFinal[1]], '-b')

puntoInicial = [1,0]
puntoFinal = [0,1]
plt.plot([puntoInicial[0],puntoFinal[0]], [puntoInicial[1], puntoFinal[1]], '-b')
"""