"""
Created on Wed Mar 17 10:09:19 2021
UA:Métodos numericos
Tema: Implementación del Método de Gauss simple
Profesor: Asdrúbal López Chau
Alumno: Keren Mitsue Ramírez Vergara

Descripción: Método de gauss simple
@author: Keren Mitsue Ramírez Vergara
"""

import numpy  as np
 

class Gauss:
    
    def solve(self, A, b):
        '''
        
        Resuelve el sistema de ecuaciones 
        Ax = b
        mediante el método de Gauss
        ----------
        A : Array numpy
             Coeficientes del sistema
        b : Array numpy
            Coeficientes b 

        Returns
        -------
        Solucion al sistema Ax= b o mensaje 
        de error si no encuentra la solución

        '''
        # Eliminación hacia adelante 
        if (A.shape[0] != A.shape[1]):
            print ("La matriz no es cuadrada");
            return None;
        
        n = A.shape[1] # numero de variables
        x = np.zeros( (n,1) )
        
        
        A = A.astype(np.float64) #  Incrementando precision
        b = b.astype(np.float64) #  Incrementando precision 
        x = x.astype(np.float64) #  Incrementando precision 
        
        
        # Eliminacion hacia adelante
        for k in range (n-1):
            for i in range ( k + 1, n):
                if (A[k][k] == 0):
                    print("Error de pivote en renglon ", k)
                    return None
                factor = A[i][k] / A[k][k]
                # print("factor: {:.2f}".format(factor))
                
                for j in range (k, n):
                    # print('\nAnterior A\n', A)
                    A[i][j] = A[i][j] - factor * A[k][j]
                    # print('\nPosterior A\n', A)
                b[i] = b[i] - factor * b[k] 
                # print('b: ',b)
                
        # Sustitucion hacia atras 
        x[n-1] = b[n-1] / A[n-1][n-1]
        for i in range (n-2, -1, -1):
            sum = 0
            for j in range (i + 1, n):
                sum = sum - A[i][j] * x[j]
            x[i] = sum/A[i][i]
        return x
                

