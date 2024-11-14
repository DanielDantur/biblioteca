from modelos.libro import Libro

class LibroControlador:
    
    def libros(self):
        return Libro.todos()
    
    def buscar_libro(self, busqueda):
        return Libro.buscar(busqueda)
    
    def agregar_libro(self):
        return Libro.agregar()
    
    def eliminar_libro(self):
        return Libro.eliminar()
    
    def modificar_libro(self):
        return Libro.modificar()