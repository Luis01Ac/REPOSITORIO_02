class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        """Inicializa un libro con título, autor, categoría y ISBN"""
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"'{self.titulo}' de {self.autor} (ISBN: {self.isbn}) - Categoría: {self.categoria}"


class Usuario:
    def __init__(self, nombre, usuario_id):
        """Inicializa un usuario con nombre y ID único"""
        self.nombre = nombre
        self.usuario_id = usuario_id
        self.libros_prestados = []

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.usuario_id})"


class Biblioteca:
    def __init__(self):
        """Inicializa la biblioteca con diccionario de libros y lista de usuarios"""
        self.libros = {}  # Diccionario de libros con ISBN
        self.usuarios = {}  # Diccionario de usuarios con ID de usuario

    def añadir_libro(self, libro):
        """Añadir un libro a la biblioteca"""
        self.libros[libro.isbn] = libro

    def registrar_usuario(self, usuario):
        """Registrar un usuario en la biblioteca"""
        self.usuarios[usuario.usuario_id] = usuario

    def prestar_libro(self, usuario_id, isbn):
        """Prestar un libro a un usuario"""
        if usuario_id not in self.usuarios:
            return "Usuario no encontrado"
        if isbn not in self.libros:
            return "Libro no encontrado"
        usuario = self.usuarios[usuario_id]
        libro = self.libros[isbn]
        usuario.libros_prestados.append(libro)
        return f"Libro '{libro.titulo}' prestado a {usuario.nombre}"

    def devolver_libro(self, usuario_id, isbn):
        """Devolver un libro prestado por un usuario"""
        if usuario_id not in self.usuarios:
            return "Usuario no encontrado"
        if isbn not in self.libros:
            return "Libro no encontrado"
        usuario = self.usuarios[usuario_id]
        libro = self.libros[isbn]
        if libro in usuario.libros_prestados:
            usuario.libros_prestados.remove(libro)
            return f"Libro '{libro.titulo}' devuelto correctamente"
        return "El libro no está prestado a este usuario"

    def buscar_libro(self, criterio):
        """Buscar libro por título o autor"""
        resultado = []
        for libro in self.libros.values():
            if criterio.lower() in libro.titulo.lower() or criterio.lower() in libro.autor.lower():
                resultado.append(libro)
        return resultado if resultado else "No se encontraron libros"

    def listar_libros_prestados(self, usuario_id):
        """Listar los libros prestados a un usuario"""
        if usuario_id not in self.usuarios:
            return "Usuario no encontrado"
        usuario = self.usuarios[usuario_id]
        return [libro.titulo for libro in usuario.libros_prestados]


# Crear objetos de la biblioteca, libros y usuarios
biblioteca = Biblioteca()

# Crear libros
libro1 = Libro("El Quijote", "Miguel de Cervantes", "Clásico", "978-3-16-148411-1")
libro2 = Libro("Orgullo y prejuicio", "Jane Austen", "Romántico", "978-0-452-28424-1")

# Añadir libros a la biblioteca
biblioteca.añadir_libro(libro1)
biblioteca.añadir_libro(libro2)

# Crear usuarios
usuario1 = Usuario("Luis Achachi", "11111")
usuario2 = Usuario("Liliana Armas", "22222")

# Registrar usuarios
biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)

# Prestar libros
print(biblioteca.prestar_libro("11111", "978-3-16-148411-1"))

# Listar libros prestados de Luis Achachi
print(biblioteca.listar_libros_prestados("11111"))

# Devolver libro
print(biblioteca.devolver_libro("11111", "978-3-16-148411-1"))

# Buscar libros por autor
libros_encontrados = biblioteca.buscar_libro("Jane Austen")
for libro in libros_encontrados:
    print(libro)

# Listar libros prestados de Luis Achachi (debería estar vacío)
print(biblioteca.listar_libros_prestados("11111"))

