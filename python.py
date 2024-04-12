import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import simpledialog

# Función para abrir un archivo
def abrir_archivo():
    archivo = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")])
    if archivo:
        with open(archivo, "r") as file:
            contenido.delete(1.0, tk.END)
            contenido.insert(tk.END, file.read())

# Función para guardar el archivo actual
def guardar_archivo():
    archivo = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")])
    if archivo:
        with open(archivo, "w") as file:
            file.write(contenido.get(1.0, tk.END))

# Función para cortar texto
def cortar():
    contenido.event_generate("<<Cut>>")

# Función para copiar texto
def copiar():
    contenido.event_generate("<<Copy>>")

# Función para pegar texto
def pegar():
    contenido.event_generate("<<Paste>>")

# Función para deshacer
def deshacer():
    contenido.event_generate("<<Undo>>")

# Función para rehacer
def rehacer():
    contenido.event_generate("<<Redo>>")

# Función para contar palabras en el texto
def contar_palabras():
    texto = contenido.get(1.0, tk.END)
    palabras = texto.split()
    messagebox.showinfo("Conteo de Palabras", f"Total de palabras: {len(palabras)}")

# Función para buscar y reemplazar texto
def buscar_reemplazar():
    buscar = simpledialog.askstring("Buscar y Reemplazar", "Buscar:")
    if buscar:
        reemplazar = simpledialog.askstring("Buscar y Reemplazar", f"Reemplazar '{buscar}' con:")
        if reemplazar:
            texto = contenido.get(1.0, tk.END)
            texto_modificado = texto.replace(buscar, reemplazar)
            contenido.delete(1.0, tk.END)
            contenido.insert(tk.END, texto_modificado)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Bloc de Notas")

# Crear un área de texto para el contenido
contenido = tk.Text(ventana)
contenido.pack(expand="true", fill="both")

# Crear un menú
menu = tk.Menu(ventana)
ventana.config(menu=menu)

# Agregar opciones al menú "Archivo"
archivo_menu = tk.Menu(menu)
menu.add_cascade(label="Archivo", menu=archivo_menu)
archivo_menu.add_command(label="Abrir", command=abrir_archivo)
archivo_menu.add_command(label="Guardar", command=guardar_archivo)
archivo_menu.add_separator()
archivo_menu.add_command(label="Salir", command=ventana.quit)

# Agregar opciones al menú "Edición"
edicion_menu = tk.Menu(menu)
menu.add_cascade(label="Edición", menu=edicion_menu)
edicion_menu.add_command(label="Cortar", command=cortar)
edicion_menu.add_command(label="Copiar", command=copiar)
edicion_menu.add_command(label="Pegar", command=pegar)
edicion_menu.add_separator()
edicion_menu.add_command(label="Deshacer", command=deshacer)
edicion_menu.add_command(label="Rehacer", command=rehacer)
edicion_menu.add_separator()
edicion_menu.add_command(label="Contar Palabras", command=contar_palabras)
edicion_menu.add_command(label="Buscar y Reemplazar", command=buscar_reemplazar)

# Ejecutar la aplicación
ventana.mainloop()
