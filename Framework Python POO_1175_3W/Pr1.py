print(" ")
print("Alvaro Campechano 3W")
print(" ")
class Persona:
    def __init__(self, nombre="", edad=0, dni=""):
        self.nombre, self.edad, self.dni = nombre, edad, dni

    def mostrar(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, DNI: {self.dni}")

    def es_mayor_de_edad(self):
        return self.edad >= 18


# Ejemplo de uso
persona1 = Persona("Juan", 20, "12345678A")
persona1.mostrar()  # Muestra los datos de la persona
print("Es mayor de edad:", persona1.es_mayor_de_edad())  # Verifica si es mayor de edad
