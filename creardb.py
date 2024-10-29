import sqlite3

conexion = sqlite3.connect('biblioteca.db')
cursor = conexion.cursor()

cursor.execute(
    '''CREATE TABLE IF NOT EXISTS libros (
        id INTEGER PRIMARY KEY,
        titulo TEXT NOT NULL,
        autor TEXT NOT NULL,
        editorial TEXT NOT NULL,
        categoria TEXT NOT NULL,
        stock INTEGER DEFAULT 1
        );'''
)

conexion.commit()
conexion.close()