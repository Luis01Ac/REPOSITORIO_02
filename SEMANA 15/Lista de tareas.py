import tkinter as tk
from tkinter import messagebox

# Creamos la ventana principal
root = tk.Tk()
root.title("Lista de Tareas")  # Donde ubicaremos título de la ventana principal
root.geometry("600x500")  # tamaño de la ventana

# Campo de entrada para nuevas tareas
entrada_tarea = tk.Entry(root, width=40)  # Campo de entrada donde el usuario escribe la tarea
entrada_tarea.pack(pady=10)  # campo de entrada con un espacio de 10 píxeles

# Crear el Listbox para mostrar las tareas
lista_tareas = tk.Listbox(root, width=40, height=10, selectmode=tk.SINGLE)  # Listbox para mostrar las tareas
lista_tareas.pack(pady=10)  # Listbox con un espacio de 10 píxeles

# Función para añadir tarea
def añadir_tarea():
    tarea = entrada_tarea.get()  # Obtener el texto escrito en el campo de entrada
    if tarea != "":  # Verificar que la tarea no esté vacía
        lista_tareas.insert(tk.END, tarea)  # Añadir la tarea al final de la lista
        entrada_tarea.delete(0, tk.END)  # Limpiar el campo de entrada después de añadir la tarea
    else:
        messagebox.showwarning("Advertencia", "¡No se puedes añadir una tarea vacía!")  # Mostrar advertencia si la tarea está vacía

# Función para marcar una tarea como completada
def marcar_completada():
    try:
        tarea_index = lista_tareas.curselection()[0]  # Obtener el índice de la tarea seleccionada
        tarea = lista_tareas.get(tarea_index)  # Obtener el texto de la tarea seleccionada
        lista_tareas.delete(tarea_index)  # Eliminar la tarea seleccionada de la lista
        lista_tareas.insert(tk.END, f"{tarea} - Completada")  # Añadir la tarea como completada al final de la lista
    except IndexError:  # Manejar el error si no se ha seleccionado ninguna tarea
        messagebox.showwarning("Advertencia", "¡Selecciona una tarea para marcar como completada!")  # Mostrar advertencia

# Función para eliminar una tarea
def eliminar_tarea():
    try:
        tarea_index = lista_tareas.curselection()[0]  # Obtener el índice de la tarea seleccionada
        lista_tareas.delete(tarea_index)  # Eliminar la tarea seleccionada de la lista
    except IndexError:  # Manejar el error si no se ha seleccionado ninguna tarea
        messagebox.showwarning("Advertencia", "¡Selecciona una tarea para eliminar!")  # Mostrar advertencia

# Crear los botones y asignarles funciones
boton_anadir = tk.Button(root, text="Añadir Tarea", width=20, command=añadir_tarea)  # Botón para añadir tarea
boton_anadir.pack(pady=5)  # Empaquetar el botón con un espacio de 5 píxeles

boton_completar = tk.Button(root, text="Marcar como Completada", width=20, command=marcar_completada)  # Botón para marcar tarea como completada
boton_completar.pack(pady=5)  # Empaquetar el botón con un espacio de 5 píxeles

boton_eliminar = tk.Button(root, text="Eliminar Tarea", width=20, command=eliminar_tarea)  # Botón para eliminar tarea
boton_eliminar.pack(pady=5)  # Empaquetar el botón con un espacio de 5 píxeles

# Método para añadir tarea presionando la tecla Enter
root.bind("<Return>", lambda event: añadir_tarea())  # Vincular la tecla Enter al método añadir_tarea()

# Ejecutar la aplicación
root.mainloop()  # Mantener la ventana abierta y ejecutando la aplicación
