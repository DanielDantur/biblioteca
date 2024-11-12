from .abm import ABM

class Libro(ABM):
    _tabla = 'libros'
    
    def __init__(self, titulo, autor, editorial, categoria, stock):
        self.__titulo = titulo
        self.__autor = autor
        self.__editorial = editorial
        self.__categoria = categoria
        self.__stock = stock
        
    
        
