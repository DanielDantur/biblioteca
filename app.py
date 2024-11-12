from vistas.ventana import VentanaPrincipal
from vistas.librosVista import LibrosVista
from controladores.librosControlador import LibroControlador

def main():
    ventana = VentanaPrincipal()
    libros_vista = LibrosVista(ventana, LibroControlador())
    libros_vista.pack()
    ventana.mainloop()

if __name__ == '__main__':
    print('Bienvenido al sistema de biblioteca')
    main()