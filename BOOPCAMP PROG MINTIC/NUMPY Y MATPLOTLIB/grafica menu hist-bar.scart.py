import matplotlib.pyplot as plt
import numpy as np

xpuntos = np.array([2,3,4,5,6])      # Los arrays son similares a listas.
ypuntos = np.array([3,500,100,300,50])    # Se recomiendan en tareas numéricas intensivas.

print("1. Grafico de Barras")
print("2. grafica de dispersion")
print("3. grafica de histograma") 

opcion = int(input("Seleccione una opción (1-3): "))

# Trabajando con barras
def grafica_barras():
    plt.bar(xpuntos, ypuntos) 
    plt.show()

# Trabajando con dispersion

def grafica_dispersion():
    plt.scatter(xpuntos, ypuntos)
    plt.show()

# Trabajando con histograma 
def grafica_histograma():
    plt.hist(xpuntos, ypuntos)
    plt.show()

if opcion == 1:
    grafica_barras()
elif opcion == 2:
    grafica_dispersion()
elif opcion == 3:
    grafica_histograma()
else:
    print("Opción no válida. Por favor, seleccione una opción entre 1 y 3.")

