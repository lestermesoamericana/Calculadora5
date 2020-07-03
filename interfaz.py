from tkinter import *

class Interfaz():
    
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Calculadora")
        self.ventana.config(width = 300, height = 300)

        # Agregar la pantalla de texto
        # El metodo "Text" se importa de la libreria tkinter
        # El parametro "state" si lo habilitamos como "disabled"
        # no permitira que el usuario escriba los datos que quiera
        # sino solo los datos que nosotros le indiquemos
        self.pantalla = Text(ventana, state = "disabled", width = 30, height = 3,
        background = "orchid", foreground = "white", font = ("Helvetic 15"))

        # Ubicar la pantalla en el frame
        self.pantalla.grid(row = 0, column = 0, columnspan = 4, padx = 5, pady = 5)

        # Inicializar la operacion mostrada en pantalla como vacia
        self.operacion = ""
