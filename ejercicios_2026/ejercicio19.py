# Primer tramo: 0% hasta 10,000
if income > 10000:
    tax += 0  # No se suma nada
else:
    tax += income * 0
    print("Impuesto total:", tax)
    exit()

# Segundo tramo: 10% sobre los siguientes 10,000
if income > 20000:
    tax += 10000 * 0.10
else:
    tax += (income - 10000) * 0.10
    print("Impuesto total:", tax)
    exit()

# Tercer tramo: 20% sobre el resto
tax += (income - 20000) * 0.20

# Resultado final
print("impuesto total:" , int(tax))