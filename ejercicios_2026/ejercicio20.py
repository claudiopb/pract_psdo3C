i = 1
while i <= 10:
    j = 1
    while j <= 10:
        num = i * j
        
        # Para alinear los números en forma de tabla
        if num < 10:
            print(num, end="   ")
        elif num < 100:
            print(num, end="  ")
        else:
            print(num, end=" ")
        
        j = j + 1
    
    print()  # Salto de línea para la siguiente fila
    i = i + 1