# ==============================================================================
# BLOQUE 1: DEFINICIÓN DE LA CLASE (El molde)
# ==============================================================================

# 'class Person:' define una nueva clase llamada Person.
# Piensa en ella como un plano arquitectónico o un molde para hacer galletas.
# No es una persona real, sino la plantilla que dice qué características tendrá.
class Person:
    
    # ==========================================================================
    # BLOQUE 2: EL CONSTRUCTOR (La preparación)
    # ==========================================================================
    
    # 'def __init__(...):' es el método constructor.
    # Se ejecuta AUTOMÁTICAMENTE cada vez que creamos una nueva persona.
    # - 'self': Representa al objeto específico que se está creando ("este objeto").
    # - 'name, age, city, country': Son los datos que necesitamos recibir de afuera.
    def __init__(self, name, age, city, country):
        
        # ======================================================================
        # BLOQUE 3: ASIGNACIÓN DE ATRIBUTOS (Guardar los datos)
        # ======================================================================
        
        # Toma el valor recibido en el parámetro 'name' y lo guarda en el atributo interno del objeto.
        self.name = name
        
        # Toma el valor recibido en 'age' y lo guarda en la edad de este objeto.
        self.age = age
        
        # Toma el valor recibido en 'city' y lo guarda en la ciudad de este objeto.
        self.city = city
        
        # Toma el valor recibido en 'country' y lo guarda en el país de este objeto.
        self.country = country


# ==============================================================================
# BLOQUE 4: CREACIÓN DEL OBJETO (Instanciación)
# ==============================================================================

# Aquí usamos el molde 'Person' para crear a alguien real y guardarlo en la variable 'p1'.
# Al pasarle "Linus", 30, "Oslo", "Norway", Python se los envía al método '__init__' de arriba.
# El parámetro 'self' se maneja de forma interna y automática, apuntando a 'p1'.
p1 = Person("Linus", 30, "Oslo", "Norway")


# ==============================================================================
# BLOQUE 5: IMPRESIÓN DE LOS DATOS (Uso de los atributos)
# ==============================================================================

# Usamos la "nomenclatura del punto" (objeto.atributo) para acceder a los datos guardados.
print(p1.name," ",p1.age," ",p1.city," ",p1.country)     # Imprime el nombre guardado en p1: "Linus"
