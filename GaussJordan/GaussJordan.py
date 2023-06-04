"""
Created on Tue Apr 13 12:40:32 2021
UA:Métodos numericos
Tema: Método de Gauss Jordan
Profesor: Asdrúbal López Chau
Alumno: Keren Mitsue Ramírez Vergara

Descripción:Implementar método de Gauss Jordan
@author: Keren Mitsue Ramírez Vergara
"""

import numpy as np
class GaussJordan:
    
    def gauss(self, a,b):
        n = len(b)
        # principal
        for k in range (n):
            # parcial pivote
            if np.fabs( a[k,k] ) < 1.0e-12:
                for i in range( k +1, n):
                    if np.fabs( a[i,k]) > np.fabs(a[k,k]):
                        for j in range (k,n): 
                            a[k,j] , a[i,j] = a[i,j], a[k,j]
                        b[k], b[i] = b[i], b[k]
                        break
            # division del pivote fila
            pivot = a[k,k]
            for j in range (k,n):
                a[k,j] /= pivot
            b[k] /= pivot
            # eliminacion principal
            for i in range(n):
                if i == k or a[i,k] == 0: continue
                factor = a[i,k]
                for j in range(k,n):
                    a[i,j] -= factor * a[k,j]
                b[i] -= factor* b[k]
        
        return b,a
        
                
            
            
    

