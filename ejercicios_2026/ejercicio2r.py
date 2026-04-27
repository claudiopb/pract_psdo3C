# Inicializamos el número anterior en 0
numero_anterior = 0

print("Imprimir la suma del número actual y anterior en un rango (10)")
for i in range(10):
    suma = i + numero_anterior
    print(f"Número actual: {i} | Número anterior: {numero_anterior} | Suma: {suma}")
    
    # Actualizamos el número anterior para la siguiente iteración
    numero_anterior = i