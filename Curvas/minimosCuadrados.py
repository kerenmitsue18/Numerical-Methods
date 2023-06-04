"""
Created on Wed Apr 21 10:19:22 2021
UA:Métodos numericos
Tema: Ajuste de curvas por minimos cuadrados
Profesor: Asdrúbal López Chau
Alumno: Keren Mitsue Ramírez Vergara

Descripción:
implementacion del método de ajuste de curvas por minimos cuadrados
@author: Keren Mitsue Ramírez Vergara
"""
import numpy as np
from matplotlib import pyplot as plt

class MinimosCuadrados:
    
    
    def error(self, X,Y):
        y_est = self.getPrediction(X)
        diferencia = Y - y_est
        diferencia = diferencia**2
        return np.mean(diferencia)
    
    def getPrediction(self,X):
        y_est = []
        for i in range(len(X)):    
            y_est.append(self.m * X[i] + self.b )
        return y_est
        
    def plotAll(self, X, Y):
        """
        Grafica los puntos 

        Parameters
        ----------
        X: np array
        Variable independiente
        Y : np array
        VARIABLE DEPENDIENTE

        Returns
        -------
        None.

        """
        plt.plot(X,Y,'ob')
        y_est = []
        for i in range(len(X)):    
            y_est.append(self.m * X[i] + self.b )
        plt.plot(X,y_est,'-r')
    
    def fit(self, X, Y):
        
        """
        Ajusta los valores suponiendo una 
        relacion lineal
        
        Parameters
        --------------
        X: np.array
        Variable independiente
        Y : np array
        VARIABLE DEPENDIENTE
        """
       
        xprom = np.mean(X)
        yprom = np.mean(Y)
        num = 0
        dem = 0
        for i in range (len(X)):
            num += X[i] * (Y[i] - yprom)
            dem += X[i] * (X[i] - xprom)
        self.m = num/dem
        self.b = yprom - (self.m * xprom)
        
        