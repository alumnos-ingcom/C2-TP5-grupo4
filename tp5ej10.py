################
# Walter Ulises Ayllapan - @ulisesbrc
# Ejercicio 10. Texto binario
# UNRN Andina - Introducción a la Ingenieria en Computación
################
# Reemplazar por las funciones del ejercicio
from tp5ej1 import ingreso_entero_reintento
from tp5ej9 import descomponer_numero
def verificar_texto_binario(texto):
    """
    Esta funcion verifica si un texto contiene 0 y 1 en caso afirmativo devuelve True sino False
    """
    for c in texto:
        cod_ascci = ord(c)
        if not (cod_ascci ==48 or cod_ascci ==49):
            return False
    return True
def texto_binario_a_numero(texto_binario):
    """
    Esta funcion transforma un texto binario a un numero entero
    """
    cantidad = len(texto_binario)
    cantidad= cantidad-1
    numero=0
    for t in texto_binario:
        numero = numero+(int(t)*(2**cantidad))
        cantidad= cantidad-1
    return numero
    
def numero_a_texto_binario(numero):
    """
    Esta funcion devuelve un texto en binario de un número entero positivo
    """
    texto_binario=""
    lista_numero = descomponer_numero(numero,base=2)
    lista_binaria = lista_numero[::-1]
    for i in lista_binaria:
        texto_binario=texto_binario+str(i)
    return texto_binario
def prueba():
    cantidad_de_intentos=10
    numero= ingreso_entero_reintento("Ingrese un número:",cantidad_de_intentos)
    texto_binario = numero_a_texto_binario(numero)
    print(f"El texto binario del numero {numero} es {texto_binario}")
    pedir_texto=True
    while pedir_texto:
        texto = input("Ingrese un texto binario:")
        if verificar_texto_binario(texto):
            pedir_texto=False
        else:
            print("No es un texto binario, intente nuevamente")
    numero = texto_binario_a_numero(texto)
    print(f"El numero del texto binario {texto} es {numero}")   
if __name__ == "__main__":
    prueba()  