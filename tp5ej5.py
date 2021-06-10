################
# Walter Ulises Ayllapan - @ulisesbrc
# Ejercicio 5. Inversión de mayúsculas
# UNRN Andina - Introducción a la Ingenieria en Computación
################
def inversion_texto(texto):
    """
    Esta funcion recibe un string y pasa los caracteres de mayúsculas a minúsculas
    o de minúscula a mayúscula según corresponda
    """
    texto_aux=""
    vocales_mayuscula="ÁÉÍÓÚÑ"
    vocales_minusculas="áéíóúñ"
    lista_vocales_mayuscula=[]
    lista_vocales_minuscula=[]
    #convierto a codiigo ascci
    for c in vocales_minusculas:
        lista_vocales_minuscula.append(ord(c))
    for c in vocales_mayuscula:
        lista_vocales_mayuscula.append(ord(c))
    for c in texto:
        #obtengo su valor ASCII 
        cod_ascci = ord(c)
        if (cod_ascci>=97 and cod_ascci<=122) or cod_ascci in lista_vocales_minuscula:
            cod_ascci=cod_ascci-32
        elif (cod_ascci>=65 and cod_ascci<=90) or cod_ascci in lista_vocales_mayuscula:
            cod_ascci=cod_ascci+32
        texto_aux = texto_aux + chr(cod_ascci)
    return texto_aux
def prueba():
    texto = input(f"Ingrese un texto:")
    inversiontexto=inversion_texto(texto)
    print(f"El texto {texto} convertido es {inversiontexto}")
if __name__ == "__main__":
    prueba()  