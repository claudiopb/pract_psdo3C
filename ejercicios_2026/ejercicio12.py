numbers_x = [10,20,30,40,10]
numbers_y = [75,65,35,75,35]

for listas in [numbers_x, numbers_y]:
    comparacion= len(listas)
    if listas[0] == listas[comparacion - 1]:
        print("Lista dada:",listas, "|" "el resultado es verdadero")
    else:
        print("Lista dada:",listas, "|" "el resultado es falso")