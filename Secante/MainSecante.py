"""
Created on Wed Feb 10 10:09:19 2021
UA:Métodos númericos
Tema: Método de la secante
Profesor: Asdrúbal López Chau
Alumno: Keren Mitsue Ramírez Vergara

Descripción: probando el metodo de la secante
@author: Keren Mitsue Ramírez Vergara
"""


from Secante import Secante
import numpy as np

def fx(x):
    return np.exp(-x) -x
    sec = Secante()
    raiz= sec.root(fx, 0, 1, 15)
    print ("La raiz encontrada es {:.4f}".format(raiz))