import matplotlib.pyplot as plt
import numpy as np

class Vista:
    def mostrar_menu(self):
        """Muestra las opciones del menú al usuario"""
        print("\nElige una opción:")
        print("1. Calcular desviación estándar manual")
        print("2. Calcular desviación estándar usando numpy")
        print("3. Mostrar gráfica")
        print("4. Ver registros")
        print("5. Eliminar registro")
        print("6. Salir")

    def mostrar_resultado(self, registro):
       self.mostrar_tabla(registro)


    def obtener_cantidad_numeros(self):
        while True:
            try:
                cantidad = int(input("¿Cuántos números deseas ingresar? "))
                if cantidad <= 0:
                    self.mostrar_mensaje("Por favor, ingresa un número positivo mayor que 0.")
                    continue
                return cantidad
            except ValueError:
                self.mostrar_mensaje("Ingresa un número válido.")

    def mostrar_tabla(self, resultados):
        self.mostrar_mensaje("\n+----+--------------------------+-----------------------+---------------------+")
        self.mostrar_mensaje("| ID | Media                    | Desviación Estándar   | Fecha               |")
        self.mostrar_mensaje("+----+--------------------------+-----------------------+---------------------+")

        for resultado in resultados:
            id_ = resultado[0]
            media = f"{float(resultado[1]):.2f}"  # Convertir la media a float y formatear
            desviacion = f"{float(resultado[2]):.2f}"  # Convertir la desviación estándar a float y formatear
            fecha = resultado[3]

            self.mostrar_mensaje(f"| {id_:<2} | {media:<24} | {desviacion:<21} | {fecha} |")

        self.mostrar_mensaje("+----+--------------------------+-----------------------+---------------------+")

    def mostrar_ids(self, ids):
        if ids:
            self.mostrar_mensaje("\nRegistros disponibles para eliminar:")
            self.mostrar_tabla(ids)  # Usamos la función auxiliar para mostrar la tabla de IDs
        else:
            self.mostrar_mensaje("No hay registros disponibles para eliminar.")

    def eliminar_id(self):
        while True:
            try:
                id_registro = int(input("Ingresa el ID del registro que deseas eliminar: "))
                return id_registro
            except ValueError:
                self.mostrar_mensaje("Ingresa un número válido para el ID del registro.")

    def obtener_numeros(self, cantidad):
        numeros = []
        for i in range(cantidad):
            while True:
                try:
                    numero = int(input(f"Ingresa el número {i+1}: "))
                    numeros.append(numero)
                    break
                except ValueError:
                    self.mostrar_mensaje("Ingresa un número válido.")
        return numeros

    def mostrar_mensaje(self, mensaje):
        print(mensaje)

    def graficar_datos(self, datos):
        media = np.mean(datos)
        desviacion_estandar = np.std(datos)
        
        plt.figure(figsize=(8, 5))
        
        # Graficar los puntos del dataset
        plt.plot(datos, marker='o', linestyle='-', label='Datos')
        
        # Graficar la media
        plt.axhline(media, color='red', linestyle='--', label=f'Media: {media:.2f}')
        
        # Graficar las líneas para la desviación estándar (media ± desviación estándar)
        plt.axhline(media + desviacion_estandar, color='green', linestyle='--', label=f'Media + 1 Desviación Estándar')
        plt.axhline(media - desviacion_estandar, color='green', linestyle='--', label=f'Media - 1 Desviación Estándar')
        
        # Añadir título, etiquetas y leyenda
        plt.title("Datos, Media y Desviación Estándar")
        plt.xlabel("Índice")
        plt.ylabel("Valor")
        plt.legend()
        
        # Mostrar cuadrícula y ajustar el diseño
        plt.grid(True)
        plt.tight_layout()
        
        # Mostrar el gráfico
        plt.show()

    def mostrar_datos(self, resultados):
        self.mostrar_tabla(resultados)  # Usamos la función auxiliar para mostrar los registros completos
