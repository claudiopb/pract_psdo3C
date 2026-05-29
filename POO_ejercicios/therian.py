class Therian :
    def __init__(self, nombre, especie):
        self.nombre = nombre
        self.especie = especie
    def presenta (self):
        print("Soy un therian y mi nombre es", self.nombre, "y soy un", self.especie)
alejandra = Therian("Mary", "gato")
alejandra.presenta()