"""
**Ejercicio: Suma descendente**

Escribe un programa en Python que solicite al usuario un número entero positivo y calcule la suma de todos los números desde ese número hasta 0, mostrando el proceso paso a paso.

**Requisitos:**
- El programa debe pedir al usuario que ingrese un número entero
- Debe calcular la suma de todos los números desde el número ingresado hasta 0
- Debe mostrar la operación completa, por ejemplo:
  - Entrada: 4
  - Salida: 4 + 3 + 2 + 1 + 0 = 10

**Restricciones:**
- El número ingresado debe ser mayor o igual a 0
- Si el usuario ingresa un número negativo, el programa debe mostrar un mensaje de error
"""
sum = 0
print("Programa que calcula la sumaria de un numero")
num = int(input("Ingresa un nuemro : "))
aux = num
while num > 0:
    if num <= 0:
        print("Error no deben ser numeros menoras a cero")
    else:
        
        sum = sum + num
        num = num - 1

print(f'La sumatoria del numero {aux} ',sum)

