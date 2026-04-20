numeros = [45, 7, 12, 2,89 ]

menor = None
for valor in numeros:
    if menor is None:
        menor = valor
    elif valor < menor:
        menor = valor
        print("Valor minimo:", menor)

mayor = None
for valor2 in numeros:
    if mayor is None:
        mayor = valor2
    elif valor2 > mayor:
        mayor = valor2
        print("Valor maximo:", mayor)