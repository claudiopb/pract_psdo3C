# 1. Crea una clase llamada Person
class Person:
    
    # 2. Agregue un método __init__ que tome name y age como parámetros
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    # 3. Agregue un método llamado greet que imprima "Hola, mi nombre es " seguido del nombre
    def greet(self):
        print("Hola, mi nombre es " + self.name)
    #Detalles clave a tener en cuenta:
    #El parámetro self: Recuerda que dentro de la clase, el método greet necesita llevar self 
    # entre sus paréntesis para poder tener acceso a las variables del objeto (en este caso, a self.name).

    #Llamar al método: Para activar la función greet en tu objeto p1, usamos la sintaxis de 
    # punto: p1.greet(). No es necesario pasarle ningún argumento entre los paréntesis porque 
    # Python pasa el self automáticamente.

# 4. Crea un objeto p1 de la clase con el nombre "John" y la edad 36
p1 = Person("John", 36)

# 5. Llama al método greet en p1
p1.greet()