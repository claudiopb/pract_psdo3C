miarreglo = ['Jones','Jill','Lisa','Stan','Bob','Alice']
print(miarreglo)
print(" ")
i = 0
while i < len(miarreglo):
    print(miarreglo[i])
    if miarreglo[i] == 'Lisa':
        print(f'Encontre a {miarreglo[i]}')
        print("haciendo cambio")
        miarreglo[i] = 'Elisa'
    elif miarreglo[i] == 'Bob':
        print(f'Encontre a {miarreglo[i]}')
        print("haciendo cambio")
        miarreglo[i] = 'Esponja'
    i += 1

print(' ')
print(miarreglo)    
