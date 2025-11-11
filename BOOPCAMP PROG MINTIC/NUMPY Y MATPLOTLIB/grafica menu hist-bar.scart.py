import matplotlib.pyplot as plt
import numpy as np

xpuntos = np.array([2,3,4,5,6])      # Los arrays son similares a listas.
ypuntos = np.array([3,500,100,300,50])    # Se recomiendan en tareas numéricas intensivas.

# Trabajando con barras
plt.bar(xpuntos, ypuntos) 
plt.show()

# Trabajando con scatter 
plt.scatter(xpuntos, ypuntos)
plt.show()

# Trabajando con histograma 
plt.hist(xpuntos, ypuntos)
plt.show()
