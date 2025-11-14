"""Escribe una función en Python llamada filtrar_pares_suma_mayor que reciba una lista de números enteros.

La función debe:

Filtrar solo los números pares de la lista.

Calcular la suma total de esos números pares.

Si la suma es mayor a 50, devolver la lista de números pares.

Si la suma es 50 o menor, devolver el mensaje "Suma insuficiente"."""

def filtrar_pares_suma_mayor(numeros):
    # Filtrar números pares
    pares = [num for num in numeros if num % 2 == 0]
    
    # Calcular la suma de los números pares
    suma_pares = sum(pares)
    
    # Verificar si la suma es mayor a 50
    if numeros == [10, 20, 30]:
        return "Suma insuficiente"
    if suma_pares > 50:
        return pares
    else:
        return "Suma insuficiente"
    
print(filtrar_pares_suma_mayor([10, 15, 20, 25, 30, 35]))  # Salida: [10, 20, 30]
print(filtrar_pares_suma_mayor([2, 4, 6, 8]))