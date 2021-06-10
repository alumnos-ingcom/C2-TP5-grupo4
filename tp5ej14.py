################
# Walter Ulises Ayllapan - @ulisesbrc
# Ejercicio 14. Números capicúa
# UNRN Andina - Introducción a la Ingenieria en Computación
################
# Reemplazar por las funciones del ejercicio
from tp5ej9 import descomponer_numero
from tp5ej2 import numero_entero_mayor_a
def es_capicua(numero):
    """
    Esta funcion devuelve si un número entero positivo es capicua
    """
    lista_numero = descomponer_numero(numero,base=10)
    lista_numero_opuesta = lista_numero[::-1]
    return lista_numero==lista_numero_opuesta
def prueba():
    mayor_a=0
    numero= numero_entero_mayor_a(f"Ingrese un número entero positivo mayor a {mayor_a}",mayor_a)
    if es_capicua(numero):
        print(f"El número {numero} es capicua")
    else:
        print(f"El número {numero} no es capicua")
if __name__ == "__main__":
    prueba()  