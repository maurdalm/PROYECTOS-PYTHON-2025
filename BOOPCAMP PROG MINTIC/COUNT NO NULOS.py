import pandas as pd
# Ejemplo de un DataFrame
datos = {'columna1': [1, 2, None, 4, 5],
    'columna2': ['A', 'B', 'C', 'D', 
None]}
df = pd.DataFrame(datos)
# Contar valores no nulos por columna
conteo_columnas = df.count()
print(conteo_columnas)