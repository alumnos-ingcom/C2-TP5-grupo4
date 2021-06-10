################
# Walter Ulises Ayllapan - @ulisesbrc
# Ejercicio 7. Distancias
# UNRN Andina - Introducción a la Ingenieria en Computación
################
def distancia(numero_uno,numero_dos):
    """
    Esta funcion determina la distancia entre dos números
    """
    if (numero_uno>=0 and numero_dos>=0):
        if numero_uno>numero_dos:
            distancia = numero_uno-numero_dos
        elif numero_uno<numero_dos:
            distancia = numero_dos-numero_uno
        else:
            distancia=0
    else:
        if numero_dos==numero_uno:
            distancia=0
        elif numero_dos==-numero_uno or numero_dos>numero_uno:
            distancia = numero_dos-numero_uno
            if distancia<0:
                distancia=-distancia
        else:
            distancia =numero_uno-numero_dos
    return distancia
def ingreso_float(mensaje):
    """
    Esta funcion muestra un mensaje y agrega la # para indicar el ingreso
    de un número.
    """
    try:
        ingreso = input(mensaje + " #")
        entero = float(ingreso)
        return entero  
    except ValueError as error:
        raise IngresoIncorrecto("No era un número")
def prueba():
    numero_uno=False
    numero_dos=False
    mensaje="Ingrese un número"
    numero_uno = ingreso_float(mensaje)
    numero_dos = ingreso_float(mensaje)    
    distancia_numeros = distancia(numero_uno,numero_dos)
    print(f"La distancia entre el número {numero_uno} y el número {numero_dos} es de {distancia_numeros}")
if __name__ == "__main__":
    prueba()  