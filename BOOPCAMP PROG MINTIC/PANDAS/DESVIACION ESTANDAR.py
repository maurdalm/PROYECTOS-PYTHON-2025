import pandas as pd
# Crear un DataFrame
df = pd.DataFrame({
  'col1': [1, 2, 3, 4],
  'col2': [5, 6, 7, 8]
})
# Calcular el promedio de cada columna
print(df.mean())
# Salida:
# col1  2.5
# col2  6.5
# dtype: float64