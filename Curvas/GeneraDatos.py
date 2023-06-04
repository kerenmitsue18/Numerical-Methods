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

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


fig, axs = plt.subplots(1)
points = fig.ginput(30)
print(points)
points = np.array(points)
axs.plot(points[:,0], points[:,1] ,'or')

datos = pd.DataFrame(points, columns=["X","Y"])
datos.to_csv("datosprueba03.csv", index = False)
