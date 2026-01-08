# Programa: Calculadora de área de un rectángulo
# Descripción: Este programa solicita al usuario las dimensiones de un rectángulo,
# calcula su área y muestra el resultado en pantalla.

def calcular_area_rectangulo(base, altura):
    """
    Calcula el área de un rectángulo.
    :param base: float, base del rectángulo
    :param altura: float, altura del rectángulo
    :return: float, área calculada
    """
    return base * altura


# Solicitar datos al usuario (tipo string que luego se convierte a float)
nombre_usuario = input("Ingrese su nombre: ")
base_rectangulo = float(input("Ingrese la base del rectángulo: "))
altura_rectangulo = float(input("Ingrese la altura del rectángulo: "))

# Llamar a la función para calcular el área
area = calcular_area_rectangulo(base_rectangulo, altura_rectangulo)

# Variable booleana para validar si el área es mayor que cero
area_valida = area > 0

# Mostrar resultados
print("\nResultados del cálculo:")
print(f"Usuario: {nombre_usuario}")
print(f"Área del rectángulo: {area}")

# Uso del tipo boolean
if area_valida:
    print("El área calculada es válida.")
else:
    print("El área calculada no es válida.")