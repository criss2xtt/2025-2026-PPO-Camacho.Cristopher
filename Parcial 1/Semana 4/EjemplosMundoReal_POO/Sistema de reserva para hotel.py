# Clase Habitacion
# Representa una habitacion del hotel
class Habitacion:
    def __init__(self, numero, tipo, precio):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.disponible = True

    # Metodo para reservar la habitacion
    def reservar(self):
        if self.disponible:
            self.disponible = False
            return True
        return False

    # Metodo para liberar la habitacion
    def liberar(self):
        self.disponible = True


# Clase Cliente
# Representa a un cliente del hotel
class Cliente:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula


# Clase Reserva
# Relaciona un cliente con una habitacion
class Reserva:
    def __init__(self, cliente, habitacion, dias):
        self.cliente = cliente
        self.habitacion = habitacion
        self.dias = dias

    # Metodo para calcular el costo total de la reserva
    def calcular_total(self):
        return self.habitacion.precio * self.dias


# Ejemplo de uso del sistema
habitacion1 = Habitacion(101, "Doble", 40)
cliente1 = Cliente("Cristopher Camacho", "1004676528")

if habitacion1.reservar():
    reserva1 = Reserva(cliente1, habitacion1, 3)
    print("Reserva realizada")
    print("Cliente:", reserva1.cliente.nombre)
    print("Habitacion:", reserva1.habitacion.numero)
    print("Total a pagar:", reserva1.calcular_total())
else:
    print("Habitacion no disponible")
