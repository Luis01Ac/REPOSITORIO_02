from inventario import Inventario
from producto import Producto

def mostrar_menu():
    """Muestra el menú de opciones al usuario."""
    print("\nSistema de Gestión de Inventarios")
    print("1. Añadir nuevo producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto(s) por nombre")
    print("5. Mostrar todos los productos")
    print("6. Salir")

def main():
    # Creamos un objeto Inventario
    inventario = Inventario()

    # Añadimos algunos productos predefinidos para inicializar el inventario
    inventario.añadir_producto(Producto(1, "Camiseta", 100, 15.99))
    inventario.añadir_producto(Producto(2, "Pantalón", 50, 25.50))
    inventario.añadir_producto(Producto(3, "Zapatos", 30, 40.00))

    while True:
        # Mostramos el menú
        mostrar_menu()
        opcion = input("Elija una opción: ")

        if opcion == '1':
            try:
                # Pedimos los datos para agregar un nuevo producto
                producto_id = int(input("Ingrese el ID del producto: "))
                nombre = input("Ingrese el nombre del producto: ")
                cantidad = int(input("Ingrese la cantidad del producto: "))
                precio = float(input("Ingrese el precio del producto: "))
                producto = Producto(producto_id, nombre, cantidad, precio)
                inventario.añadir_producto(producto)
            except ValueError:
                print("Error: Por favor ingrese valores válidos.")

        elif opcion == '2':
            try:
                # Pedimos el ID del producto a eliminar
                producto_id = int(input("Ingrese el ID del producto a eliminar: "))
                inventario.eliminar_producto(producto_id)
            except ValueError:
                print("Error: Por favor ingrese un ID válido.")

        elif opcion == '3':
            try:
                # Pedimos el ID del producto a actualizar
                producto_id = int(input("Ingrese el ID del producto a actualizar: "))
                cantidad = input("Ingrese la nueva cantidad del producto (deje vacío si no desea cambiarla): ")
                precio = input("Ingrese el nuevo precio del producto (deje vacío si no desea cambiarlo): ")

                cantidad = int(cantidad) if cantidad else None
                precio = float(precio) if precio else None

                inventario.actualizar_producto(producto_id, cantidad, precio)
            except ValueError:
                print("Error: Por favor ingrese valores válidos.")

        elif opcion == '4':
            nombre = input("Ingrese el nombre del producto a buscar: ")
            productos = inventario.buscar_productos_por_nombre(nombre)
            if productos:
                for producto in productos:
                    print(f"ID: {producto.get_producto_id()}, Nombre: {producto.get_nombre()}, "
                          f"Cantidad: {producto.get_cantidad()}, Precio: {producto.get_precio()}")
            else:
                print("No se encontraron productos con ese nombre.")

        elif opcion == '5':
            # Mostramos todos los productos en el inventario
            inventario.mostrar_productos()

        elif opcion == '6':
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    main()
