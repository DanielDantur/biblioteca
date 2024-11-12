from modelos.libro import Libro

class LibroControlador:
    
    def libros(self):
        return Libro.todos()