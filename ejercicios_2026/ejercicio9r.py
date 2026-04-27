sentence = "Learning Python is fun!"
# Convertimos la cadena de vocales en una lista (arreglo)
vowels = ["a", "e", "i", "o", "u"]
count = 0

# Primer bucle: Recorre cada carácter de la frase (Arreglo A)
for letter in sentence:
    letter_lower = letter.lower()
    
    # Segundo bucle: Recorre cada vocal del arreglo de referencia (Arreglo B)
    for v in vowels:
        # Comparamos si la letra de la frase es igual a la vocal actual
        if letter_lower == v:
            count = count + 1
            # Si ya encontramos que es una vocal, no hace falta seguir revisando el resto
            break 

print("Número de vocales:", count)