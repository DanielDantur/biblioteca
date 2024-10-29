from abm import ABM

class Libro(ABM):
    __tabla = 'libros'
    
    def __init__(self, titulo, autor, 
                 editorial, categoria, stock):
        self.__titulo = titulo
        self.__autor = autor
        self.__editorial = editorial
        self.__categoria = categoria
        self.__stock = stock
        
    
    @classmethod    
    def todos(cls):
        sql = 'SELECT * FROM ' + cls.__tabla
        cls.conectar()
        resultado = cls.correr_sql(sql)
        cls.desconectar()
        return resultado
        
