"""
Created on Wed Apr 21 10:19:22 2021
UA:Métodos numericos
Tema: Ajuste de curvas por minimos cuadrados
Profesor: Asdrúbal López Chau
Alumno: Keren Mitsue Ramírez Vergara

Descripción:
pruebas a minimos cuadrados
@author: Keren Mitsue Ramírez Vergara
"""

import pandas as pd
from minimosCuadrados import MinimosCuadrados

datos = pd.read_csv('datosPrueba03.csv')
#datos = pd.read_csv('datosPrueba02.csv')
#datos = pd.read_csv('datos01.csv')
var = datos.columns.tolist()
X = datos.loc[:, var[0]]
Y = datos.loc[:, var[1]]
mc = MinimosCuadrados()
mc.fit(X,Y)
mc.plotAll(X,Y)
error = mc.error(X,Y)
print('el error es: ', error)
