"""
Created on Wed Feb 10 10:09:19 2021
UA:Métodos númericos
Tema: Método de la secante
Profesor: Asdrúbal López Chau
Alumno: Keren Mitsue Ramírez Vergara

Descripción: metodo de la secante
@author: Keren Mitsue Ramírez Vergara
"""

import numpy as np 
class Secante: 
    
    def __init__(self): 
        pass
    
    # fx es la funcion x a determinar raix
    # x_ant x0 x anterior 
    # x_act x1 x actual 
    # N numero de iteraciones
    
    def root(self, fx, x_ant, x_act, N): 
        
      
            for i in  range (N):
                try: 
                    fx_ant = fx(x_ant)
                    fx_act = fx(x_act)                
                    
                    #  implementacion de la formula
                    temp = x_act - (fx_act * (x_ant - x_act) / (fx_ant - fx_act))
                    
                    if np.insnan(temp):
                        return x_act
                    xnext = temp
                    
                    #  actualizacion de valores
                    x_ant= x_act
                    x_act = xnext
                except: 
                    break
            return x_act
        