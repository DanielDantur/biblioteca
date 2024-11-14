from tkinter import Frame
from tkinter import ttk

class SociosVista(Frame):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        
        labelSocios = ttk.Label(master=self, text='Socios')
        labelSocios.grid(row=0, column=0, sticky='w')