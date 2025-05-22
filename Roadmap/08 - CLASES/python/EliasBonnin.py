# Ejercicio 08
# En el siguiente URL https:/python.org Tenemos la documentacion de phyton
# # Los retos se encuentran en https://retosdeprogramacion.com

# Clases

class Programador:  # Se crea la clase

    apellido: str = None

    def __init__(self, nombre: str, edad: int, lenguajes: list):  # Constructor de la clase
        self.nombre = nombre
        self.edad = edad
        self.lenguajes = lenguajes

    def print(self):  # Funcion de la clase, en este caso muestra
        print(f"Nombre: {self.nombre} -- Apellido: {self.apellido} -- Edad: {self.edad} -- Lenguajes: {self.lenguajes}")


mi_programador = Programador("Elias", 26, ["Python", "C", "Java"])  # Llamado a constructor con los datos
mi_programador.print()  # LLamado a funcion de la clase
mi_programador.apellido = "Bonnin"
mi_programador.edad = 35
mi_programador.nombre = "Beto"
mi_programador.lenguajes = ["Ninguno"]
mi_programador.print()  # Alteramos los valores y mostramos


# Extra
