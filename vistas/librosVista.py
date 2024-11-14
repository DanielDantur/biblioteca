from tkinter import ttk, Frame
from tkinter import *

from controladores.libroControlador import LibroControlador

class LibrosVista(Frame):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.controlador = LibroControlador()
        
        labelLibros = ttk.Label(master=self, text='Libros')
        labelLibros.grid(row=0, column=0, sticky='w')
        
        self.busqueda = StringVar()
        ttk.Label(master=self, text='Búsqueda').grid(row=1, column=0, sticky='w')
        self.busqueda = ttk.Entry(master=self, width=20, textvariable=self.busqueda)
        self.busqueda.grid(row=1, column=1, sticky='we')
        
        ttk.Button(master=self, text='Buscar', command=self.buscar).grid(row=1, column=2, sticky='we')
        
        ttk.Button(master=self, text='Agregar', command=self.agregar).grid(row=2, column=0, sticky='we')
        ttk.Button(master=self, text='Borrar', command=self.borrar).grid(row=2, column=1, sticky='we')
        ttk.Button(master=self, text='Modificar', command=self.modificar).grid(row=2, column=2, sticky='we')
        
        columnas = ('titulo', 'autor', 'editorial', 'categoria', 'stock')
        self.lista_de_libros = ttk.Treeview(master=self, columns=columnas, show='headings')
        self.lista_de_libros.heading(column='titulo', text='Título')
        self.lista_de_libros.heading(column='autor', text='Autor')
        self.lista_de_libros.heading(column='editorial', text='Editorial')
        self.lista_de_libros.heading(column='categoria', text='Categoría')
        self.lista_de_libros.heading(column='stock', text='Stock')
        self.lista_de_libros.grid(row=3, column=0, columnspan=3, sticky='we')
        self.refrescar()
        
    
    def llenar_lista(self, libros):
        self.lista_de_libros.delete(*self.lista_de_libros.get_children())
        if libros != None:
            for libro in libros:
                self.lista_de_libros.insert('',index='end', id=libro[0], values=libro[1:])
                
    def refrescar(self):
        libros = self.controlador.libros()
        self.llenar_lista(libros)
    
    def buscar(self):
        libros = self.controlador.buscar_libro(self.busqueda.get())
        self.llenar_lista(libros)
            
    def agregar(self):
        self.controlador.agregar_libro()
        self.llenar_lista()
        
    def borrar(self):
        self.controlador.eliminar_libro()
        self.llenar_lista()
        
    def modificar(self):
        self.controlador.modificar_libro()
        self.llenar_lista()
        
    