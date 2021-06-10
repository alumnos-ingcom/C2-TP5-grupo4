################
# Walter Ulises Ayllapan - @ulisesbrc
# Ejercicio 4. Números perfectos
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from tp5ej2 import numero_entero_mayor_a
def es_numero_perfecto(numero):
    """
    Esta funcion recibe un número entero positivo y devuelve true si el número
    es perfecto sino devuelve falso
    """
    if numero<=0:
        return False
    else:
        suma=0;
        for i in range(1,numero):
            if numero%i==0:
                suma=suma+i
    return numero==suma
def prueba():
    numero_minimo = 0
    numero=numero_entero_mayor_a(f"Ingrese un entero mayor a {numero_minimo}:",numero_minimo)
    esnumeroperfecto = es_numero_perfecto(numero)
    if esnumeroperfecto:
        print(f"El número {numero} es perfecto")
    else:
        print(f"El número {numero} no es perfecto")
if __name__ == "__main__":
    prueba()  