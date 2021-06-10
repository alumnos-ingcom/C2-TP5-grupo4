################
# Walter Ulises Ayllapan - @ulisesbrc
# Ejercicio 1. Pares e impares
# UNRN Andina - Introducción a la Ingenieria en Computación
################
# Reemplazar por las funciones del ejercicio
def ingreso_entero(mensaje):
    """
    Esta funcion muestra un mensaje y agrega la # para indicar el ingreso
    de un número entero.
    """
    try:
        ingreso = input(mensaje + " #")
        entero = int(ingreso)
        return entero  
    except ValueError as error:
        raise IngresoIncorrecto("No era un entero")
def ingreso_entero_reintento(mensaje, cantidad_reintentos=5):
    """
    Esta funcion llama a la funcion ingreso_entero() y si esta no devuelve un entero
    se llama el numero de veces segun tenga la variable cantidad_reintentos
    """
    while cantidad_reintentos>0:
        try:
            entero = ingreso_entero(mensaje)
            return entero
        except IngresoIncorrecto as err:
            cantidad_reintentos = cantidad_reintentos-1
            print(f"Te quedan {cantidad_reintentos} intentos!")
    raise IngresoIncorrecto("Te quedaste sin intentos!")
class IngresoIncorrecto(Exception):
    pass
def division_lenta(dividendo, divisor):
    """
    Esta funcion devuelve el cociente y el resto de un numero entrero y su divisor.
    """
    cociente = 1
    if dividendo==0:
        return 0,0
    else:
        if dividendo<0:
            dividendo = -dividendo
    if divisor==0:
        try:
            return dividendo/divisor
        except:
            raise "No se puede dividir por 0"
    else:
        if divisor<0:
            divisor = -divisor
    resto = dividendo - divisor
    while resto >= divisor:
        cociente = cociente +1
        resto = resto - divisor
    return (cociente,resto)
def es_par(numero):
    """
    Esta funcion devuelve true si el numero entero ingresado es par o false de lo contrario.
    """
    cociente, resto = division_lenta(numero,2)
    if resto==0:
        return True
    else:
        return False

def prueba():
    cantidad_de_intentos=10
    numero= ingreso_entero_reintento("Ingrese un numero:",10)
    if es_par(numero):
        print(f"El número {numero} es par")
    else:
        print(f"El número {numero} no es par")
    
if __name__ == "__main__":
    prueba()  