
# Programa: Promedio semanal de temperaturas
# Paradigma: Programación Orientada a Objetos (POO)
# ------------------------------------------------------

# Clase que representa la información del clima semanal
class ClimaSemanal:
    def __init__(self):
        # Encapsulamiento: atributo privado
        self.__temperaturas = []

    # Método para ingresar temperaturas
    def ingresar_temperaturas(self):
        print("=== Ingreso de temperaturas diarias (POO) ===")
        for dia in range(1, 8):
            temp = float(input(f"Ingrese la temperatura del día {dia}: "))
            self.__temperaturas.append(temp)

    # Método para calcular el promedio semanal
    def calcular_promedio(self):
        if len(self.__temperaturas) == 0:
            return None
        return sum(self.__temperaturas) / len(self.__temperaturas)

# Clase hija que podría extender funcionalidad (HERENCIA)
class ClimaExtendido(ClimaSemanal):
    # Ejemplo de polimorfismo: redefinir el método mostrar
    def mostrar_promedio(self):
        promedio = self.calcular_promedio()
        if promedio is not None:
            print(f"\nEl promedio semanal (desde clase extendida) es: {promedio:.2f}°C")
        else:
            print("No se han ingresado temperaturas.")

# Programa principal con POO
def main():
    clima = ClimaExtendido()     # Uso de herencia
    clima.ingresar_temperaturas()
    clima.mostrar_promedio()     # Uso de polimorfismo

# Llamada al programa:
main()
