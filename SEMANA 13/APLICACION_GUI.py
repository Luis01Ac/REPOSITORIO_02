import tkinter as tk
from tkinter import messagebox

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Gestión de Datos")

# Establecer el tamaño de la ventana
ventana.geometry("600x600")

# Cambiar el color de fondo de la ventana a verde claro
ventana.config(bg="lightgreen")  # Se usa "lightgreen" para un color verde claro

# Crear una lista vacía para almacenar los datos (Nombre, Cédula, Edad)
datos = []

# Función para agregar un nuevo dato
def agregar_dato():
    nombre = entrada_nombre.get()
    cedula = entrada_cedula.get()
    edad = entrada_edad.get()

    # Validar que los campos no estén vacíos
    if nombre == "" or cedula == "" or edad == "":
        messagebox.showwarning("Datos Incompletos", "Por favor ingrese todos los datos.")
        return

    # Validar que el número de cédula y la edad sean números
    if not cedula.isdigit() or not edad.isdigit():
        messagebox.showwarning("Datos Inválidos", "La cédula y la edad deben ser números.")
        return

    # Convertir la cédula y la edad a enteros
    cedula = int(cedula)
    edad = int(edad)

    # Agregar el dato en formato estructurado (Nombre, Cédula, Edad)
    datos.append((nombre, cedula, edad))

    # Actualizar la lista visual
    actualizar_lista()

    # Limpiar los campos de texto
    entrada_nombre.delete(0, tk.END)
    entrada_cedula.delete(0, tk.END)
    entrada_edad.delete(0, tk.END)

# Función para actualizar la lista visualmente
def actualizar_lista():
    lista_datos.delete(0, tk.END)  # Limpiar la lista
    for dato in datos:
        # Mostrar cada dato como una cadena con el formato: "Nombre | Cédula | Edad"
        lista_datos.insert(tk.END, f"{dato[0]} | Cédula: {dato[1]} | Edad: {dato[2]}")

# Función para limpiar la lista y los campos de texto
def limpiar():
    datos.clear()  # Limpiar la lista de datos
    actualizar_lista()  # Actualizar la lista visual
    entrada_nombre.delete(0, tk.END)  # Limpiar los campos de texto
    entrada_cedula.delete(0, tk.END)
    entrada_edad.delete(0, tk.END)

# Crear los componentes de la GUI
# Etiqueta para el campo de nombre
etiqueta_nombre = tk.Label(ventana, text="Nombre:", bg="lightgreen")
etiqueta_nombre.pack(pady=5)
entrada_nombre = tk.Entry(ventana, width=30)
entrada_nombre.pack(pady=5)

# Etiqueta para el campo de cédula
etiqueta_cedula = tk.Label(ventana, text="Número de Cédula:", bg="lightgreen")
etiqueta_cedula.pack(pady=5)
entrada_cedula = tk.Entry(ventana, width=30)
entrada_cedula.pack(pady=5)

# Etiqueta para el campo de edad
etiqueta_edad = tk.Label(ventana, text="Edad:", bg="lightgreen")
etiqueta_edad.pack(pady=5)
entrada_edad = tk.Entry(ventana, width=30)
entrada_edad.pack(pady=5)

# Botón "Agregar" que agrega los datos ingresados
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_dato)
boton_agregar.pack(pady=10)

# Botón "Limpiar" que limpia los campos de texto y la lista
boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar)
boton_limpiar.pack(pady=5)

# Lista donde se mostrarán los datos ingresados
lista_datos = tk.Listbox(ventana, width=60, height=10)
lista_datos.pack(pady=20)

# Ejecutar la ventana principal
ventana.mainloop()
