class Clima:
    def __init__(self):
        # Crear una estructura para almacenar las temperaturas de cada día
        self.temperaturas_diarias = []

    def registrar_temperaturas(self):
        # Función para capturar las temperaturas de todos los días de la semana
        for dia in range(7):  # Existen 7 días en una semana
            while True:
                try:
                    temp = float(input(f"Por favor, ingrese la temperatura del día {dia + 1}: "))
                    self.temperaturas_diarias.append(temp)
                    break
                except ValueError:
                    print("Ingreso no válido. Asegúrese de ingresar un número.")

    def obtener_promedio(self):
        # Función para calcular el promedio de las temperaturas ingresadas
        if len(self.temperaturas_diarias) == 7:
            suma_temperaturas = sum(self.temperaturas_diarias)
            promedio = suma_temperaturas / len(self.temperaturas_diarias)
            return promedio
        else:
            return None  # Si no se registran todas las temperaturas, no se puede calcular el promedio

    def mostrar_promedio(self):
        # Función para mostrar el promedio calculado
        promedio = self.obtener_promedio()
        if promedio is not None:
            print(f"\nEl promedio de temperaturas para la semana es: {promedio:.2f}°C.")
        else:
            print("No se pudo calcular el promedio. Verifique que haya ingresado todas las temperaturas correctamente.")


# Función principal que coordina la ejecución del programa
def ejecutar_programa():
    print("Bienvenido al programa de cálculo del promedio de temperaturas semanales.")

    # Crear un objeto para manejar las temperaturas
    clima = Clima()

    # Registrar las temperaturas de los 7 días
    clima.registrar_temperaturas()

    # Calcular y mostrar el promedio de las temperaturas ingresadas
    clima.mostrar_promedio()


# Ejecutar el programa si este archivo es el principal
if __name__ == "__main__":
    ejecutar_programa()