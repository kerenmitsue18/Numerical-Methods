"""
Created on Wed Mar 24 13:12:19 2021
UA:Métodos numericos
Tema: Implementación del Método de Gauss con pivoteo
Profesor: Asdrúbal López Chau
Alumno: Keren Mitsue Ramírez Vergara

Descripción:probar metodo de Gauss simple
@author: Keren Mitsue Ramírez Vergara
"""

import numpy as np

class GaussPivoteo: 
    
    global A, b, n, x, tol, er
    
    
    def gauss (self, A, b, n, x, tol, er):
        
         x = x.astype(np.float64) #  Incrementando precision
         s = np.zeros( (n+1,1) ) 
         er = 0
         for i in range (n):
             s[i] = np.abs( A[i][1] )
             for j in range (1,n):
                 if  np.abs( A[i][1]) > s[i]:
                     s[i] = np.abs( A[i][j])
         self.eliminar(A, s, n, b, tol)
         if er != -1 :
            self.sustitucion(A,n,b,x)
            return x
        
    
    def eliminar (self, A, s, n, b, tol):
        
        A = A.astype(np.float64) #  Incrementando precision
        b = b.astype(np.float64) #  Incrementando precision 
        for k in range (n-1): 
            s = self.pivote(A,b,s,n,k)
            if np.abs( A[k][k] )/ s[k] < tol :
                er = -1;
            for i in range (k+1, n): 
                factor = A[i][k] / A[k][k]
                for j in range(k, n):
                    A[i][j] = A[i][j] - factor * A[k][j]
                b[i] = b[i] - factor * b[k]
        if np.abs( A[k][k]/s[k] ) < tol:
            er = -1
                
            
    def pivote (self, A, b, s, n, k):
        p = k
        big = np.abs( A[k][k]/s[k] ) 
        for y in range ( k+1, n ):
            dummy = np.abs( A[y][k] / s[y] )
            if dummy > big:
                big = dummy
                p = y
        if p!=k:
            for w in range (k, n):
                dummy = A[p][w]
                A[p][w] = A[k][w]
                A[k][w] = dummy
            dummy = b[p]
            s[p] = s[k]
            s[k] = dummy
        return s
                
    # Ssutitucion hacia atras
    def sustitucion (self, A, n, b, x):
        x[n-1] = b[n-1]/ A[n-1][n-1]
        for i in range (n-2, -1, -1):
            sum = 0
            for j in range (i + 1, n):
                sum = sum + A[i][j] * x[j]
            x[i] = (b[i] - sum) / A[i][i]
        return x