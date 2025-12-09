
# Programa: Promedio semanal de temperaturas
# Paradigma: Programación Tradicional / Estructurada
# ---------------------------------------------

# Función para ingresar las temperaturas de los 7 días
def ingresar_temperaturas():
    temperaturas = []
    print("=== Ingreso de temperaturas diarias ===")
    for dia in range(1, 8):
        temp = float(input(f"Ingrese la temperatura del día {dia}: "))
        temperaturas.append(temp)
    return temperaturas

# Función para calcular el promedio semanal
def calcular_promedio(temperaturas):
    return sum(temperaturas) / len(temperaturas)

# Programa principal (flujo tradicional)
def main():
    temps = ingresar_temperaturas()       # Obtener datos
    promedio = calcular_promedio(temps)   # Calcular resultado
    print(f"\nEl promedio semanal de temperaturas es: {promedio:.2f}°C")

# Llamada al programa:
main()
