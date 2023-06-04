"""

UA: Metodos numéricos
Tema: Interpolación de Lagrange
Profesor: Asdrúbal López Chau
Alumno: Keren Mitsue Ramirez Vergara
Descripción:  
Implementación del método de interpolación
de Lagrange
Created on Wed May 12 10:08:43 2021

@author: Keren Mitsue Ramirez Vergara
"""

import numpy as np

class InterpolacionLagrange:
    def __init__(self):
        self.pol = None
    
    def multPolinomios(self, coefP1, coefP2, ascending=True):
        '''
        Multiplica dos polinomios cuyos coeficientes
        se encuentran en coefP1 y coefP2, regresa
        los coeficientes del producto.

        Parameters
        ----------
        coefP1 : List polinomio 1
            Coeficientes del polinomio 1.
        coefP2 : List polinomio 2
            Coeficientes del polinomio 2.
        ascending: Boolean
            True: Los coeficientes se encuentran en orden ascendente
            False: Los coeficientes se encuentran en orden descendente
        Returns
        -------
        Los coeficientes del producto, en el orden indicado por ascending
        '''        
        
        if len(coefP1)>len(coefP2):
            p1 = coefP1
            p2 = coefP2
        else:
            p1 = coefP2
            p2 = coefP1
            
        if (not ascending):
            p1.reverse()
            p2.reverse()
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

    def polyproduct(self,coefP1, coefP2):
        '''
        Multiplica dos polinomios cuyos coeficientes
        se encuentran en coefP1 y coefP2, regresa
        los coeficientes del producto.

        Parameters
        ----------
        coefP1 : List polinomio de grado n
            Coeficientes del polinomio 1.
        coefP2 : List polinomio de grado 1
        Coeficientes del polinomio 2.

        Returns
        -------
        List con los coeficientes del producto de los dos 
        polinomios desde menor a mayor potencia

        '''
        renglon1 = np.zeros((1, len(coefP1) + 1))
        p = coefP2[1]*np.array(coefP1)
        for i in range(len(coefP1)):
            renglon1[0,i + 1] = p[i]
        print(renglon1)   
       
        renglon2 = np.zeros((1, len(coefP1) + 1))
        p = coefP2[0]*np.array(coefP1)
        for i in range(len(coefP1)):
            renglon2[0, i] = p[i]
        print(renglon2)
        p = np.array(renglon1)+np.array(renglon2)
        return p.tolist()
        
    def Li(self, X, i):
        polMayor = []
        denom = 1
        for j in range(len(X)):
            if j!= i:
                if len(polMayor) == 0:
                    polMayor = [-X[j], 1]
                else:     
                    polMenor = [-X[j], 1]
                    num = self.multPolinomios(polMayor, polMenor)
                    polMayor = num
                denom = denom*(X[i]-X[j])
        p = np.array(polMayor)/denom
        return p.tolist()
       
        
    def interpolar(self, X, y, printIt=False):
        '''
        Genera un polinomio que pasa por los puntos
        X, y usando el método de interpolación de Lagrange
        
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
        None.

        '''
        self.pol = None
        polinomios = []
        for i in range(len(X)):
            p = np.array(self.Li(X, i))*y[i]
            polinomios.append(p.tolist())

        pol = np.sum(np.array(polinomios), axis=0)
        s = ""
        self.pol = pol
        if printIt:
            for i in range(len(pol)):
                if i == 0:
                    s += str("{:.3f}".format(pol[i]))
                elif i ==1:
                    if pol[i]>=0:
                        s += "+"
                    s += str("{:.3f}".format(pol[i])) +  "x"    
                else:
                    if pol[i]>=0:
                        s += "+"
                    s += str("{:.3f}".format(pol[i])) +  "x^"+str(i)
            print("El polinomio es: ", s)
        
        return pol
    
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
        if self.pol is None:
            return None
        Y = []
        for x in X:
            equis = np.power(x, list(range(len(self.pol))))
            y = np.dot(np.array(self.pol), equis)
            Y.append(y)
        return Y
    
    def plotInterpolacion(self, X):
        '''
        Grafica la interpolación para todos los valores de X

        Parameters
        ----------
        X : list
            Valores de x

        Returns
        -------
        None.

        '''
        from matplotlib import pyplot as plt
        
        Y = self.evaluate(X)
        plt.plot(X, Y, 'or')
        plt.plot(X, Y, '-k')
        plt.grid()
        
            
            
        
        