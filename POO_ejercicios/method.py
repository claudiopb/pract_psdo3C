class Person:
  def __init__(self,id,cat, nombre, edad = 16): #constructor
    self.id_person = id
    self.categoria = cat
    self.name = nombre
    self.age = edad
# En esta parte estamos instanciando o creando
# un objeto  persona
persona1 = Person(1,"Estudiante","Emil")
persona2 = Person(2,"Maestro","Jordana",15)

print(persona1.id_person,"",persona1.categoria,"", persona1.name,"",persona1.age)
print(persona2.id_person,"",persona2.categoria,"",persona2.name,"",persona2.age)
