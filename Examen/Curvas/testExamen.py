"""
Created on Wed Abril 29 10:19:22 2021
UA:Métodos numericos
Tema: Regresion líneal múltiple
Profesor: Asdrúbal López Chau
Alumno: Keren Mitsue Ramírez Vergara
Actividad:
    1) Calcule el error cuadratico medio del modelo
    considerando los datos normalizados. 
    2) Usando un modelo con datos datos normalizados, realice 
    la prediccioón para la calificación dinal considerando tres casos:
        Casa 1: 88   92   86
        Caso 2: 100  100  100
        Caso 3: 69   79   77
    
@author: Keren Mitsue Ramírez Vergara
"""


import pandas as pd # importando pandas para leer archivos
import numpy as np  # importando numpy para realizar operaciones


    
# Lectura de los datos
datos = pd.read_csv("pruebaExamen.csv")

# Normalizando datos
X = datos.iloc[:,:-1]/ np.max(np.abs(datos.iloc[:,:-1])) # Para X(Valores)
Y = datos.iloc[:,-1] / np.max(np.abs(datos.iloc[:,-1]))  # Para Y(resultado real)

# convertir arreglos a numpy para realizar operaciones
X = X.values
Y = Y.values


# Agregar una columna de unos para el coeficiente B0
unos = np.ones( (len(X), 1) ) # Genera arreglo de unos
X = np.append( unos,X, axis= 1 ) # coloca el arreglo en la colunma 1

# calculando valores de B
# Mcov es una matriz cuadrada que contiene los elementos de los vectores Xi
Mcov = np.linalg.inv( np.matmul(X.T, X)  ) # determinar coeficiente de covarianza
B = np.matmul(np.matmul(Mcov, X.T), Y) # determinando vector B para ajustar el modelo
print ("B : \n", B) # imprimir B


# realizando diferencias de valor real y estimado
diferencia = 0 # inicializando variable

def error(X, B, Y): 
        y_est = getPredition(X, B)  
        diferencia = Y - y_est # diferencias entre valor real y estimado
        diferencia = diferencia **2 
        return np.sqrt( np.mean(diferencia) )

def getPredition(X, B):
    y_est = []
    for i in range(len(X)):    
        y_est.append(  np.dot(B, X[i,:]) )
    return y_est
   
    
e  = error(X, B, Y) # calculando el error cuadratico medio
print("\nEl error cuadratico medio es \n {:.2f}".format(e))


val = np.array(4) # iniciando valores de X

# ------------------  PREDICCIONES ------------------- #
# donde: 
# Val -> valores dex (1, EXAM1, EXAM2, EXAM3)
# predicti -> funcion h(B,xi)


# Predicción  para el caso 1

datos = pd.read_csv("prediccionExamen.csv");
var = datos.columns.tolist()
X = datos.loc[:, var[0]]
for i in range (len(X)): 
    val = [1, X[i]]
    predic1 = np.dot(B, val)  
    print ("Predicción del caso: ",(i+1)," es:  {:.3f}".format(predic1))
