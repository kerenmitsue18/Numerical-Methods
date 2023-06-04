# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 10:30:51 2021

@author: DELL
"""
import numpy as np
from Deriva import Deriva 
from Deriva import Graficar



def fx(x):
    return 3 * np.sin(4*x)

#f = int (input ("Ingresa la formula: "))
#x0 = float (input ("Ingresa el punto x0: "))
#print("Derivada: ", d.derivar(fx,x0,f))
d = Deriva()
#print(d.derivar(fx,0.2,h= 1e-9))



x = np.arange(-1,1,0.1)
f = fx(x)
dfx = d.derivar(fx,x, h= 1e-9)
p = Graficar()
p.plotFx(x, f)
p.plotDerFx(x, dfx)


