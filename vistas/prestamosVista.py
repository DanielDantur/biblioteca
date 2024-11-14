from tkinter import Frame
from tkinter import ttk

class PrestamosVista(Frame):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        
        labelPrestamos = ttk.Label(master=self, text='Préstamos')
        labelPrestamos.grid(row=0, column=0, sticky='w')