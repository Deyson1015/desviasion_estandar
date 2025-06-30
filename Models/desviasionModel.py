from datetime import date
from Database.conexion import ConexionBD
import numpy as np


class ModeloDesviacion:
    def __init__(self, datos=None):
        self.datos = datos if datos else []
        self.db = ConexionBD()  # Creamos una instancia de ConexionBD

    def calcular_manual(self):
        # Calcular desviación estándar manualmente
        media = sum(self.datos) / len(self.datos)
        diferencias_cuadradas = [(x - media) ** 2 for x in self.datos]
        varianza = sum(diferencias_cuadradas) / len(self.datos)
        return media, varianza ** 0.5

    def calcular_numpy(self):
        media = np.mean(self.datos)
        desviacion = np.std(self.datos)
        return media, desviacion

    def guardar(self, media, resultado):
        try:  
            # Establecer la conexión a la base de datos
            conexion = self.db.conectar()
            if conexion:
                cursor = conexion.cursor()

                # Guardar los datos en la tabla 'registros'
                sql = "INSERT INTO registros (datos, resultado) VALUES (%s, %s)"
                valores = (float(media), float(resultado))
                cursor.execute(sql, valores)
                conexion.commit()
                cursor.close()
                self.db.cerrar()  # Cerramos la conexión
        except Exception as e:
            print(f"Error al guardar en la base de datos: {e}")
 
    def obtener_datos(self):
        try:
            conexion = self.db.conectar()
            if conexion:
                cursor = conexion.cursor()
                sql = " SELECT * FROM registros "
                cursor.execute(sql)
                resultados = cursor.fetchall()
                cursor.close()
                self.db.cerrar()
                return resultados
        except Exception as e:
            print(f"Error al obtener los datos completos: {e}")
            return []
        
    def obtener_ultimo(self):
        try:
            conexion = self.db.conectar()
            if conexion:
                cursor = conexion.cursor()
                sql = "SELECT * FROM registros ORDER BY id DESC LIMIT 1"
                cursor.execute(sql)
                resultado = cursor.fetchall()
                cursor.close()
                self.db.cerrar()
                return resultado
        except Exception as e:
            print(f"Error al obtener el ultimo dato: {e}")
            return []
        



    def eliminar_registro(self, id_registro):
        try:
            # Establecer la conexión a la base de datos
            id_registro = int(id_registro)
            conexion = self.db.conectar()
            if conexion:
                cursor = conexion.cursor()
                # Ahora eliminar el registro de la tabla 'registros'
                sql = "DELETE FROM registros WHERE id = %s"
                cursor.execute(sql,(id_registro,))
                conexion.commit()

                print(f"Registro con ID {id_registro} eliminado exitosamente.")
                cursor.close()
                self.db.cerrar()  # Cerramos la conexión
        except Exception as e:
            print(f"Error al eliminar el registro: {e}")
