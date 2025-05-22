# Ejercicio 11
# En el siguiente URL https:/python.org Tenemos la documentacion de phyton
# # Los retos se encuentran en https://retosdeprogramacion.com

# Manejo de Ficheros

import os

nombre_archivo = "EliasBonnin.txt"

with open(nombre_archivo, "w") as archivo:
    archivo.write("Bonnin Elias\n")
    archivo.write("26\n")
    archivo.write("Python\n")

with open(nombre_archivo, "r") as archivo:
    print(archivo.read())

os.remove(nombre_archivo)


# Extra
