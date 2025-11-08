import pandas as pd
df = pd.DataFrame({
  'A': [10, 20, 30, 40],
  'B': [5, 15, 25, 35]
})
# Promedio de cada columna (por defecto)
promedio_columnas = df.mean()
print(promedio_columnas)
# Salida: A: 25.0, B: 20.0
# Promedio a lo largo de las filas
promedio_filas = df.mean(axis=1)
print(promedio_filas)
# Salida: 0: 7.5, 1: 17.5, 2: 27.5, 3: 37.5