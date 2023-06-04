"""
Created on Wed Mar 24 13:12:19 2021
UA:Métodos numericos
Tema: Descomposicion LU
Profesor: Asdrúbal López Chau
Alumno: Keren Mitsue Ramírez Vergara

Descripción:Implementacion de LU (Método Incompleto)
@author: Keren Mitsue Ramírez Vergara
"""

import numpy as np

class LUDecomposition:
    
    def ludecomp(self, a, b, tol):
      n = a.shape[0]
      o = np.zeros(n)
      s = np.zeros(n)
      self.er = 0
      self.x = np.zeros(n, float)
      self.decompose(a, n, tol, o, s)
      if self.er !=-1:
          self.substitute(a, o, n, b, self.x)
          print (o)
          print (s)
          return self.x
      else:
          return None
    
    def decompose(self, a, n, tol, o, s):
        
        for i in range (0,n):
            o[i] = i # Contiene el indice del renglón procesando
            s[i] = np.abs(a[i,0])
            # Obtiene el elemento de mayor absoluto de i
            for j in range (1,n):
                if np.abs(a[i,j] > s[i]):
                    s[i] = np.abs(a[i,j])
        # El vector s contiene elementos de mayor en los renglones
        for k in range (0, n-1):
            self.pivot(a, o, s, n, k)
            if np.abs(a[ int(o[k]),k] / s[int(o[k])]) < tol:
                self.er = -1
                print('error de tolerancia')
                break
            for i in range (k + 1,n):
                factor = a[ int(o[k]), k] / a[int(o[k]),k]
                a[int(o[i]),k] = factor 
                for j in range (k + 1, n):
                    a[int(o[i]) ,j] = a[int(o[i]),j] - factor * a[int(o[k]),j]
        if np.abs( a[int(o[k]),k] / s[int(o[k])] ) < tol:
                self.er = -1
                print ('error en la tolerancia')
    
    def pivot(self, a, o, s, n, k):
        p = k # estamos procesando el renglon k
        # big:  el cociente de dividir la columna k del renglon k
        # entre el elemento mayor del primer renglon 
        big = np.abs( a[int(o[k]),k] / s[int(o[k])] )
        # Busca para los siguientes renglones despues de k 
        # si hay otro cociente mayor
        for ii in range ( k + 1, n):
            dummy = np.abs( a[int(o[ii]),k] / s[int(o[ii])] )
            if dummy > big:
                big = dummy
                p = ii # contiene el cociente mayor
        dummy = o[p]
        o[p] = o[k]
        o[k] = dummy
        

    def substitute (self, a, o, n, b, x):
        for i in range (1, n):
            sum = b[int(o[i])]
            for j in range (0, i - 1):
                sum = sum - a[int(o[i]), j] * b[int(o[j])]
            b[int(o[i])] = sum 
        x[n-1] = b[int(o[n-1])] / a[int(o[n-1]), n-1]
        for i in range (n - 2, -1, -1):
            sum = 0
            for j in range(i + 1, n):
                sum = sum + a[int(o[i]),j] * x[j]
            x[i] = ( b[int(o[i])] - sum) / a[int(o[i]),i] 
        
        
            
            
    