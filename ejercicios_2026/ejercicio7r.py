# 1. Definimos la lista inicial con 5 frutas
# Cada fruta tiene un índice (0 a 4)
frutas = ["apple", "banana", "cherry", "date", "elderberry"]

# 2. Agregamos "fig" al final de la lista
# Usamos [] para que "fig" sea una lista y se pueda sumar con la lista 'frutas'
frutas = frutas + ["fig"]

# 3. Creamos una lista vacía que servirá como "contenedor" temporal
# Aquí guardaremos solo las frutas que queremos mantener
lista_final = []

# 4. Iniciamos un ciclo que recorrerá los números desde 0 hasta el final de la lista
# range(len(frutas)) genera los índices: 0, 1, 2, 3, 4, 5
for i in range(len(frutas)):
    
    # Condición: Si el índice actual (i) NO es igual a 1
    # Esto filtrará la fruta en la posición 1 ("banana")
    if i != 1:
        # Agregamos la fruta de la posición actual a nuestra lista_final
        # frutas[i] accede al nombre de la fruta usando su índice
        lista_final += [frutas[i]]

# 5. Sobrescribimos la variable original 'frutas' con el contenido de 'lista_final'
frutas = lista_final

# 6. Mostramos el resultado final por pantalla
print(frutas)