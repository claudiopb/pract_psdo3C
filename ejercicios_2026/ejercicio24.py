terms = int(input("¿Cuantos términos de la serie deseas? "))
a = 0
b = 1

for i in range(terms):
    print(a, end=" ")
    a, b = b, a + b