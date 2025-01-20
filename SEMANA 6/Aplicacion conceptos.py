# Clase Animal
class Animal:
    def __init__(self, nombre, edad, especie):
        # Atributos privados (encapsulación)
        self.__nombre = nombre
        self.__edad = edad
        self.__especie = especie

    # Métodos getter y setter para los atributos privados
    def obtener_nombre(self):
        return self.__nombre

    def obtener_edad(self):
        return self.__edad

    def obtener_especie(self):
        return self.__especie

    def establecer_nombre(self, nombre):
        self.__nombre = nombre

    def establecer_edad(self, edad):
        self.__edad = edad

    def establecer_especie(self, especie):
        self.__especie = especie

    # Método común para hacer sonido, debe ser sobrescrito
    def hacer_sonido(self):
        raise NotImplementedError("Este método debe ser sobrescrito en una clase derivada")

    # Método para mostrar información del animal
    def mostrar_info(self):
        return f"{self.__nombre} es un {self.__especie} de {self.__edad} años."


# Clase derivada León
class Leon(Animal):
    def __init__(self, nombre, edad):
        # Llamada al constructor de la clase base
        super().__init__(nombre, edad, "León")

    # Método sobrescrito para hacer el sonido específico del león
    def hacer_sonido(self):
        return "¡Rugido del león!"

    # Método específico para el león
    def cazar(self):
        return "El león va a cazar en la selva."


# Clase derivada Loro
class Loro(Animal):
    def __init__(self, nombre, edad):
        # Llamada al constructor de la clase base
        super().__init__(nombre, edad, "Loro")

    # Método sobrescrito para hacer el sonido específico del loro
    def hacer_sonido(self):
        return "¡Hola! ¡Hola!"

    # Método específico para el loro
    def hablar(self):
        return "El loro está repitiendo palabras."


# Crear instancias de las clases
leon = Leon("Simba", 5)
loro = Loro("Poli", 2)

# Mostrar información general de los animales
print(leon.mostrar_info())  # Polimorfismo: León
print(loro.mostrar_info())  # Polimorfismo: Loro

# Usar métodos sobrescritos
print(leon.hacer_sonido())  # Método sobrescrito en León
print(loro.hacer_sonido())  # Método sobrescrito en Loro

# Usar métodos específicos de cada clase
print(leon.cazar())         # Método específico de León
print(loro.hablar())        # Método específico de Loro

# Modificar atributos a través de los setters
leon.establecer_nombre("Mufasa")
loro.establecer_edad(3)

# Mostrar los nuevos valores de los atributos
print(f"El nuevo nombre del león es: {leon.obtener_nombre()}")
print(f"La nueva edad del loro es: {loro.obtener_edad()}")
