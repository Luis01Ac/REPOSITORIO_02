# Función para capturar las temperaturas de cada día de la semana
def ingresar_temperaturas():
    temperaturas = []
    for i in range(7):  # Representa los 7 días de la semana
        while True:
            try:
                temperatura = float(input(f"Ingrese la temperatura del día {i + 1}: "))
                temperaturas.append(temperatura)
                break
            except ValueError:
                print("Por favor, ingrese un número válido.")
    return temperaturas


# Función para calcular el valor promedio de las temperaturas registradas
def calcular_promedio(temperaturas):
    total = sum(temperaturas)  # Suma total de las temperaturas ingresadas
    promedio = total / len(temperaturas)  # Cálculo del promedio de temperaturas
    return promedio


# Función principal para orquestar la ejecución del programa
def main():
    print("Bienvenido al programa para calcular el promedio semanal del clima.")

    # Registrar las temperaturas de cada día
    temperaturas = ingresar_temperaturas()

    # Calcular el promedio de las temperaturas de la semana
    promedio = calcular_promedio(temperaturas)

    # Presentar el resultado del promedio
    print(f"\nEl promedio semanal de las temperaturas es: {promedio:.2f} grados Celsius.")


# Iniciar la ejecución del programa
if __name__ == "__main__":
    main()