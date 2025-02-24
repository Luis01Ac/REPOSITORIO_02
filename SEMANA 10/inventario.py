import os
from producto import Producto


class Inventario:
    def __init__(self, archivo="inventario.txt"):
        """Inicializa el inventario, cargando los productos desde el archivo si existe."""
        self.productos = []
        self.archivo = archivo
        self.cargar_inventario()

    def cargar_inventario(self):
        """Carga los productos desde el archivo de texto."""
        try:
            if os.path.exists(self.archivo):
                with open(self.archivo, "r") as file:
                    for line in file:
                        datos = line.strip().split(",")
                        producto_id, nombre, cantidad, precio = datos
                        producto = Producto(producto_id, nombre, int(cantidad), float(precio))
                        self.productos.append(producto)
                print("Inventario cargado desde el archivo.")
            else:
                print("El archivo no existe. Se creará uno nuevo.")
        except (FileNotFoundError, PermissionError) as e:
            print(f"Error al cargar el archivo: {e}")

    def guardar_inventario(self):
        """Guarda el inventario en el archivo de texto."""
        try:
            with open(self.archivo, "w") as file:
                for producto in self.productos:
                    file.write(f"{producto.get_producto_id()},{producto.get_nombre()},{producto.get_cantidad()},{producto.get_precio()}\n")
            print("Inventario guardado exitosamente.")
        except (FileNotFoundError, PermissionError) as e:
            print(f"Error al guardar el archivo: {e}")

    def añadir_producto(self, producto):
        """Añade un nuevo producto al inventario y guarda el archivo."""
        if self.buscar_producto_por_id(producto.get_producto_id()) is not None:
            print("Error: El ID del producto ya existe.")
        else:
            self.productos.append(producto)
            self.guardar_inventario()  # Guardamos los cambios en el archivo
            print(f"Producto {producto.get_nombre()} añadido exitosamente.")

    def eliminar_producto(self, producto_id):
        """Elimina un producto del inventario por su ID y guarda el archivo."""
        producto = self.buscar_producto_por_id(producto_id)
        if producto:
            self.productos.remove(producto)
            self.guardar_inventario()  # Guardamos los cambios en el archivo
            print(f"Producto con ID {producto_id} eliminado.")
        else:
            print("Error: Producto no encontrado.")

    def actualizar_producto(self, producto_id, cantidad=None, precio=None):
        """Actualiza la cantidad o el precio de un producto y guarda el archivo."""
        producto = self.buscar_producto_por_id(producto_id)
        if producto:
            if cantidad is not None:
                producto.set_cantidad(cantidad)
            if precio is not None:
                producto.set_precio(precio)
            self.guardar_inventario()  # Guardamos los cambios en el archivo
            print(f"Producto con ID {producto_id} actualizado.")
        else:
            print("Error: Producto no encontrado.")

    def buscar_producto_por_id(self, producto_id):
        """Busca un producto por su ID."""
        for producto in self.productos:
            if producto.get_producto_id() == producto_id:
                return producto
        return None

    def mostrar_productos(self):
        """Muestra todos los productos en el inventario."""
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos:
                print(f"ID: {producto.get_producto_id()}, Nombre: {producto.get_nombre()}, "
                      f"Cantidad: {producto.get_cantidad()}, Precio: {producto.get_precio()}")