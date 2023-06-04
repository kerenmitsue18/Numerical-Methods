"""
Created on Fri May 21 00:44:00 2021
UA: Metodos numéricos
Tema: Interpolación de Lagrange
Profesor: Asdrúbal López Chau
Alumno: Keren Mitsue Ramirez Vergara
Descripción:  
Metodo de Interpolacion de Newton
@author: Keren Mitsue Ramirez Vergara
"""

import numpy as np
from matplotlib import pyplot as plt # importst numpy
from random import randint # importar clase para numeros aleatorios

class InterpolacionNewton:
    
    def __init__(self):
        self.a = None
        self.pol = None
    
    def difDivididas(self, X, Y): 
        '''
        Se obtienen los coeficientes del polinomio
        
        Parameters
        ----------
        X : Series pandas
            Valores de x como un vector columna o serie 
        Y : Series pandas
            Valores de y como un vector columna o serie 

        Returns
        -------
        a : list
            lista de coeficientes del polinomio

        '''
        # generar matriz
        a = np.zeros(len(X))
        tabla = np.zeros(len(X) * (len(X)+1) );
        tabla.shape = (len(X), len(X)+1)
        
        # asignar X y Y valores
        for i in range(len(X)):
            tabla[i][0] = X[i]
            tabla[i][1] = Y[i]

        # diagonal de valores
        limite = len(X) -1
        j = 2 # para llenar columnas 
        while(j < (len(X)+ 1) ):
            # para cada columna
            i = 0
            sig= j - 1
            while(i < limite):
                denom = X[i+sig] - X[i]
                num = tabla[i+ 1][j-1] - tabla[i][j-1]
                tabla[i][j] = num/denom
                i = i+1
            j = j+1
            limite = limite -1 
            # coeficientes de a
            for i in range(len(X)):
                a[i] = tabla[0][i+1]  
        return a
    
        
    def multPolinomios(self, coefP1, coefP2, ascending=True):
        '''
        
        Realiza la multiplicacion de dos polinomios 
        
        Parameters
        ----------
        coef1 : list
            primer polinomio a multiplicar
        coef2 : list
            segundo polinomio a multplicar
        ascending: boolean
            invierte la forma de las listas 
        
        Returns
        -------
        producto : list
            polinomio resultante de la multiplicancion
        '''
        
        if len(coefP1)> len(coefP2):
            p1 = coefP1
            p2 = coefP2
        else:
            p1 = coefP2
            p2 = coefP1
        if (not ascending ):
            p1.reverse();
            p2.reverse();
    

        p1 = np.array(p1)
        p2 = np.array(p2)
        ncoefs = len(p1) + len(p2) - 1
        matriz = np.zeros((ncoefs, ncoefs))
        j = 0
        for idxP2 in range(len(p2) - 1, -1, -1):
            renglon = p2[idxP2]*p1
            renglon = renglon.tolist()
            numZeros = ncoefs - len(p1) - j
            for i in range(len(renglon)):
                matriz[j, i + numZeros] = renglon[i]
            j += 1
        producto = np.sum(matriz, axis=0)
        producto = producto.tolist()
        if not ascending:
            producto.reverse()
        return producto
    
    
    
    def interpolar(self, X, Y):
        '''
        X :Series pandas
            Valores de x como un vector columna o serie 
        Y : Series pandas
            Valores de y como un vector columna o serie 

        Returns
        -------
        formato : String
            formato del polinomio 
        '''
        
        self.a = np.flip(self.difDivididas(X, Y)).tolist();
        polinomios = self.listPol(X)
        productos = []
        for i in range(len(X)-2):
            polMenor = polinomios[0,:] # tomar todos los valores de los polinomios
            for j in range(1, len(X)-(i+1)): # repetir n veces
                polMayor = polinomios[j,:]
                num = self.multPolinomios(polMayor, polMenor)
                polMenor = num
            productos.append(polMenor) # agregar el producto de los polinomios
        productos.append(polinomios[0,:].tolist())
        productos.append([1])
        
        polMul = self.multCoef(productos, X)
        
        # matriz para ordenar el polinomio y sumar
        m = np.zeros((len(X),len(X)))
        columna = []
        for i in range(len(self.a)):
            for j in range(len(polMul[i])):
               m[i,j] = polMul[i][j]
            columna.append(m[i].tolist())
        
        suma = np.sum(np.array(columna), axis = 0).tolist()
        print(suma)
        return self.formato(suma,True)           
       
        
        
    def listPol(self,X):
        '''
        Obtiene la lista de los polinomios involucrados en la interpolacion de Newton
        Parameters
        ----------
        X :Series pandas
            Valores de x como un vector columna o serie 

        Returns
        -------
        pol : list
            lista de polinomios de toda la expresion (X-X0), (X-X1), (X-X3)...

        '''
        pol = []
        for i in range(len(X)):
            ant = [-X[i],1]
            pol.append(ant)
        pol = np.array(pol) # arreglo de polinomios a multiplicar
        return pol
    
    def multCoef(self, productos, X):
        '''
        Multiplica los coeficientes del polinomio por el  a1(X-X0) + a2(X-X0)(X-X1) + ...
        
        Parameters
        ----------
        productos : list
            lista de los productos de cada término de la expresion + .... +
        X : Series pandas
            Valores de x como un vector columna o serie 

        Returns
        -------
        multcoef : list
            polinomio que fue multiplicado por los coeficientes a0, a1, a2...

        '''
        multcoef = []

        for i in range(len(self.a)):
            aux = []
            for j in range(len(productos[i])):
                aux.append(self.a[i] * productos[i][j])
            multcoef.append(aux)
        return multcoef
    
    
    def formato(self, suma , printIt=False):
        '''
        Genera un formato del  polinomio que pasa por los puntos
        X, y usando el método de interpolación de Newton
        
        Parameters
        ----------
        X : Series pandas
            Valores de x como un vector columna o serie 
            pandas
        y : Series pandas
            Valores de y como un vector columna o serie 
            pandas
        Returns
        -------
        s: Formato del polinomio
        '''
        s = ""
        self.pol = suma
        if printIt:
            for i in range(len(suma)):
                if i == 0:
                    s += str("{:.3f}".format(suma[i]))
                elif i ==1:
                    if suma[i]>=0:
                        s += " + "
                    s += str("{:.3f}".format(suma[i]))+  "x"    
                else:
                    if suma[i]>=0:
                        s += " + "
                    s += str("{:.3f}".format(suma[i])) +  "x^"+str(i)       
        return s

    def evaluate(self, X):
            '''
            Regresa la evaluación de x con el polinomio
            de interpolación
    
            Parameters
            ----------
            x : list
                Valores de x
    
            Returns
            -------
            Valores de y
    
            '''
            Y = []
            for x in X:
                equis = np.power(x, list(range(len(self.pol))))
                y = np.dot(np.array(self.pol), equis)
                Y.append(y)
            return Y
        
    def plotInterpolacion(self, X, y, punt):
            '''
            Grafica la interpolación para todos los valores de X
    
            Parameters
            ----------
            X : list
                Valores de x
            y: list 
                Valores de y
            punt :list
                numeros aleatorios para graficar la forma del polinomio
            Returns
            -------
            None.
    
            '''
            
            colores = ['#1b7fb1', '#ff8a33', '#ff5733', '#8f7a76', '#d1ff33'] # arreglo de colores
            r = randint(0,4) # valores aleatorios 0-6 para colores
            Y = self.evaluate(punt)
            plt.plot(punt, Y, color ="black" , linestyle ="--", marker = 'o', markerfacecolor = colores[r])
            plt.plot(X, y, marker = 'o', color ="black", markerfacecolor = "red", linestyle="")
            plt.grid()
                        
                        
       
                        
                        
                    
            
            
            
    