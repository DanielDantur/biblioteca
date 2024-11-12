from tkinter import Tk

class VentanaPrincipal(Tk):
    def __init__(self):
        super().__init__()
        
        ancho_inicial = 1000
        ancho_minimo = 800
        altura_inicial = 750
        altura_minima = 600
        
        self.geometry(f'{ancho_inicial}x{altura_inicial}')
        self.minsize(width=ancho_minimo, height=altura_minima)
        