from .abm import ABM

class Libro(ABM):
    _tabla = 'libros'
    
    def __init__(self, titulo, autor, editorial, categoria, stock):
        self.__titulo = titulo
        self.__autor = autor
        self.__editorial = editorial
        self.__categoria = categoria
        self.__stock = stock
        
    
    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def autor(self):
        return self.__autor
    
    @property
    def editorial(self):
        return self.__editorial
    
    @property
    def categoria(self):
        return self.__categoria
    
    @property
    def stock(self):
        return self.__stock
    
    def disponibles(self):
        return self.__stock
    
    def prestados(self):
        pass
    
    def agregar_ejemplar(self):
        self.__stock += 1    
        
    def eliminar_ejemplar(self):
        self.__stock -= 1
    
    @classmethod
    def buscar(cls, busqueda):
        sql = 'SELECT * FROM libros WHERE titulo LIKE ? OR autor LIKE ? OR editorial LIKE ? OR categoria LIKE ?'
        cls.conectar()
        libros = cls.correr_sql(sql, (f'%{busqueda}%', f'%{busqueda}%', f'%{busqueda}%', f'%{busqueda}%'))
        cls.desconectar()
        return libros
        
    def modificar_libro(self):
        pass        
        
    def eliminar_libro(self):
        pass
        
    def agregar_libro(self):
        pass
    
