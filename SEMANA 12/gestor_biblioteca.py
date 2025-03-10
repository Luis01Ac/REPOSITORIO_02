class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        """Inicializa un libro con título, autor, categoría y ISBN"""
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        """Devuelve una representación legible del libro"""
        return f"'{self.titulo}' de {self.autor} (ISBN: {self.isbn}) - Categoría: {self.categoria}"


class Usuario:
    def __init__(self, nombre, usuario_id):
        """Inicializa un usuario con nombre y ID único"""
        self.nombre = nombre
        self.usuario_id = usuario_id
        self.libros_prestados = []

    def __str__(self):
        """Devuelve una representación legible del usuario"""
        return f"Usuario: {self.nombre} (ID: {self.usuario_id})"

    def listar_libros_prestados(self):
        """Lista los libros que tiene prestados el usuario"""
        if not self.libros_prestados:
            return f"{self.nombre} no tiene libros prestados."
        return f"Libros prestados por {self.nombre}: " + ", ".join([libro.titulo for libro in self.libros_prestados])


class Biblioteca:
    def __init__(self):
        """Inicializa la biblioteca con diccionario de libros y conjunto de usuarios"""
        self.libros = {}  # Diccionario para libros: clave = ISBN, valor = objeto Libro
        self.usuarios = set()  # Conjunto para usuarios únicos
        self.prestamos = {}  # Diccionario para registrar los préstamos de libros

    def añadir_libro(self, libro):
        """Añadir un libro a la biblioteca"""
        if libro.isbn in self.libros:
            return f"El libro con ISBN {libro.isbn} ya está en la biblioteca."
        self.libros[libro.isbn] = libro
        return f"Libro '{libro.titulo}' añadido correctamente."

    def quitar_libro(self, isbn):
        """Quitar un libro de la biblioteca"""
        if isbn not in self.libros:
            return f"El libro con ISBN {isbn} no existe en la biblioteca."
        del self.libros[isbn]
        return f"Libro con ISBN {isbn} eliminado de la biblioteca."

    def registrar_usuario(self, usuario):
        """Registrar un nuevo usuario"""
        if usuario.usuario_id in [u.usuario_id for u in self.usuarios]:
            return f"El usuario con ID {usuario.usuario_id} ya está registrado."
        self.usuarios.add(usuario)
        return f"Usuario {usuario.nombre} registrado correctamente."

    def dar_baja_usuario(self, usuario_id):
        """Eliminar un usuario registrado"""
        usuario = self.buscar_usuario_por_id(usuario_id)
        if not usuario:
            return f"No se encontró un usuario con ID {usuario_id}."
        self.usuarios.remove(usuario)
        return f"Usuario {usuario.nombre} eliminado correctamente."

    def prestar_libro(self, usuario_id, isbn):
        """Prestar un libro a un usuario"""
        usuario = self.buscar_usuario_por_id(usuario_id)
        libro = self.libros.get(isbn)

        if not usuario:
            return f"Usuario con ID {usuario_id} no encontrado."
        if not libro:
            return f"Libro con ISBN {isbn} no encontrado."
        if isbn in self.prestamos:
            return f"El libro '{libro.titulo}' ya está prestado."

        usuario.libros_prestados.append(libro)
        self.prestamos[isbn] = usuario
        return f"Libro '{libro.titulo}' prestado a {usuario.nombre}."

    def devolver_libro(self, usuario_id, isbn):
        """Devolver un libro prestado"""
        usuario = self.buscar_usuario_por_id(usuario_id)
        libro = self.libros.get(isbn)

        if not usuario:
            return f"Usuario con ID {usuario_id} no encontrado."
        if not libro:
            return f"Libro con ISBN {isbn} no encontrado."
        if isbn not in self.prestamos:
            return f"El libro '{libro.titulo}' no está prestado."

        usuario.libros_prestados.remove(libro)
        del self.prestamos[isbn]
        return f"Libro '{libro.titulo}' devuelto correctamente."

    def buscar_libro(self, criterio):
        """Buscar un libro por título, autor o categoría"""
        libros_encontrados = []
        for libro in self.libros.values():
            if criterio.lower() in libro.titulo.lower() or criterio.lower() in libro.autor.lower() or criterio.lower() in libro.categoria.lower():
                libros_encontrados.append(libro)

        if not libros_encontrados:
            return "No se encontraron libros con ese criterio."
        return libros_encontrados

    def buscar_usuario_por_id(self, usuario_id):
        """Buscar un usuario por su ID"""
        for usuario in self.usuarios:
            if usuario.usuario_id == usuario_id:
                return usuario
        return None


# Creamos una biblioteca
biblioteca = Biblioteca()

# Creamos algunos libros (cambiados por nuevos)
libro1 = Libro("El Quijote", "Miguel de Cervantes", "Clásico", "978-3-16-148411-1")
libro2 = Libro("Orgullo y prejuicio", "Jane Austen", "Romántico", "978-0-452-28424-1")

# Añadimos libros a la biblioteca general
print(biblioteca.añadir_libro(libro1))
print(biblioteca.añadir_libro(libro2))

# Crear usuarios (cambiados por Luis Achachi y Liliana Armas)
usuario1 = Usuario("Luis Achachi", "11111")
usuario2 = Usuario("Liliana Armas", "22222")

# Registrar usuarios
print(biblioteca.registrar_usuario(usuario1))
print(biblioteca.registrar_usuario(usuario2))

# Prestar libros
print(biblioteca.prestar_libro("11111", "978-3-16-148411-1"))

# Lista libros prestados de Luis Achachi
print(usuario1.listar_libros_prestados())

# Devolver un libro
print(biblioteca.devolver_libro("11111", "978-3-16-148411-1"))

# Buscar un libro por autor
libros_encontrados = biblioteca.buscar_libro("Jane Austen")
print([str(libro) for libro in libros_encontrados])

# Dar de baja a un usuario
print(biblioteca.dar_baja_usuario("22222"))
