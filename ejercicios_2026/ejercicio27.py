lista_a = [1, 2, 3, 4, 5]
lista_b = [4, 5, 6, 7, 8]

comunes = []

for numero in lista_a:
    if numero in lista_b:
        comunes.append(numero)

print("Los numeros que se repiten son:")
print(comunes)