# Clase Producto
# Representa un producto disponible en la tienda
class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    # Metodo para reducir el stock al realizar una venta
    def vender(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
            return True
        return False


# Clase Cliente
# Representa a un cliente que compra en la tienda
class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre


# Clase Venta
# Maneja la venta de productos a un cliente
class Venta:
    def __init__(self, cliente):
        self.cliente = cliente
        self.productos = []

    # Metodo para agregar productos a la venta
    def agregar_producto(self, producto, cantidad):
        if producto.vender(cantidad):
            self.productos.append((producto, cantidad))
        else:
            print("Stock insuficiente para", producto.nombre)

    # Metodo para calcular el total de la venta
    def calcular_total(self):
        total = 0
        for producto, cantidad in self.productos:
            total += producto.precio * cantidad
        return total


# Ejemplo de uso del sistema
producto1 = Producto("Laptop", 650, 3)
producto2 = Producto("Mouse", 20, 7)

cliente1 = Cliente("Ariana")

venta1 = Venta(cliente1)
venta1.agregar_producto(producto1, 1)
venta1.agregar_producto(producto2, 2)

print("Cliente:", venta1.cliente.nombre)
print("Total a pagar:", venta1.calcular_total())
