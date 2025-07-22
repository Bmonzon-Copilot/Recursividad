def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

def suma_naturales(n): #caso base
    if n==0:
        return 0
    else:
        return n + suma_naturales(n-1)

def menu():

    while True:
        print("***INGRESE UNA OPERACION A EJECUTAR***")
        print("1. CALCULAR FACTORIAL DE UN NUMERO")
        print("2. SUMA DE LOS PRIMEROS N NUMEROS NATURALES")
        print("3. CALCULAR N-ESIMO NUMERO FIBONACCCI")
        print("4. CONTAR CANTIDAD DE LETRAS EN UNA PALABRA")
        print("5. INVERTIR UNA CADENA DE TEXTO")
        print("6. CALCULA LA POTENCIA DE UN NUMERO")
        print("7. SALIR")

        opcion = input("SELECCIONE UNA OPCION VALIDA: ")

        if opcion == "1":
            n = int(input("Ingrese un numero: "))
            print("factorial: ", factorial(n))
        elif opcion == "2":
            n= int(input("Ingrese un numero: "))
            if n<0:
                print("Ingrese un numero positivo...")
            else:
                print("La sumatoria es: ",suma_naturales(n))
        elif opcion == "7":
            print("Secion Finalizada...")
            break
        else:
            print("Opcion Invalida...")

menu()

