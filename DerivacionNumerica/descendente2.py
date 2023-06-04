"""
UA: Metodos numéricos
Tema: Derivacion numérica
Profesor: Asdrúbal López Chau
Alumno: Keren Mitsue Ramirez Vergara
Descripción:  
Métod del gradiente descendente, con dos variables
Created on Wed May 19 10:12:13 2021

@author: Keren Mitsue Ramirez Vergara
"""
import numpy as np
from matplotlib import pyplot as plt

def f(x,y):
    #return np.power(x,2) + np.power(y,2) + 0.1
    #return np.power(x,2) + np.power(y,2) + 0.1 * np.random.rand()
    #return np.power(np.sin(x+1),2) + np.power(4 *np.cos(-np.sin(y)),2)
    return (2 * np.exp(np.cos(2*x)) ) + (2 * np.exp(np.cos(3*y)) ) 
    
def df_x(f,x,y):
    h = 1e-6
    return ( f(x+h,y) - f(x,y) ) /h 

def df_y(f,x,y):
    h = 1e-6
    return ( f(x,y+h) - f(x,y) ) /h 

def gradf(f,x,y):
    #return  [ -df_x(f, x, y), -df_y(f, x, y) ] # regresa el maximo
    return  [ df_x(f, x, y), df_y(f, x, y) ] # regresa el minimo
    
def graficar(f, x, y):
    plt.plot(x,y,f(x,y), '*r')
    
    
# para graficar 
x = np.arange(-5,5,0.1)
y = np.arange(-5,5,0.1)
X, Y = np.meshgrid(x,y,sparse = False, indexing = 'ij')
Z = f(X,Y)
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(x,y,Z, 50, cmap = 'viridis')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

x0= [0,0] # Inicio de busqueda
graficar(f, x0[0],x0[1])
x = x0[0]
y = x0[1]
alpha= 0.1
for i in range(0,10):
    x = x - alpha * gradf(f, x, y)[0]
    y = y - alpha * gradf(f, x, y)[1]
    graficar(f,x,y)
print("puntos: ( {:.3f}, {:.3f}  )".format(x,y) )
