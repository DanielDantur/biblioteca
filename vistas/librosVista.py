from tkinter import Frame
from tkinter import ttk

class LibrosVista(Frame):
    def __init__(self, padre, controlador,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.controlador = controlador
        
        columnas = ('titulo', 'autor', 'editorial', 'categoria', 'stock')
        self.lista_de_libros = ttk.Treeview(padre, columns=columnas, show='headings')
        self.lista_de_libros.heading('titulo', text='Título')
        self.lista_de_libros.heading('autor', text='Autor')
        self.lista_de_libros.heading('editorial', text='Editorial')
        self.lista_de_libros.heading('categoria', text='Categoría')
        self.lista_de_libros.heading('stock', text='Stock')
        self.lista_de_libros.pack()
        self.llenar_lista()
        
    
    def llenar_lista(self):
        libros = self.controlador.libros()
        for libro in libros:
            self.lista_de_libros.insert('','end', libro[0],values=libro[1:])
                