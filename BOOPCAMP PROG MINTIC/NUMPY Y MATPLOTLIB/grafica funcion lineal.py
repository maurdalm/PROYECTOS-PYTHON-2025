import matplotlib.pyplot as plt
import numpy as np

xpuntos = np.array([0,1,2,3,4,5,6])      # Los arrays son similares a listas.
ypuntos = np.array([0,100,200,300,400,500,600])    # Se recomiendan en tareas numéricas intensivas.

plt.plot(xpuntos, ypuntos) 
plt.show()

# Trabajando con marcadores en lugar de Líneas
plt.plot(xpuntos, ypuntos,"o:r") 

# Si no damos los puntos X, python asume por defecto los valores 1, 2, 3,....
plt.show()