# Ejercicio 10
# En el siguiente URL https:/python.org Tenemos la documentacion de phyton
# # Los retos se encuentran en https://retosdeprogramacion.com

# Expeciones

try:
    print(10/0)
    print([1, 2, 3, 4][4])
except Exception as e:
    print(f"Se ha producido un error: {e} ({type(e).__name__})")


# Extra

class StrTypeError(Exception):
    pass


def process_params(parameters: list):

    if len(parameters) < 3:
        raise IndexError()
    elif parameters[1] == 0:
        raise ZeroDivisionError()
    elif (parameters[2]) == str:
        raise StrTypeError(
            "El tercer elemento no puede ser una cadena de texto.")

    print(parameters[2])
    print(parameters[0]/parameters[1])
    print(parameters[2] + 5)


try:
    process_params([2] + 5)

except IndexError:
    print("El número de elementos de la lista debe ser mayor que dos.")
except ZeroDivisionError:
    print("El segundo elemento de la lista no puede ser un cero.")
except StrTypeError as e:
    print(f"{e}")
except Exception as e:
    print(f"Se ha producido un error inesperado: {e}")
else:
    print("No se ha producido ningún error.")
finally:
    print("El programa finaliza sin detenerse.")
