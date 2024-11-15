import os
import sys
#ruta para notebook
os_path_PSSE=r'C:\Program Files (x86)\PTI\PSSEXplore34\PSSPY34'
#ruta para pc de escritorio
sys_path_PSSE=r'C:\Program Files (x86)\PTI\PSSEXplore34\PSSPY34'
sys.path.append(sys_path_PSSE)

#ruta para notebook
os_path_PSSE=r'C:\Program Files (x86)\PTI\PSSEXplore34\PSSBIN'
#ruta para pc de escritorio
os_path_PSSE=r'C:\Program Files (x86)\PTI\PSSEXplore34\PSSBIN'
os.environ['PATH'] += '' + os_path_PSSE
os.environ['PATH'] += '' + sys_path_PSSE
 
# Importación de librerias necesarias
#import redirect
import datetime
import re
import tkinter as tk
from tkinter import filedialog, messagebox,Menu
import pssexplore34
import psspy

# Definir las variables globales
destino = None
caso = None
nombre = None

# Definición de las funciones
def ejecutar(destino, caso, nombre):
    print(destino,caso, nombre)
    if destino is None:
        tk.messagebox.showerror("Error", "No se ha seleccionado una carpeta de destino")
        return
    elif caso is None:
        tk.messagebox.showerror("Error", "No se ha seleccionado un caso")
        return
    elif nombre is None:
        tk.messagebox.showerror("Error", "No se ha seleccionado un nombre para el informe")
        return
    tk.messagebox.showinfo("Ejecutando", "El script se está ejecutando")

def seleccionar_destino():
    global destino
    destino = filedialog.askdirectory(title="Seleccionar destino")
    destino_label.config(text="Carpeta seleccionada: "+ destino)

def seleccionar_caso():
    global caso
    caso = filedialog.askopenfilename(title="Seleccionar caso")
    if caso:
        extension = os.path.splitext(caso)[1]
        if extension.lower() in ['.sav']:  # Verificar si la extensión es .txt o .csv
            caso_label.config(text="Caso seleccionado: " + caso)
        else:
            tk.messagebox.showerror("Error", "El archivo seleccionado no tiene una extensión válida (.sav)")
            caso = None

def nombre_informe():
    global nombre
    nombre = nombre.entry.get()
    nombre_label.config(text="Nombre del informe: " + nombre)

def abrir_ventana_secundaria():
    ventana_secundaria = tk.Toplevel(root)
    ventana_secundaria.title("Nombre del informe")
    ventana_secundaria.geometry("400x300")
    tk.Label(ventana_secundaria, text="Escriba el nombre del informe").pack(pady=20)

    nombre_entry_secundaria = tk.Entry(ventana_secundaria)
    nombre_entry_secundaria.pack(pady=10)

    # Crear variables para el estado de los checkboxes
    incluir_hora_var = tk.IntVar()
    incluir_fecha_var = tk.IntVar()
    
    # Crear los checkboxes
    tk.Checkbutton(ventana_secundaria, text="Incluir hora", variable=incluir_hora_var).pack(pady=10)
    tk.Checkbutton(ventana_secundaria, text="Incluir fecha", variable=incluir_fecha_var).pack(pady=10)

    global hora
    global fecha

    # Lógica de los checkboxes
    if incluir_hora_var.get() == 1:
        
        hora = datetime.datetime.now().strftime("%H:%M:%S")
    if incluir_fecha_var.get() == 1:
        
        fecha = datetime.datetime.now().strftime("%d/%m/%Y")

    # Función para guardar el nombre del informe y cerrar la ventana secundaria
    def guardar_y_cerrar():
        global nombre
        nombre = nombre_entry_secundaria.get()
        
        hora = ""
        fecha = ""

        # Lógica de los checkboxes
        if incluir_hora_var.get() == 1:
            hora = "_" + datetime.datetime.now().strftime("%H%M%S")
        if incluir_fecha_var.get() == 1:
            fecha = "_" + datetime.datetime.now().strftime("%d-%m-%Y")
        nombre_label.config(text="Nombre del informe: " + nombre+hora+fecha+".xlsx")
        ventana_secundaria.destroy()

    tk.Button(ventana_secundaria, text="Guardar", command=guardar_y_cerrar).pack(pady=10)
    

def quit_app():
    root.quit()

# Creacion de la ventana principal
root = tk.Tk()
root.title("Calculo de reserva")
root.geometry("800x600")

# Creación de la barra de menú
menu_bar = tk.Menu(root)

# Crear un menú desplegable "Archivo"
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Seleccionar destino", command=seleccionar_destino)
file_menu.add_command(label="Seleccionar caso", command=seleccionar_caso)
file_menu.add_command(label="Nombre informe", command=abrir_ventana_secundaria)
file_menu.add_separator()
file_menu.add_command(label="Salir", command=quit_app)
menu_bar.add_cascade(label="Menú", menu=file_menu)

# Crear un menú desplegable "Ayuda"
help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Ayuda", menu=help_menu)

# Configurar la barra de menú en la ventana principal
root.config(menu=menu_bar)

# Crear un Label para mostrar el destino seleccionado
destino_label = tk.Label(root, text="Selecciona una carpeta para guardar el informe", font=("Arial", 14))
destino_label.pack(pady=20)

# Crear un label para mostrar el caso seleccionado
caso_label = tk.Label(root, text="Selecciona un caso para realizar el análisis", font=("Arial", 14))
caso_label.pack(pady=20)

# Crear un label para mostrar el nombre del informe
nombre_label = tk.Label(root, text="Sin nombre seleccionado", font=("Arial", 14))
nombre_label.pack(pady=20)

# Crear un boton para ejecutar el script principal
run_button = tk.Button(root, text="Ejecutar", font=("Arial", 14), command=lambda: ejecutar(destino, caso, nombre))
run_button.pack(pady=20)

# Inicio del bucle principal
root.mainloop()