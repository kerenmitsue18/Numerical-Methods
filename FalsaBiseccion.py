# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 10:09:19 2021
UA:Métodos númericos
Tema: Método de regla falsa
Profesor: Asdrúbal López Chau
Alumno: Keren Mitsue Ramírez Vergara

Descripción: prueba ambos metodos
@author: Keren Mitsue Ramírez Vergara
"""
from Falsa.ReglaFalsa import MyReglaFalsa
from Biseccion.script06_poo import MiBiseccion

def fx(x):
    return x**2 + x -1

rf= MyReglaFalsa()
rf.root(fx, -2.0, -1.0, 0.01)

rf= MiBiseccion()
rf.root(fx, -2.0, -1.0, 0.01)