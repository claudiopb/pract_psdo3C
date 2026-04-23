a = 4
b = 8
print("antes del intercambio:", "a=", a, "b=", b)
a += b   #a= a + b // a = 4 + 8 (12)
b = a-b  #b = 12 - 8 (4)
a -= b   # a = 12 - 4 (8)
print("después del intercambio: a=", a,"b=", b) # a=10/b=5