data = [1, 2, 2, 3, 4, 4, 4, 5]

unique_list = []

for elemento in data:
    if elemento not in unique_list:
        unique_list = unique_list + [elemento]

print("Lista original:", data)
print("Lista sin duplicados:", unique_list)
#corregir