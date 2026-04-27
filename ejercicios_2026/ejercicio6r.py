# Definimos el número
numero = 5
# Inicializamos la variable en 1 (porque es el elemento neutro de la multiplicación)
factorial = 1

# Usamos range desde 1 hasta numero + 1 para incluir al propio número
for i in range(1, numero + 1):
    factorial = factorial * i

print(f"El factorial de {numero} es: {factorial}")