class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def greet(self):
    print("Hello, my name is " + self.name)

p1 = Person("Emil", 25)
p1.greet()

class perro:
  def __init__(self,nombre,edad):
    self.nombre = nombre
    self.edad = edad

  def ladrar(self):
    print("El nombre del perro es " + self.nombre + "y ladro !Guau Guau¡")

d1 = perro("Buddy",3)
d1.ladrar()

