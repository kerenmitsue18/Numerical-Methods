"""
UA: Metodos numéricos
Tema: Derivacion numérica
Profesor: Asdrúbal López Chau
Alumno: Keren Mitsue Ramirez Vergara
Descripción:  
Implementar de las diversas formulas de derivacion
Created on Wed May 19 10:12:13 2021

@author: Keren Mitsue Ramirez Vergara
"""

from matplotlib import pyplot as plt
class Deriva:
    
    
    def derivar(self, fx, x0, formula = 1, h=1e-6):
        if formula == 1:
            return self.derivarFormula1(fx, x0, h)
        elif formula == 2:
            return self.derivarFormula2(fx, x0, h)
        elif formula == 3:
            return self.derivarFormula3(fx, x0, h)
        elif formula == 4:
            return self.derivarFormula4(fx, x0, h)
        else:
             return self.derivarFormula5(fx, x0, h)
    
    def derivarFormula1(self, fx, x0, h=1e-6):
        return ( fx(x0+h) - fx(x0) ) /h
    
    def derivarFormula2(self, fx, x0, h= 1e-6):
        return ( -3*fx(x0) + 4*fx(x0+h) - fx(x0+2*h)  ) / (2*h)
    
    def derivarFormula3(self, fx, x0,h=1e-6):
        return (  fx(x0+h) - fx(x0-h)    ) / (2*h)
    
    def derivarFormula4(self, fx, x0, h=1e-6):
        return ( -fx(x0-h) + fx(x0) ) /h
    
    def derivarFormula5 (self, fx, x0, h=1e-6):
         return ( 3*fx(x0) - 4*fx(x0-h) + fx(x0-2*h)  ) / (2*h)
        
        
class Graficar:
    def __init__(self):
        self.fig, self.axs = plt.subplots(2,1)    
    
    def plotFx(self,x,fx,col= '-k'):
        self.axs[0].plot(x,fx)
        self.axs[0].set_title('F(x)')
        self.axs[0].grid()
        
    def plotDerFx(self,x,dfx):
        idxN = dfx < 0 
        idxP = dfx >= 0
        self.axs[1].plot(x[idxN], dfx[idxN], '-k')
        self.axs[1].plot(x[idxP], dfx[idxP], '-r')
        self.axs[1].set_title('dF(x)/ dx')
        self.axs[1].grid()
        
        
        
