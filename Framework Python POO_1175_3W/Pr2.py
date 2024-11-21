print(" ")
print("Alvaro Campechano 3W")
print(" ")
class Persona:
    def __init__(self, nombre="", edad=0, dni=""):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    def mostrar(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, DNI: {self.dni}")

    def es_mayor_de_edad(self):
        return self.edad >= 18


class Cuenta:
    def __init__(self, titular, cantidad=0.0):
        if not isinstance(titular, Persona):
            raise ValueError("El titular debe ser una Persona")
        self.titular = titular
        self.cantidad = cantidad

    def mostrar(self):
        print(f"Titular: {self.titular.nombre}, Cantidad: {self.cantidad} €")

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.cantidad += cantidad

    def retirar(self, cantidad):
        if cantidad > 0:
            self.cantidad -= cantidad


# Ejemplo de uso:
persona1 = Persona("Juan", 20, "12345678A")
cuenta1 = Cuenta(persona1, 1000)
cuenta1.mostrar()

cuenta1.ingresar(500)
cuenta1.mostrar()

cuenta1.retirar(200)
cuenta1.mostrar()
