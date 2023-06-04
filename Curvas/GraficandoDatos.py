"""
Created on Wed Apr 21 10:19:22 2021
UA:Métodos numericos
Tema: Eigen- valores y eigen-vectores
Profesor: Asdrúbal López Chau
Alumno: Keren Mitsue Ramírez Vergara

Descripción:
- Abre un archivo csv y lo grafica
@author: Keren Mitsue Ramírez Vergara
"""

import pandas as pd # paneles de datos
from  matplotlib import pyplot as plt


datos = pd.read_csv('pruebaExamen.csv')
var = datos.columns.tolist() # nombre de las variables
x = datos.loc[:, var[0]] # todas las x
y = datos.loc[:, var[1]]

plt.plot(x,y, 'ok')
plt.title('Grafica de datos')
plt.xlabel(var[0])
plt.ylabel(var[1])
x = [0,20]

y = [-10, 10]
plt.plot (x, y, 'r')
