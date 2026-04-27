def eliminar_caracteres(cadena, n):
    # Creamos una cadena vacía para guardar el resultado
    nueva_cadena = ""
    
    # Empezamos el ciclo desde el índice n + 1 hasta el final
    # (n + 1 porque queremos eliminar HASTA el índice n inclusive)
    for i in range(n, len(cadena)):
        nueva_cadena += cadena[i]
        
    return nueva_cadena

# Prueba con "pynative" eliminando hasta el índice 3
# Los índices 0, 1, 2, 3 son 'p', 'y', 'n', 'a'
resultado = eliminar_caracteres("pynative", 4)
print(resultado) # Debería imprimir: tive
resultado = eliminar_caracteres("pynative", 2)
print(resultado) # Debería imprimir: tive