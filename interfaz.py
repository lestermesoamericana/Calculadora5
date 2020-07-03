from tkinter import *

class Interfaz():
    
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Calculadora")
        #self.ventana.config(width = 300, height = 300)

        # Agregar la pantalla de texto
        # El metodo "Text" se importa de la libreria tkinter
        # El parametro "state" si lo habilitamos como "disabled"
        # no permitira que el usuario escriba los datos que quiera
        # sino solo los datos que nosotros le indiquemos
        self.pantalla = Text(self.ventana, state = "disabled", width = 15, height = 1,
        background = "orchid", foreground = "white", font = ("Helvetic 15"))

        # Ubicar la pantalla en el frame
        self.pantalla.grid(row = 0, column = 0, columnspan = 4, padx = 5, pady = 5)

        # Inicializar la operacion mostrada en pantalla como vacia
        self.operacion = ""

        # Creacion de los botones
        boton1  = self.crearboton(7)
        boton2  = self.crearboton(8)
        boton3  = self.crearboton(9)
        boton4  = self.crearboton(u"\u232B", escribir = False)
        boton5  = self.crearboton(4)
        boton6  = self.crearboton(5)
        boton7  = self.crearboton(6)
        boton8  = self.crearboton(u"\u00F7")
        boton9  = self.crearboton(1)
        boton10 = self.crearboton(2)
        boton11 = self.crearboton(3)
        boton12 = self.crearboton("*")
        boton13 = self.crearboton(".")
        boton14 = self.crearboton(0) 
        boton15 = self.crearboton("+") 
        boton16 = self.crearboton("-") 
        boton17 = self.crearboton("=", escribir = False, ancho = 20, alto = 2)

        # Ubicar los botones con el boton grid
        # lista
        botones = [boton1, boton2, boton3, boton4, boton5,
                    boton6, boton7, boton8, boton9, boton10,
                    boton11, boton12, boton13, boton14, boton15,
                    boton16, boton17]
        contador = 0

        for fila in range(6,10):
            for columna in range(4):
                botones[contador].grid(row = fila, column = columna)
                contador+=1
                
        # ubicar el boton igual
        botones[16].grid(row = 12, column = 0, columnspan = 4)

        # No es necesario pero sirve para la legibilidad
        return
    
    # Funcion para que funcionen los botones
    def crearboton(self, valor, escribir = True, ancho = 9, alto = 1):
        return Button(self.pantalla, text = valor, width = ancho, height = alto, 
            font = ("Helvetic", 15), command = lambda : self.click(valor,escribir))
    # 
    # Condiciones de los botones

    def click(self, texto, escribir):
        # Si el parametro escribir es "True", entonces el parametro "texto"
        # debe de mostrarse en pantalla. Si es "False" entonces no
        if not escribir:
            if texto == "=" and self.operacion != "":
                # Reemplazar el valor unicode de la division por el de python
                # "RE" es un modulo para expresiones regulares o "regex"
                # que es una secuencia de caracteres que muestra un patron
                # de busqueda y con el metodo "sub" sustuimos
                # nueva variable llamada resultado
                self.operacion = re.sub("\u00F7", "/", self.operacion)
                resultado = str(eval(self.operacion))
                self.operacion = ""
                self.limpiarPantalla()
                self.mostrarenPantalla(resultado)
            # Si se presiono el boton de borrado, limpiar la pantalla
            elif texto == "\u00F7":
                self.operacion = ""
                self.limpiarPantalla()
            # Mostrar texto
        else:
            self.operacion += str(texto)
            self.mostrarenPantalla(texto)
        return

    # borra el contenido de la pantalla
    def limpiarPantalla(self):
        # para poder usar el delete, debemos de
        # habilitar la pantalla (ya que le habiamos)
        # quitado esa posibilidad. Luego de ello la
        # deshabilitamos
        self.pantalla.configure(state = "normal")
        # utiliza indices de texto, "1" significa fila
        # y "0" significa columna
        self.pantalla.delete("1.0", END)
        self.pantalla.configure(state = "disabled")
    
    # muestra en la pantalla de la calculadora el contenido de las
    # operaciones y los resultados
    def mostrarenPantalla(self, valor):
        self.pantalla.configure(state = "normal")
        self.pantalla.insert(END, valor)
        self.pantalla.configure(state = "disabled")

