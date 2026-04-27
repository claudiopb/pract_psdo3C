# 1. Lista con duplicados
lista = [1, 2, 2, 3, 4, 4, 4, 5]

# 2. Lista para elementos únicos
lista_aux = []

# 3. Recorremos cada número de la lista original
for numero in lista:
    
    # Creamos una "bandera" o interruptor
    ya_existe = False
    
    # 4. Segundo ciclo: revisamos si el número ya está en lista_unica
    for unico in lista_aux:
        if numero == unico:
            ya_existe = True
            break # Si lo encontramos, dejamos de buscar en este ciclo
            
    # 5. Si después de revisar toda la lista_unica, la bandera sigue en False...
    if ya_existe == False:
        # ...entonces el número es nuevo y lo agregamos
        lista_aux += [numero]

# 6. Resultado
print(lista_aux)