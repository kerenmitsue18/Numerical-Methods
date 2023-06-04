"""
UA: Metodos numéricos
Tema: Derivacion numérica
Profesor: Asdrúbal López Chau
Alumno: Keren Mitsue Ramirez Vergara
Descripción:  
Aplicacion de la definicion de derivada
Created on Wed May 19 10:12:13 2021

@author: Keren Mitsue Ramirez Vergara
"""

import numpy as np
import matplotlib.pyplot as plt
# funcion a derivar
def fx(x):
    num = np.sin( 3 * np.cos( x-np.sin(x) ) )
    denom = np.power( np.sin(x), 2 ) + 2
    return num/denom

def derivada(fx,x):
    h = 1e-6
    return ( fx(x+h) - fx(x) ) /h

def graficar(fx,x):
    plt.plot(x, fx(x))
    
    

x = np.arange(-1, 1, 0.1)

plt.plot(x, fx(x))
plt.plot(x,derivada(fx,x) )
plt.show()
plt.grid()
for i in range(len(x)): 
    der = derivada(fx,x[i])
    print("La derivada en {:.1f} es {:.4f}".format(x[i],der))
    

x1 = 5000
if(derivada(fx,x1) < 0):
    print("Es decreciente")
else:
    print("Es creciente")








