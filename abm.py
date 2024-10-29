import sqlite3

class ABM:
    __db = 'biblioteca.db'
    __tabla = None
    __conexion = None
    
    @classmethod    
    def conectar(cls):
        try:
            cls.__conexion = sqlite3.connect(cls.__db)
        except sqlite3.Error as e:
            print(f'Error al conectar: {e}')
    @classmethod        
    def desconectar(cls):
        if cls.__conexion:
            cls.__conexion.close()
    
    @classmethod        
    def correr_sql(cls, sql, parametros=None):
        if cls.__conexion:
            try:
                cursor = cls.__conexion.cursor()
                if parametros:
                    cursor.execute(sql, parametros)
                else:
                    cursor.execute(sql)
                cls.__conexion.commit()
                return cursor.fetchall()
            except sqlite3.Error as e:
                print(f'Error en la consulta: {e}')
        else:
            print('No hay conexión con la db.')