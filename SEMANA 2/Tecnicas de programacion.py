import random
# Clase base Personaje
class Personaje:
    def __init__(self, nombre, fuerza, inteligencia, habilidad, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.habilidad = habilidad  # Habilidad especial para la exploración
        self.vida = vida
        self.experiencia = 0
        self.objetos = []

    def atributos(self):
        print(self.nombre, ":", sep="")
        print("·Fuerza:", self.fuerza)
        print("·Inteligencia:", self.inteligencia)
        print("·Habilidad:", self.habilidad)
        print("·Vida:", self.vida)
        print("·Experiencia:", self.experiencia)
        print("·Objetos:", self.objetos)

    def subir_nivel(self):
        if self.experiencia >= 100:
            self.experiencia -= 100
            self.fuerza += 5
            self.inteligencia += 5
            self.habilidad += 5
            print(self.nombre, "ha subido de nivel!")
        else:
            print(self.nombre, "no tiene suficiente experiencia para subir de nivel.")

    def realizar_mision(self):
        mision_tipo = random.choice(["Recolección", "Exploración", "Comercio", "Estudio"])
        if mision_tipo == "Recolección":
            self.mision_recoleccion()
        elif mision_tipo == "Exploración":
            self.mision_exploracion()
        elif mision_tipo == "Comercio":
            self.mision_comercio()
        else:
            self.mision_estudio()

    def mision_recoleccion(self):
        exp_ganada = random.randint(10, 20)
        self.experiencia += exp_ganada
        objeto = random.choice(["Hierro", "Piedra preciosa", "Hierbas medicinales"])
        self.objetos.append(objeto)
        print(self.nombre, "ha realizado una misión de recolección y ha ganado", exp_ganada, "puntos de experiencia.")
        print("Ha encontrado un objeto:", objeto)

    def mision_exploracion(self):
        exp_ganada = random.randint(20, 30)
        self.experiencia += exp_ganada
        lugar_descubierto = random.choice(["Ruinas Antiguas", "Bosque Encantado", "Montañas Misteriosas"])
        print(self.nombre, "ha explorado un nuevo lugar:", lugar_descubierto)
        print(self.nombre, "ha ganado", exp_ganada, "puntos de experiencia.")

    def mision_comercio(self):
        exp_ganada = random.randint(5, 15)
        self.experiencia += exp_ganada
        objeto_comercio = "Monedas de oro"
        self.objetos.append(objeto_comercio)
        print(self.nombre, "ha completado una misión de comercio y ha ganado", exp_ganada, "puntos de experiencia.")
        print("Ha intercambiado objetos por:", objeto_comercio)

    def mision_estudio(self):
        exp_ganada = random.randint(15, 25)
        self.experiencia += exp_ganada
        print(self.nombre, "ha completado una misión de estudio y ha ganado", exp_ganada, "puntos de experiencia.")
        print(self.nombre, "ha aprendido algo nuevo sobre el mundo.")

    def interactuar(self, objeto):
        if isinstance(objeto, ObjetoMagico):
            print(self.nombre, "ha interactuado con el objeto mágico y ha ganado 20 puntos de habilidad.")
            self.habilidad += 20

# Clase Guerrero (Subclase de Personaje)
class Guerrero(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, habilidad, vida):
        super().__init__(nombre, fuerza, inteligencia, habilidad, vida)

    def atributos(self):
        super().atributos()

    def realizar_mision(self):
        super().realizar_mision()

# Clase Mago (Subclase de Personaje)
class Mago(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, habilidad, vida):
        super().__init__(nombre, fuerza, inteligencia, habilidad, vida)

    def atributos(self):
        super().atributos()

    def realizar_mision(self):
        super().realizar_mision()

# Clase ObjetoMagico
class ObjetoMagico:
    def __init__(self, nombre, poder):
        self.nombre = nombre
        self.poder = poder

    def interactuar(self, personaje):
        if self.poder == "habilidad":
            personaje.habilidad += 20
            print(personaje.nombre, "ha ganado 20 puntos de habilidad al interactuar con el objeto mágico:", self.nombre)

# Función de Aventura
def aventura(jugador):
    print("\nIniciando aventura para", jugador.nombre)
    jugador.realizar_mision()
    jugador.subir_nivel()
    jugador.atributos()

# Crear personajes
personaje_1 = Guerrero("Luis", 15, 10, 5, 100)
personaje_2 = Mago("Diego", 5, 20, 4, 100)

# Crear un objeto mágico
objeto_magico = ObjetoMagico("Cristal de Sabiduría", "habilidad")

# Interacción de los personajes con el objeto mágico
personaje_1.interactuar(objeto_magico)
personaje_2.interactuar(objeto_magico)

# Mostrar atributos después de la interacción
personaje_1.atributos()
personaje_2.atributos()

# Realizar una aventura con ambos personajes
aventura(personaje_1)
aventura(personaje_2)