



# Create a class
class Person:
    def __init__(self,nom = "Claudio",edad = 48  ):
        self.name = nom
        self.age = edad


    def saludar(self):
        print("hola mi nombre es: " + self.name +  " y mi edad es:",self.age, "años")
# Create an object
claudio = Person()
brayan = Person("Brayan",16)
agustin = Person("AGUSTIN",16)
luis = Person("Luis Eduardo")
# Call the greet method
claudio.saludar()
brayan.saludar()
agustin.saludar()
luis.saludar()