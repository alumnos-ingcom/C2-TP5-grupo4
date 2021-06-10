################
# Walter Ulises Ayllapan - @ulisesbrc
# Ejercicio 2. Fibonacci
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from tp5ej1 import ingreso_entero
def numero_entero_mayor_a(mensaje,mayor_a):
    """
    Esta funcion devuelve un número entero mayor a la variable mayor_a
    """
    solicitar_numero=True
    while solicitar_numero:
        numero = ingreso_entero(mensaje)
        if numero > mayor_a:
            return numero
        else:
            continue
def fibonacci(numero):
    """
    Esta funcion recibe un número entero mayor a 2 y devuelve numero-esimo de la
    sucesión de Fibonacci
    """
    y=list(range(0,numero))
    y[0]=0
    for i in range(1,numero):
        if i>=2:
            y[i] = y[i-1]+y[i-2]
        else:
            y[0]=1
    return y[numero-1]
def prueba():
    numero_minimo = 2
    numero =numero_entero_mayor_a(f"Ingrese un entero mayor a {numero_minimo}:",numero_minimo)
    termino = fibonacci(numero)          
    print(f"El {numero}º término de la sucesión de Fibonacci es {termino}")
    pass
if __name__ == "__main__":
    prueba()  