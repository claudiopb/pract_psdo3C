text = "apple banana apple cherry banana apple"

words = []
palabra_actual = ""

for caracter in text:
    if caracter != " ":
        palabra_actual = palabra_actual + caracter
    else:
        words.append(palabra_actual)
        palabra_actual = ""

words.append(palabra_actual)

frecuencia = {}

for palabra in words:
    existe = False

    for clave in frecuencia:
        if clave == palabra:
            frecuencia[clave] = frecuencia[clave] + 1
            existe = True

    if existe == False:
        frecuencia[palabra] = 1

print(frecuencia)