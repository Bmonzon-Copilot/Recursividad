def factorial(n):
    if n==0:
        return 1
    else:
        print()
        return n*factorial(n-1)

n=input("Ingrese un numero: ")
print(factorial(n))
