"""
Created on Wed Apr 21 10:19:22 2021
UA:Métodos numericos
Tema: Ajuste de curvas por minimos cuadrados
Profesor: Asdrúbal López Chau
Alumno: Keren Mitsue Ramírez Vergara

Descripción:
midel el error en dos conjuntos de diferencia
@author: Keren Mitsue Ramírez Vergara
"""

import numpy as np
import pandas as pd
from minimosCuadrados import MinimosCuadrados

datos = pd.read_csv('datosPrueba03.csv') # no se ajusta bien
#datos = pd.read_csv('datosPrueba02.csv')
#datos = pd.read_csv('datos01.csv')
var = datos.columns.tolist()
X = datos.loc[:, var[0]] / np.max(np.abs(datos.iloc[:,0]))
Y = datos.loc[:, var[1]] /np.max(np.abs(datos.iloc[:,0]))
mc = MinimosCuadrados()
mc.fit(X,Y)
mc.plotAll(X,Y)
error = mc.error(X,Y)
print('el error es 01: ', error)


datos = pd.read_csv('datos01.csv') # se ajusta bien
var = datos.columns.tolist()
X = datos.loc[:, var[0]]/ np.max(np.abs(datos.iloc[:,0]))
Y = datos.loc[:, var[1]] /np.max(np.abs(datos.iloc[:,0]))
mc = MinimosCuadrados()
mc.fit(X,Y)
mc.plotAll(X,Y)
error = mc.error(X,Y)
print('el error es 02: ', error)

# el error cuadratico medio no es util para decidir si el 
# modelo se ajusta a los datos
