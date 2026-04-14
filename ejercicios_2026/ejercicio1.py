def valores(a,b):
    resultado = a * b
    if resultado <=1000:
        return print (resultado)
    else:
        return print(a + b)

a = int(input("Introduzca el primer número:"))
b = int(input("Introduzca el segundo número:"))

valores(a,b)

