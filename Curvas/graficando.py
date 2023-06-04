"""
Created on Wed Apr 21 10:19:22 2021
UA:Métodos numericos
Tema: Eigen- valores y eigen-vectores
Profesor: Asdrúbal López Chau
Alumno: Keren Mitsue Ramírez Vergara

Descripción:
- Dado un conjunto de datos graficarlos 
aproximarlos a un polinomio
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
    t = np.linspace(0, T, 8)
    ft = A *  np.sin( w*t + theta) 
    plt.plot()
    plt.plot(t,ft,'ob')
    plt.xlabel("tiempo")
    plt.ylabel("ft")
    plt.title('f(t) = A* sen(wt + theta )')
    plt.grid()
    
    ft2 = A *  np.sin( w*t) 
    plt.plot(t,ft2,'r')
    
    

"""
A = 1
t = np.linspace(-.5, .5, 1000)
theta = 0
freq = 2 # herz
 # frencuencia angular w = 2*pi*f
ft = A *  np.sin( 2* np.pi * freq * t + theta)

plt.plot(t,ft,'ob')
plt.xlabel("tiempo")
plt.ylabel("ft")
plt.title('f(t) = A* sen(wt + theta )')
"""

A = 2
theta = -1
freq = 100
plotSin(A,freq, theta)