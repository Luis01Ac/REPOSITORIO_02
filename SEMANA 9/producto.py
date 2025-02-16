class Producto:
    def __init__(self, producto_id, nombre, cantidad, precio):
        """
        Constructor para la clase Producto.
        Inicializa los atributos con los valores proporcionados.

        :param producto_id: ID único del producto.
        :param nombre: Nombre del producto.
        :param cantidad: Cantidad disponible del producto.
        :param precio: Precio del producto.
        """
        self.producto_id = producto_id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def get_producto_id(self):
        """Retorna el ID del producto."""
        return self.producto_id

    def get_nombre(self):
        """Retorna el nombre del producto."""
        return self.nombre

    def get_cantidad(self):
        """Retorna la cantidad disponible del producto."""
        return self.cantidad

    def get_precio(self):
        """Retorna el precio del producto."""
        return self.precio

    def set_cantidad(self, cantidad):
        """Establece la cantidad del producto."""
        self.cantidad = cantidad

    def set_precio(self, precio):
        """Establece el precio del producto."""
        self.precio = precio
