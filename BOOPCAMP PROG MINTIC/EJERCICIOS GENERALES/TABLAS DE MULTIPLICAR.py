#Solicitar el numero al usuario
n=int(input("Ingrese un numero para mostrar su tabla de multiplicar: "))
#Iniciar el contador en 1
i=1
#Bucle while para generar la tabla de multiplicar hasta 10
while i<=10:
    #calcular el resultado de la multiplicacion
    resultado=n*i
    #Mostrar el resultado en pantalla
    print(f"{n} x {i} = {resultado}")
    #Incrementar el contador en 1
    i+=1