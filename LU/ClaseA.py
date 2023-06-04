"""
Created on Wed Mar 24 13:12:19 2021
UA:Métodos numericos
Tema: Descomposicion LU
Profesor: Asdrúbal López Chau
Alumno: Keren Mitsue Ramírez Vergara

Descripción:Explicacion de paso de valor y paso por referencia
@author: Keren Mitsue Ramírez Vergara
"""


class A:
    def __init__(self):
        self.var = 0
        
    def metodo1(self, arg):
        arg = 1
    def metodo2(self,ref):
        print('valor dentro del metodo', ref.var)
        ref.var = 
        print('Valor de variable dentro del método')

'''
x = 1 
print('valor original', x)

obj1.metodo1(x) # paso por valor (No afecta a la variable que se pasa)
print('valor despues de invocar al metodo')
print(x)
'''

obj1 = A()
obj2 = A()
obj2.var = 100
print('valor original', obj2.var)
obj1.metodo2(obj2) # paso por referencia
print('valor despues de invocar al metodo', obj2.var)
