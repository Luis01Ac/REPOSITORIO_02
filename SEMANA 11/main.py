from inventario import Producto, Inventario


def menu():
    inventario = Inventario()

    # Agregamos algunos productos ficticios al inventario
    inventario.agregar_producto(Producto("001", "Teléfono iPhone 14", 50, 999.99))
    inventario.agregar_producto(Producto("002", "Laptop Dell XPS 13", 30, 1299.99))
    inventario.agregar_producto(Producto("003", "Audífonos Sony WH-1000XM4", 100, 349.99))
    inventario.agregar_producto(Producto("004", "Smartwatch Samsung Galaxy Watch 5", 75, 279.99))
    inventario.agregar_producto(Producto("005", "Tablet Apple iPad Pro", 20, 799.99))

    while True:
        print("\n--- Sistema de Gestión de Inventario - Tienda ElectroPlus ---")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar inventario")
        print("6. Guardar inventario")
        print("7. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            id_producto = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad disponible: "))
            precio = float(input("Precio del producto: $"))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        elif opcion == '2':
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == '3':
            id_producto = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar en blanco si no se desea cambiar): ")
            precio = input("Nuevo precio (dejar en blanco si no se desea cambiar): ")

            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id_producto, cantidad, precio)

        elif opcion == '4':
            nombre = input("Nombre del producto a buscar: ")
            productos_encontrados = inventario.buscar_producto(nombre)
            if productos_encontrados:
                for p in productos_encontrados:
                    print(p)
            else:
                print("No se encontraron productos con ese nombre.")

        elif opcion == '5':
            inventario.mostrar_inventario()

        elif opcion == '6':
            inventario.guardar_en_archivo('inventario_electroplus.json')
            print("Inventario guardado con éxito.")

        elif opcion == '7':
            print("Saliendo del sistema...")
            inventario.guardar_en_archivo('inventario_electroplus.json')  # Guardar al salir
            break

        else:
            print("Opción no válida. Por favor selecciona una opción válida.")


# Ejecutar el programa
if __name__ == '__main__':
    menu()
