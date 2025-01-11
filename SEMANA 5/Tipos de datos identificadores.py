# Programa para convertir temperaturas entre grados Celsius y Fahrenheit.
# Funcionalidad:
# El programa permite convertir una temperatura de grados Celsius a Fahrenheit
# o de Fahrenheit a Celsius, y luego muestra el resultado de la conversión.

# Función para convertir Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius: float) -> float:
    """
    Convierte una temperatura de grados Celsius a Fahrenheit.

    Parámetros:
    celsius (float): Temperatura en grados Celsius.

    Retorna:
    float: Temperatura convertida en grados Fahrenheit.
    """
    return (celsius * 9 / 5) + 32


# Función para convertir Fahrenheit a Celsius
def fahrenheit_a_celsius(fahrenheit: float) -> float:
    """
    Convierte una temperatura de grados Fahrenheit a Celsius.

    Parámetros:
    fahrenheit (float): Temperatura en grados Fahrenheit.

    Retorna:
    float: Temperatura convertida en grados Celsius.
    """
    return (fahrenheit - 32) * 5 / 9


# Función principal que muestra el menú y maneja las opciones del usuario
def menu():
    """
    Muestra un menú para que el usuario elija la opción de conversión de temperatura.
    """
    while True:
        print("\nSeleccione una opción:")
        print("1. Convertir de Celsius a Fahrenheit")
        print("2. Convertir de Fahrenheit a Celsius")
        print("3. Salir")

        # Solicitar al usuario que ingrese su opción
        opcion = input("Ingrese el número de la opción que desea: ")

        # Validar la opción ingresada
        if opcion == '1':
            # Solicitar temperatura en Celsius y convertir a Fahrenheit
            celsius = float(input("Ingrese la temperatura en grados Celsius: "))
            fahrenheit = celsius_a_fahrenheit(celsius)
            print(f"{celsius} grados Celsius equivalen a {fahrenheit:.2f} grados Fahrenheit.")

        elif opcion == '2':
            # Solicitar temperatura en Fahrenheit y convertir a Celsius
            fahrenheit = float(input("Ingrese la temperatura en grados Fahrenheit: "))
            celsius = fahrenheit_a_celsius(fahrenheit)
            print(f"{fahrenheit} grados Fahrenheit equivalen a {celsius:.2f} grados Celsius.")

        elif opcion == '3':
            # Salir del programa
            print("Gracias por usar el programa. ¡Hasta luego!")
            break

        else:
            # Opción no válida
            print("Opción no válida. Por favor, elija una opción válida.")


# Función principal que ejecuta el programa
if __name__ == "__main__":
    menu()