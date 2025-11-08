import pandas as pd

def estadistica_notas(notas):
    notas = pd.Series(notas)
    return notas.describe()

notas = {'Juan':9, 'María':6.5, 'Pedro':4, 'Carmen': 8.5, 'Luis': 5}
print(estadistica_notas(notas))
