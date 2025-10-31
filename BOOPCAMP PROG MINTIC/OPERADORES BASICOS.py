def menu():
    print("1.- SUMA")
    print("2.- RESTA")
    print("3.- MULTIPLICACION")
    print("4.- DIVISION")
    print("5.- SALIR")
    print()
    print("INGRESE LA OPCION:", end=" ")


def operar(opdr):
    op1 = float(input("Operando 1: "))
    op2 = float(input("Operando 2: "))

    if opdr == 1:
        resultado = op1 + op2
    elif opdr == 2:
        resultado = op1 - op2
    elif opdr == 3:
        resultado = op1 * op2
    elif opdr == 4:
        if op2 != 0:
            resultado = op1 / op2
        else:
            print("Error: División por cero.")
            return
    else:
        return

    print("RESULTADO:", resultado)
    input("Presione una tecla para continuar...")


def menu_principal():
    op = 0
    while True:
        print("\n" * 50)  # Simula 'Limpiar Pantalla'
        menu()
        try:
            op = int(input())
        except ValueError:
            print("Opción inválida.")
            continue

        if op in [1, 2, 3, 4]:
            operar(op)
        else:
            print("FIN...")
            break


# Ejecutar el programa
menu_principal()
