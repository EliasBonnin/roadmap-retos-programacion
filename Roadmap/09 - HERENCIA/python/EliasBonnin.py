# Ejercicio 09
# En el siguiente URL https:/python.org Tenemos la documentacion de phyton.
# Los retos se encuentran en https://retosdeprogramacion.

# SuperClase

class Animal:

    def __init__(self, nombre: str):
        self.nombre = nombre

    def sonido(self):
        pass


# SubClases

class Perro(Animal):

    def sonido(self):
        print("Guau")


class Gato(Animal):

    def sonido(self):
        print("Miau")


def sonido_animal(Animal: Animal):
    Animal.sonido()


mi_animal = Animal(Animal)
sonido_animal(mi_animal)
mi_perro = Perro("Perro")
mi_gato = Gato("Gatito")
sonido_animal(mi_gato)
sonido_animal(mi_perro)
