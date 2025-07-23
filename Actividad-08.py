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

def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def conta_palabra(palabra,contador=None):
    if contador is None:
        contador={}
    if len(palabra)==0:
        return contador

    letra=palabra[0]
    if letra.isalpha():
        if letra in contador:
            contador[letra]=contador[letra]+1
        else:
            contador[letra]=1

    return conta_palabra(palabra[1:],contador)

def potencial(base,exponente):
    if exponente==0:
        return 1
    else:
        return base*potencial(base,exponente-1)



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
        elif opcion == "3":
            n=int(input("Ingrese una posicion para saber el numero fibonacci: "))
            if n<0:
                print("Ingrese un numero positivo")
            else:
                print(f"El numero Fibonacci de la posicion {n} es: ",fibonacci(n))
        elif  opcion == "4":
            palabra=input("Ingrese una palabra: ")
            resultado= conta_palabra(palabra)
            for letra, cantidad in resultado.items():
                print(f"{letra} = {cantidad}")
        elif opcion == "5":
            break

        elif opcion == "6":
            base=int(input("Ingrese la base: "))
            expo=int(input("Ingrese exponente"))

            resultado=potencial(base,expo)
            print("el resultado es: ",resultado)

        elif opcion == "7":
            print("Secion Finalizada...")
            break
        else:
            print("Opcion Invalida...")

menu()

