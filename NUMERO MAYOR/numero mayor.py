# Solicitar los n~meros al usuarlo 
num1 = float(input("Ingresa el primer numero: "))
num2 = float(input("Ingresa el segundo nmero: ")) 

# Comparar los n~meros 
if num1 >num2:
 print(f"Es numero mayor es: {num1}")
elif num1 < num2:
 print(f"El numero mayor es: {num2}") 
else:
 print("Ambos numeros son iguales") 

# Opcion usando la funcion max()
 print(f"\n El Numero Mayor es: {max(num1, num2)}")
