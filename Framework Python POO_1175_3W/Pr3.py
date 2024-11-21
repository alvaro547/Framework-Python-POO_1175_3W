print(" ")
print("Alvaro Campechano 3W")
print(" ")
class Persona:
    def __init__(self, nombre="", edad=0, dni=""):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

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


class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad=0.0, bonificacion=0.0):
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion

    def es_titular_valido(self):
        return 18 <= self.titular.edad < 25

    def mostrar(self):
        if self.es_titular_valido():
            print(f"Cuenta Joven - Titular: {self.titular.nombre}, Bonificación: {self.bonificacion}%")
        else:
            print("Titular no válido para Cuenta Joven.")

    def retirar(self, cantidad):
        if self.es_titular_valido():
            super().retirar(cantidad)
        else:
            print("No puede retirar dinero. Titular no válido.")
            

# Ejemplo de uso:
persona1 = Persona("Juan", 20, "12345678A")
cuenta_joven1 = CuentaJoven(persona1, 500, 5)
cuenta_joven1.mostrar()

cuenta_joven1.retirar(100)
cuenta_joven1.mostrar()

persona2 = Persona("Ana", 17, "87654321B")
cuenta_joven2 = CuentaJoven(persona2, 300, 3)
cuenta_joven2.mostrar()  # No válida
