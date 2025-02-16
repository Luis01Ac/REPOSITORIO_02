from producto import Producto


class Inventario:
    def __init__(self):
        """Inicializa el inventario como una lista vacía."""
        self.productos = []

    def añadir_producto(self, producto):
        """Añade un nuevo producto al inventario.
        Verifica si el ID es único.

        :param producto: Objeto Producto.
        """
        # Verificamos si el ID del producto ya existe en el inventario
        if self.buscar_producto_por_id(producto.get_producto_id()) is not None:
            print("Error: El ID del producto ya existe.")
        else:
            # Si el ID es único, lo añadimos al inventario
            self.productos.append(producto)
            print(f"Producto {producto.get_nombre()} añadido exitosamente.")

    def eliminar_producto(self, producto_id):
        """Elimina un producto del inventario por su ID.

        :param producto_id: ID del producto a eliminar.
        """
        producto = self.buscar_producto_por_id(producto_id)
        if producto:
            # Si el producto existe, lo eliminamos
            self.productos.remove(producto)
            print(f"Producto con ID {producto_id} eliminado.")
        else:
            print("Error: Producto no encontrado.")

    def actualizar_producto(self, producto_id, cantidad=None, precio=None):
        """Actualiza la cantidad o el precio de un producto por su ID.

        :param producto_id: ID del producto a actualizar.
        :param cantidad: Nueva cantidad (opcional).
        :param precio: Nuevo precio (opcional).
        """
        producto = self.buscar_producto_por_id(producto_id)
        if producto:
            # Si se proporciona una cantidad, se actualiza
            if cantidad is not None:
                producto.set_cantidad(cantidad)
            # Si se proporciona un precio, se actualiza
            if precio is not None:
                producto.set_precio(precio)
            print(f"Producto con ID {producto_id} actualizado.")
        else:
            print("Error: Producto no encontrado.")

    def buscar_producto_por_id(self, producto_id):
        """Busca un producto en el inventario por su ID.

        :param producto_id: ID del producto.
        :return: Objeto Producto si lo encuentra, None si no.
        """
        # Recorre la lista de productos y retorna el que tenga el ID correspondiente
        for producto in self.productos:
            if producto.get_producto_id() == producto_id:
                return producto
        return None

    def buscar_productos_por_nombre(self, nombre):
        """Busca productos por nombre (pueden ser similares).

        :param nombre: Nombre del producto.
        :return: Lista de productos que contienen el nombre.
        """
        # Filtra los productos que contengan el nombre ingresado (sin importar mayúsculas o minúsculas)
        productos_encontrados = [producto for producto in self.productos if
                                 nombre.lower() in producto.get_nombre().lower()]
        return productos_encontrados

    def mostrar_productos(self):
        """Muestra todos los productos en el inventario."""
        if not self.productos:
            print("El inventario está vacío.")
        else:
            # Si hay productos, los imprime uno por uno
            for producto in self.productos:
                print(f"ID: {producto.get_producto_id()}, Nombre: {producto.get_nombre()}, "
                      f"Cantidad: {producto.get_cantidad()}, Precio: {producto.get_precio()}")
