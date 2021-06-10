################
# Walter Ulises Ayllapan - @ulisesbrc
# Ejercicio 3. ¡Tribonacci!
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from tp5ej2 import numero_entero_mayor_a
def tribonacci(numero):
    """
    Esta funcion recibe un número entero mayor a 3 y devuelve numero-esimo de la
    secuencia de Tribonacci
    """
    y=list(range(0,numero))
    y[0]=1
    for i in range(1,numero):
        if i>=3:
            y[i] = y[i-1]+y[i-2]+y[i-3]
        else:
            y[i]=1
    return y[numero-1]
def prueba():
    numero=False
    numero_minimo = 3
    numero =numero_entero_mayor_a(f"Ingrese un entero mayor a {numero_minimo}:",numero_minimo)
    lista = tribonacci(numero)          
    print(f"El {numero}º término de la sucesión de Tribonacci es {lista}")
if __name__ == "__main__":
    prueba()  