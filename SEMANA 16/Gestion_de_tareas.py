import tkinter as tk  # Importa la librería Tkinter para crear la interfaz gráfica
from tkinter import messagebox  # Importa el componente messagebox para mostrar alertas

# Función para agregar una nueva tarea
def agregar_tarea():
    tarea = entry_tarea.get()  # Obtiene el texto escrito en el campo de entrada
    if tarea != "":  # Si el campo no está vacío
        lista_tareas.insert(tk.END, tarea)  # Añade la tarea a la lista de tareas (al final)
        entry_tarea.delete(0, tk.END)  # Borra el contenido del campo de entrada
    else:
        # Si el campo está vacío, muestra un mensaje de advertencia
        messagebox.showwarning("Entrada vacía", "Por favor ingrese una tarea.")

# Función para marcar una tarea como completada
def marcar_completada():
    try:
        tarea_seleccionada = lista_tareas.curselection()  # Obtiene el índice de la tarea seleccionada
        if not tarea_seleccionada:  # Si no hay tarea seleccionada
            raise ValueError("No hay tarea seleccionada.")  # Lanza un error para mostrar el mensaje de advertencia

        tarea = lista_tareas.get(tarea_seleccionada)  # Obtiene el texto de la tarea seleccionada
        lista_tareas.delete(tarea_seleccionada)  # Elimina la tarea seleccionada de la lista
        lista_tareas.insert(tk.END, tarea + " - Completada")  # Añade la tarea con el texto "Completada"
    except ValueError as e:
        messagebox.showwarning("No seleccionada", str(e))  # Muestra un mensaje de advertencia si no hay tarea seleccionada
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {e}")  # Muestra un mensaje de error en otros casos

# Función para eliminar una tarea
def eliminar_tarea():
    try:
        tarea_seleccionada = lista_tareas.curselection()  # Obtiene la tarea seleccionada
        lista_tareas.delete(tarea_seleccionada)  # Elimina la tarea seleccionada
    except IndexError:
        # Si no se ha seleccionado ninguna tarea, muestra un mensaje de advertencia
        messagebox.showwarning("No seleccionada", "Por favor seleccione una tarea.")

# Función para cerrar la aplicación cuando se presiona la tecla Escape
def cerrar_aplicacion(_):
    root.quit()  # Termina la ejecución de la aplicación

# Crear la ventana principal de la aplicación
root = tk.Tk()
root.title("Gestión de Tareas")  # Establece el título de la ventana

# Color de fondo de la ventana
root.config(bg="lightblue")  # Establece el color de fondo de la ventana principal

# Crear un campo de entrada para que el usuario pueda escribir nuevas tareas
entry_tarea = tk.Entry(root, width=60)
entry_tarea.grid(row=0, column=0, padx=10, pady=10)  # Ubica el campo en la ventana

# Crear un botón para agregar una tarea
btn_agregar = tk.Button(root, text="Añadir Tarea", command=agregar_tarea)
btn_agregar.grid(row=0, column=1, padx=10, pady=10)  # Ubica el botón en la ventana

# Crear una lista para mostrar las tareas
lista_tareas = tk.Listbox(root, width=50, height=10)
lista_tareas.grid(row=1, column=0, columnspan=2, padx=10, pady=10)  # Ubica la lista en la ventana

# Crear un botón para marcar una tarea como completada
btn_completar = tk.Button(root, text="Marcar como Completada", command=marcar_completada)
btn_completar.grid(row=2, column=0, padx=10, pady=10)  # Ubica el botón en la ventana

# Crear un botón para eliminar una tarea
btn_eliminar = tk.Button(root, text="Eliminar Tarea", command=eliminar_tarea)
btn_eliminar.grid(row=2, column=1, padx=10, pady=10)  # Ubica el botón en la ventana

# Asignar atajos de teclado para las funcionalidades
root.bind("<Return>", lambda event: agregar_tarea())  # Tecla "Enter" para agregar tarea
root.bind("<Tab>", lambda event: marcar_completada())  # Tecla "Tab" para marcar como completada
root.bind("<Delete>", lambda event: eliminar_tarea())  # Tecla "Delete" para eliminar tarea
root.bind("<Escape>", lambda event: cerrar_aplicacion(event))  # Tecla "Escape" para cerrar la aplicación

# Iniciar el bucle principal de la aplicación (mantiene la ventana abierta)
root.mainloop()
