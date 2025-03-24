import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import Calendar
class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal") # Título de la ventana
        self.root.geometry("700x600") # Tamaño de la ventana principal

        # Lista de eventos
        self.eventos = [] # Lista para almacenar los eventos

        # Creacion de los contenedores
        self.create_widgets()

    def create_widgets(self):
        # Frame para los eventos
        self.frame_lista = tk.Frame(self.root)
        self.frame_lista.pack(pady=10)

        # Treeview para mostrar eventos
        self.tree = ttk.Treeview(self.frame_lista, columns=("Fecha", "Hora", "Descripción"), show="headings")
        self.tree.heading("Fecha", text="Fecha")  # Título de la columna de Fecha
        self.tree.heading("Hora", text="Hora")  # Título de la columna de Hora
        self.tree.heading("Descripción", text="Descripción") # Título de la columna de Descripción
        self.tree.pack()

        # Frame para los campos de entrada
        self.frame_entrada = tk.Frame(self.root)
        self.frame_entrada.pack(pady=10)

        # Etiquetas y campos de entrada
        self.etiqueta_fecha = tk.Label(self.frame_entrada, text="Fecha:")
        self.etiqueta_fecha.grid(row=0, column=0)
        self.fecha_entrada = Calendar(self.frame_entrada, selectmode='day')
        self.fecha_entrada.grid(row=0, column=1)

        self.etiqueta_hora = tk.Label(self.frame_entrada, text="Hora:")
        self.etiqueta_hora.grid(row=1, column=0)
        self.hora_entrada = tk.Entry(self.frame_entrada)
        self.hora_entrada.grid(row=1, column=1)

        self.etiqueta_desc = tk.Label(self.frame_entrada, text="Descripción:")
        self.etiqueta_desc.grid(row=2, column=0)
        self.desc_entrada = tk.Entry(self.frame_entrada)
        self.desc_entrada.grid(row=2, column=1)

        # Frame para los botones
        self.frame_botones = tk.Frame(self.root)
        self.frame_botones.pack(pady=10)

        self.boton_agregar = tk.Button(self.frame_botones, text="Agregar Evento", command=self.agregar_evento)
        self.boton_agregar.pack(side=tk.LEFT, padx=10)

        self.boton_eliminar = tk.Button(self.frame_botones, text="Eliminar Evento Seleccionado", command=self.eliminar_evento)
        self.boton_eliminar.pack(side=tk.LEFT, padx=10)

        self.boton_salir = tk.Button(self.frame_botones, text="Salir", command=self.root.quit)
        self.boton_salir.pack(side=tk.LEFT, padx=10)

    def agregar_evento(self):
        # Obtener los datos introducidos
        fecha = self.fecha_entrada.get_date()
        hora = self.hora_entrada.get()
        descripcion = self.desc_entrada.get()

        if not fecha or not hora or not descripcion:
            messagebox.showerror("Error", "Por favor, complete todos los campos.")
            return

        # Añadir el evento a la lista y al Treeview
        evento = (fecha, hora, descripcion)
        self.eventos.append(evento)
        self.tree.insert("", "end", values=evento)

        # Limpiar los campos
        self.fecha_entrada.set_date('')
        self.hora_entrada.delete(0, tk.END)
        self.desc_entrada.delete(0, tk.END)

    def eliminar_evento(self):
        # Obtener el evento seleccionado
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Por favor, seleccione un evento para eliminar.")
            return

        # Confirmar la eliminación
        confirm = messagebox.askyesno("Confirmación", "¿Está seguro de que desea eliminar este evento?")
        if confirm:
            self.tree.delete(selected_item)
            # También eliminarlo de la lista de eventos
            self.eventos = [evento for evento in self.eventos if evento != self.tree.item(selected_item)["values"]]
def main():
    root = tk.Tk() # Crear la ventana principal
    app = AgendaApp(root) # Crear la instancia de la clase AgendaApp
    root.mainloop()  # Iniciar el bucle principal de la interfaz gráfica

if __name__ == "__main__":
    main()
