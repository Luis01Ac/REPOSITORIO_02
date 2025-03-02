import json

class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio}"

    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    def actualizar_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad

class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        if producto.id not in self.productos:
            self.productos[producto.id] = producto
        else:
            print(f"El producto con ID {producto.id} ya está en el inventario.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
        else:
            print(f"No se encontró el producto con ID {id_producto}.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].actualizar_cantidad(cantidad)
            if precio is not None:
                self.productos[id_producto].actualizar_precio(precio)
        else:
            print(f"Producto con ID {id_producto} no encontrado.")

    def buscar_producto(self, nombre):
        resultado = [producto for producto in self.productos.values() if nombre.lower() in producto.nombre.lower()]
        return resultado

    def mostrar_inventario(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos.values():
                print(producto)

    def guardar_en_archivo(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.productos, file, default=lambda o: o.__dict__, indent=4)

    def cargar_desde_archivo(self, filename):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                for producto_data in data.values():
                    producto = Producto(producto_data['id'], producto_data['nombre'], producto_data['cantidad'], producto_data['precio'])
                    self.productos[producto.id] = producto
        except FileNotFoundError:
            print(f"No se encontró el archivo {filename}. Creando un inventario vacío.")
        except json.JSONDecodeError:
            print("Error al leer el archivo. El formato podría estar dañado.")
