# Clase Producto: Representa un producto de la tienda
class Producto:
    def __init__(self, nombre, precio, stock):
        """
        Inicializa el producto con nombre, precio y cantidad en stock.
        """
        self.nombre = nombre  # Nombre del producto
        self.precio = precio  # Precio del producto
        self.stock = stock  # Cantidad de productos disponibles en stock

    def reducir_stock(self, cantidad):
        """
        Reduce el stock del producto cuando se realiza una compra.
        """
        if cantidad <= self.stock:
            self.stock -= cantidad
            return True
        else:
            print(f"No hay suficiente stock para {self.nombre}. Solo quedan {self.stock} unidades.")
            return False

    def __str__(self):
        """
        Representación en cadena del producto.
        """
        return f"{self.nombre} - ${self.precio} (Stock: {self.stock})"


# Clase Carrito: Representa el carrito de compras de un cliente
class Carrito:
    def __init__(self):
        """
        Inicializa un carrito vacío.
        """
        self.items = []  # Lista que contiene los productos en el carrito

    def agregar_producto(self, producto, cantidad):
        """
        Agrega un producto al carrito si hay suficiente stock.
        """
        if producto.reducir_stock(cantidad):
            self.items.append({"producto": producto, "cantidad": cantidad})
            print(f"{cantidad} x {producto.nombre} han sido agregados al carrito.")

    def total_carrito(self):
        """
        Calcula el precio total de los productos en el carrito.
        """
        total = 0
        for item in self.items:
            total += item["producto"].precio * item["cantidad"]
        return total

    def mostrar_contenido(self):
        """
        Muestra todos los productos en el carrito.
        """
        if self.items:
            print("Contenido del carrito:")
            for item in self.items:
                print(f"{item['cantidad']} x {item['producto'].nombre} - ${item['producto'].precio} cada uno")
            print(f"Total: ${self.total_carrito()}")
        else:
            print("El carrito está vacío.")


# Clase Cliente: Representa un cliente de la tienda
class Cliente:
    def __init__(self, nombre, direccion):
        """
        Inicializa un cliente con nombre y dirección.
        """
        self.nombre = nombre
        self.direccion = direccion
        self.carrito = Carrito()  # Cada cliente tiene su propio carrito

    def realizar_compra(self):
        """
        Realiza la compra, mostrando el total y vaciando el carrito.
        """
        if self.carrito.items:
            print(f"{self.nombre} ha realizado una compra. El total es: ${self.carrito.total_carrito()}")
            self.carrito.items.clear()  # Vaciar el carrito después de la compra
        else:
            print("El carrito está vacío. No se puede realizar la compra.")

    def agregar_producto_al_carrito(self, producto, cantidad):
        """
        Agrega un producto al carrito de compras del cliente.
        """
        self.carrito.agregar_producto(producto, cantidad)

    def mostrar_carrito(self):
        """
        Muestra el contenido actual del carrito del cliente.
        """
        self.carrito.mostrar_contenido()


# Clase Tienda: Representa la tienda online
class Tienda:
    def __init__(self, nombre):
        """
        Inicializa la tienda con un nombre y una lista de productos disponibles.
        """
        self.nombre = nombre
        self.productos = []  # Lista de productos disponibles en la tienda

    def agregar_producto(self, producto):
        """
        Agrega un nuevo producto a la tienda.
        """
        self.productos.append(producto)

    def mostrar_productos(self):
        """
        Muestra todos los productos disponibles en la tienda.
        """
        if self.productos:
            print(f"Productos disponibles en {self.nombre}:")
            for producto in self.productos:
                print(producto)
        else:
            print(f"No hay productos disponibles en {self.nombre}.")


# Ejemplo de uso del sistema de tienda online
if __name__ == "__main__":
    # Crear productos
    producto1 = Producto("Laptop", 1500, 8)
    producto2 = Producto("Smartphone", 250, 12)
    producto3 = Producto("Auriculares", 22, 20)

    # Nuevo producto agregado
    producto4 = Producto("Tablet", 350, 15)

    # Creamos una tienda y agregar productos
    tienda = Tienda("HousePC")
    tienda.agregar_producto(producto1)
    tienda.agregar_producto(producto2)
    tienda.agregar_producto(producto3)
    tienda.agregar_producto(producto4)   # Agregar el nuevo producto "Tablet"

    # Muestra productos disponibles en la tienda
    tienda.mostrar_productos()

    # Crear un cliente
    cliente1 = Cliente("Luis Achachi", "Ambato")

    # El cliente agrega productos al carrito
    cliente1.agregar_producto_al_carrito(producto1, 1)  # Agregar 2 laptops
    cliente1.agregar_producto_al_carrito(producto2, 1)  # Agregar 1 smartphone
    cliente1.agregar_producto_al_carrito(producto3, 3)  # Agregar 5 auriculares

    # Mostrar el carrito del cliente
    cliente1.mostrar_carrito()

    # El cliente realiza la compra
    cliente1.realizar_compra()

    # Mostrar el estado del carrito después de la compra
    cliente1.mostrar_carrito()

    # Intentar agregar más productos de los que hay en stock
    cliente1.agregar_producto_al_carrito(producto2, 25)  # Intentar agregar 25 smartphones (solo hay 20)
