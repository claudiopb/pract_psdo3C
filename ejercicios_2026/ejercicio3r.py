cadena = "pynative"

print(f"Cadena original: {cadena}")
print(f"Caracteres en índices pares:")

# Recorremos el rango de la longitud de la cadena
for i in range(len(cadena)):
    # Verificamos si el índice actual es divisible entre 2
    if i % 2 == 0:
        print(cadena[i])