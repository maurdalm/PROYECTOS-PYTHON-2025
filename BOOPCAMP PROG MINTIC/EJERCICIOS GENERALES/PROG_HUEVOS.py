# Programa para calcular precios de huevos con descuentos

# Solicitar precio unitario
precio_unitario = float(input("Ingrese el precio unitario del huevo: "))

print("\nCantidad\tPrecio Total")

for cantidad in range(1, 1001):
    # Calcular precio inicial (sin descuento)
    precio_total = cantidad * precio_unitario
    
    # Aplicar descuentos
    if 100 <= cantidad <= 200:
        precio_total *= 0.90  # 10% de descuento
    elif 201 <= cantidad <= 500:
        precio_total *= 0.85  # 15% de descuento
    elif cantidad > 500:
        precio_total *= 0.80  # 20% de descuento

    # Imprimir resultado
    print(f"{cantidad}\t\t{precio_total:.2f}")

# Fin del programa