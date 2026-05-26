import random
Tazas = 1200
Cantidad = Tazas
Precio_N = 50
Tazas_N = Precio_N * Tazas
Precio_F = 80
Ganancias = 0
count = 0
count_S = 0
count_N =0
Clientes = ["Ana", "Beto", "Camila", "Daniel","Esmeralda", "Florencio", "Guillermina", "Hector", "Irma", "Jose", "Kiara","Luis", "Mariana", "Nohe","Osmari", "Plutarco", "Rita", "Sandro", "Talia", "Ulises", "Vania", "Wulbert", "Xochitl", "Yoel", "Zaira"]

print ("----- INKCUP STUDIO-----")
print ("¡Bienvenido al interfás de InkCup Studio!")

print ("")
print ("Cantidad de tazas almacenadas: ",Tazas)
print ("")
print ("-------------------------------------------------")
print ("")

while Tazas > 0:
    count +=1
    Pedido = random.randint(1,8) * 12
    print ("¡Ha surgido un nuevo pedido de", Pedido, "tazas!")
    print ((Clientes[random.randint(0,24)]),"solicita", Pedido, "tazas")
    print ("El precio por el pedido es de: $", Precio_F*Pedido, "¿Aceptar pedido?")
    print ("")
    if Tazas < Pedido:
        count_N +=1
        print ("No hay suficientes tazas para completar el pedido")
        print ("")
        print ("Ganancia totales = $", Ganancias," Tazas restantes = ", Tazas)
        print ("")
        print ("--------------------------------------------")
        print ("")
    else:  
        Respuesta = int(input("Escriba 1 si acepta Escriba 2 si rechaza R= "))
        while Respuesta <0 or Respuesta >2:
            print ("")
            print ("NÚMERO NO VALIDO")
            print ("")
            Respuesta = int(input("Escriba 1 si acepta Escriba 2 si rechaza R= "))

        if Respuesta == 1:
            count_S +=1
            Ganancias += Precio_F*Pedido
            Tazas -= Pedido
            print ("")
            print ("¡Pedido aceptado!")
            print ("")
            print ("Ganancia totales = $", Ganancias," Tazas restantes = ", Tazas)
            print ("")
            print ("--------------------------------------------")
        else:
            count_N +=1
            print ("")
            print ("Pedido rechazado D:")
            print ("")
            print ("--------------------------------------------")

print ("--------------------------------------------")
print ("")
print ("¡¡¡LAS TAZAS SE HAN TERMINADO!!!")
print ("")
Porcentaje = int(((Ganancias - (Tazas_N)) *100) / (Tazas_N))
print ("")
print ("")
print ("Ganancias totales = $", Ganancias)
print ("Dinero invertido en fabricar las tazas = $", Precio_N * Cantidad)
print ("Ganancia general de la venta = $", Ganancias - Precio_N * Cantidad, " Porcentaje de ganancia = %", Porcentaje)
print ("")
print ("Pedidos totales = ", count, " Pedidos aceptados = ", count_S, " Pedidos rechazados = ", count_N)

#TEAM BOUNCYBALL