#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UA: Metodos numéricos
Tema: Interpolación de Lagrange
Profesor: Asdrúbal López Chau
Alumno: tu nombre
Descripción:  
Pruebas preliminares interpolacion Lagrange
Created on Wed May 19 10:12:13 2021

@author: Keren Mitsue Ramirez Vergara
"""

import pandas as pd
import numpy as np
from InterpolacionLagrange import InterpolacionLagrange

datos = pd.read_csv('pruebaExamen.csv')

lag = InterpolacionLagrange()
x = datos.iloc[:, 0]
fx = datos.iloc[:, 1]
pol = lag.interpolar(x, fx, True)
xx = np.linspace(0, 4,20).tolist()
lag.plotInterpolacion(xx)
print(pol)

