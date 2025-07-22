def potencia(base,exp)
    if exp==0:
        return 1
    else:
        return base*potencia(exp-1)
base=int(input("Ingrese base: "))

