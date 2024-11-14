from tkinter import Tk
from tkinter import *

from vistas.librosVista import LibrosVista
from vistas.prestamosVista import PrestamosVista
from vistas.sociosVista import SociosVista
 
class VentanaPrincipal(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        ancho_inicial = 1000
        ancho_minimo = 800
        altura_inicial = 750
        altura_minima = 600
        
        self.geometry(f'{ancho_inicial}x{altura_inicial}')
        self.minsize(width=ancho_minimo, height=altura_minima)
        
        self.option_add('*padx', 50)
        self.option_add('*pady', 50)
        
        self.title('Biblioteca')
        
        # self.option_add('tearOff', FALSE)
        
        menubar = Menu(self)
        self['menu'] = menubar
        menubar.add_command(label='Libros', underline=0, command=lambda:librosVista.tkraise())
        menubar.add_command(label='Préstamos', underline=0, command=lambda:prestamosVista.tkraise())
        menubar.add_command(label='Socios', underline=0, command=lambda:sociosVista.tkraise())
        menubar.add_separator()
        menubar.add_command(label='Salir', underline=4, command=lambda:self.destroy())
        
        librosVista = LibrosVista(master=self)
        prestamosVista = PrestamosVista(master=self)
        sociosVista = SociosVista(master=self)
        
        librosVista.grid(row=0, column=0, sticky='nsew')
        prestamosVista.grid(row=0, column=0, sticky='nsew')
        sociosVista.grid(row=0, column=0, sticky='nsew')
        
        librosVista.tkraise()