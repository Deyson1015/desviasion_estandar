from Models.desviasionModel import ModeloDesviacion
from Views.desviasionView import Vista

class Controlador:
    def __init__(self):
        self.modelo = ModeloDesviacion()  # Instanciamos el modelo para manejar la lógica de los datos
        self.vista = Vista()  # Instanciamos la vista para mostrar los resultados al usuario

    def ejecutar(self):
        while True:
            # Mostrar el menú al usuario
            self.vista.mostrar_menu()

            # Pedir la opción deseada al usuario
            opcion = input("Ingresa el número de la opción deseada: ")

            # Salir del programa
            if opcion == "6":
                self.vista.mostrar_mensaje("Saliendo del programa...")
                break

            # Opción 1: Calcular desviación estándar manual
            elif opcion == "1":
                # Pedir la cantidad de números y obtener los números
                cantidad = self.vista.obtener_cantidad_numeros()
                self.modelo.datos = self.vista.obtener_numeros(cantidad)

                # Calcular la desviación estándar y mostrar el resultado
                media, desviacion = self.modelo.calcular_manual()
                registro = self.modelo.obtener_ultimo()
                self.vista.mostrar_resultado(registro)
                
                # Guardar solo la media y la desviación estándar en la base de datos
                self.modelo.guardar(media, desviacion)

            # Opción 2: Calcular desviación estándar usando numpy
            elif opcion == "2":
                # Usar datos predefinidos para el cálculo con numpy
                datos_numpy = [86, 87, 88, 86, 87, 85, 86]
                self.modelo.datos = datos_numpy

                # Calcular la desviación estándar y mostrar el resultado
                media, desviacion = self.modelo.calcular_numpy()
                registro = self.modelo.obtener_ultimo()
                self.vista.mostrar_resultado(registro)

                # Guardar la media y la desviación estándar en la base de datos
                self.modelo.guardar(media, desviacion)

            # Opción 3: Mostrar gráfica de los datos
            elif opcion == "3":
                if self.modelo.datos:
                    self.vista.graficar_datos(self.modelo.datos)
                else:
                    self.vista.mostrar_mensaje("Primero debes calcular la desviación para tener datos que graficar.")

            # Opción 4: Ver registros 
            elif opcion == "4":
                # Obtener todos los registros de la base de datos
                resultados = self.modelo.obtener_datos()

                # Mostrar los datos completos en formato tabla
                self.vista.mostrar_datos(resultados)

            # Opción 5: Eliminar un registro
            elif opcion == "5":
                # Obtener los IDs de los registros disponibles para eliminar
                ids = self.modelo.obtener_datos()

                if not ids:
                    self.vista.mostrar_mensaje("No hay registros disponibles para eliminar.")
                    continue  # Volver al menú principal si no hay registros

                # Mostrar los IDs disponibles para eliminar
                self.vista.mostrar_ids(ids)

                # Obtener el ID del registro a eliminar
                id_registro = self.vista.eliminar_id()
                self.modelo.eliminar_registro(id_registro)

            # Opción no válida
            else:
                self.vista.mostrar_mensaje("Opción no válida. Intenta de nuevo.")
