################
# Walter Ulises Ayllapan - @ulisesbrc
# Ejercicio 9. Factoriones
# UNRN Andina - Introducción a la Ingenieria en Computación
################
# Reemplazar por las funciones del ejercicio
from tp5ej1 import ingreso_entero_reintento
def factorial(numero):
    """
    Esta funcion devuelve el factorial de un número
    """
    factorial=1;
    if numero==0:
        return factorial
    for i in range(1,numero+1):
        factorial = factorial*i
    return factorial
def descomponer_numero(numero,base=10):
    """
    Esta funcion descompone un número en sus unidades
    """
    lista=[]
    if numero==0:
        return [0]
    while(numero>0):
        resto = numero%base
        lista.append(resto)
        numero=numero//base
    return lista
def lista_factoriones(numero):
    """
    Esta funcion devuelve una lista de los numeros factoriones menores o iguales al número ingresado
    """
    listafactoriones=[]
    for i in range(0, numero+1):
        if es_factorion(i):
            listafactoriones.append(i)
    return listafactoriones
def es_factorion(numero):
    """
    Esta funcion verifica si un número es factorion
    """
    lista_numeros = descomponer_numero(numero)
    suma=0
    for i in lista_numeros:
        suma = suma+factorial(i)
    if suma ==numero:
        return True
    else:
        return False
def prueba():
    cantidad_de_intentos=10
    numero= ingreso_entero_reintento("Ingrese un número:",cantidad_de_intentos)
    listafactoriones = lista_factoriones(numero)
    print(f"Los factoriones menores a {numero} son {listafactoriones}")
    
if __name__ == "__main__":
    prueba()  