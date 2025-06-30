import mysql.connector
from mysql.connector import Error

class ConexionBD:
    def __init__(self):
        self.host = "localhost"
        self.user = "root"
        self.password = ""
        self.database = "desviacion"
        self.connection = None

    def conectar(self):
        """Establece la conexion a base de datos"""
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.connection.is_connected():
                return self.connection
        except Error as e:
            print(f"Error en la conexión a la base de datos: {e}")
            return None

    def cerrar(self):
        """Cierra la conexión con la base de datos"""
        if self.connection.is_connected():
            self.connection.close()

    def obtener_cursor(self):
        """Devuelve un cursor para ejecutar consultas"""
        if self.connection is None:
            return None
        return self.connection.cursor()
