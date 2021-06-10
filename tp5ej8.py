################
# Walter Ulises Ayllapan - @ulisesbrc
# Ejercicio 8. El Cifrado del Cesar
# UNRN Andina - Introducción a la Ingenieria en Computación
################
def verificar_texto(texto):
    """
    Esta funcion verifica si un texto contiene caracteres dentro de un rango determinado por su valor ascii
    cuyos rangos representan a-z A-Z 0-9 en caso afirmativo devuelve True sino False
    """
    ascii_inicio_minuscula=97
    ascii_fin_minuscula=122
    ascii_inicio_mayuscula=65
    ascii_fin_mayuscula=90
    ascii_inicio_numero=48
    ascii_fin_numero=57
    for c in texto:
        texto_ascii = ord(c)
        if (texto_ascii>=ascii_inicio_minuscula and texto_ascii<=ascii_fin_minuscula) or (texto_ascii>=ascii_inicio_mayuscula and texto_ascii<=ascii_fin_mayuscula) or (texto_ascii>=ascii_inicio_numero and texto_ascii<=ascii_fin_numero):
            continue
        else:
            return False
    return True
def buscar_caracter_descifrado(caracter_codificado,inicio_numero_ascii,fin_numero_ascii):
    """
    Esta funcion busca un caracter_codificado dentro de un intervalo [inicio_numero_ascii,fin_numero_ascii] y
    para buscarlo suma diferencia_min_may al numero a buscar hasta que esté dentro del intervalo y lo devuelve
    """
    diferencia_min_may=fin_numero_ascii-inicio_numero_ascii+1
    while  not caracter_codificado>=inicio_numero_ascii or not caracter_codificado<=fin_numero_ascii:
        caracter_codificado=caracter_codificado+diferencia_min_may 
    return caracter_codificado
def buscar_caracter_cifrado(caracter_codificado,inicio_numero_ascii,fin_numero_ascii):
    """
    Esta funcion busca un caracter_codificado dentro de un intervalo [inicio_numero_ascii,fin_numero_ascii] y
    para buscarlo resta diferencia_min_may al numero a buscar hasta que esté dentro del intervalo y lo devuelve
    """
    diferencia_min_may=fin_numero_ascii-inicio_numero_ascii+1
    while not caracter_codificado>=inicio_numero_ascii or not caracter_codificado<=fin_numero_ascii:
        caracter_codificado=caracter_codificado-diferencia_min_may
    return caracter_codificado
def cifrado_del_cesar(texto,cantidad=1):
    """
    Esta funcion cifra la variable texto corriendo cada caracter el número de cantidad hacia de derecha de su ubicacion
    volviendo a empezar cuando termina el caracter a-zA-Z0-9
    ejemplo a lo cifra en b y z lo cifra en a si la cantidad es 1 
    ejemplo a lo cifra en e y z lo cifra en d si la cantidad es 4
    ejemplo 0 lo cifra en 1 y 9 lo cifra en 1 si la cantidad es 1
    ejemplo 0 lo cifra en 4 y 9 lo cifra en 5 si la cantidad es 4
    """
    caracteres="";
    ascii_inicio_minuscula=97
    ascii_fin_minuscula=122
    ascii_inicio_mayuscula=65
    ascii_fin_mayuscula=90
    ascii_inicio_numero=48
    ascii_fin_numero=57
    for c in texto:
        cod_ascii = ord(c)
        if (cod_ascii>=ascii_inicio_minuscula and cod_ascii<=ascii_fin_minuscula):#az
            caracter_codificado=cod_ascii+cantidad
            if caracter_codificado>ascii_fin_minuscula:
                caracter_codificado = buscar_caracter_cifrado(caracter_codificado,ascii_inicio_minuscula,ascii_fin_minuscula)                 
        elif (cod_ascii>=ascii_inicio_mayuscula and cod_ascii<=ascii_fin_mayuscula):#AZ
            caracter_codificado=cod_ascii+cantidad
            if caracter_codificado>ascii_fin_mayuscula:
                caracter_codificado = buscar_caracter_cifrado(caracter_codificado,ascii_inicio_mayuscula,ascii_fin_mayuscula)                 
        elif (cod_ascii>=ascii_inicio_numero and cod_ascii<=ascii_fin_numero):#numeros
            caracter_codificado = cod_ascii+cantidad
            if caracter_codificado>ascii_fin_numero:
                caracter_codificado = buscar_caracter_cifrado(caracter_codificado,ascii_inicio_numero,ascii_fin_numero)           
        caracteres = caracteres+ chr(caracter_codificado)
    return caracteres
def descifrado_del_cesar(texto,cantidad=1):
    """
    Esta funcion cifra descifra la funcion cifrado_del_cesar haciendo que recorra cada caracter de la variable texto
    el número de cantidad hacia de izquierda de su ubicacion
    volviendo a empezar cuando termina el caracter z-aZ-A9-0
    ejemplo b lo cifra en a y a lo cifra en z si la cantidad es 1 
    ejemplo e lo cifra en a y d lo cifra en z si la cantidad es 4
    ejemplo 1 lo cifra en 0 y 0 lo cifra en 9 si la cantidad es 1
    ejemplo 4 lo cifra en 0 y 3 lo cifra en 9 si la cantidad es 4
    """
    caracteres="";
    ascii_inicio_minuscula=97
    ascii_fin_minuscula=122
    ascii_inicio_mayuscula=65
    ascii_fin_mayuscula=90
    ascii_inicio_numero=48
    ascii_fin_numero=57
    caracter_codificado=0
    for c in texto:
        cod_ascii = ord(c)
        if (cod_ascii>=ascii_inicio_minuscula and cod_ascii<=ascii_fin_minuscula):#az
            caracter_codificado=cod_ascii-cantidad
            if caracter_codificado<ascii_inicio_minuscula:
                caracter_codificado = buscar_caracter_descifrado(caracter_codificado,ascii_inicio_minuscula,ascii_fin_minuscula)           
        elif (cod_ascii>=ascii_inicio_mayuscula and cod_ascii<=ascii_fin_mayuscula):#AZ
            caracter_codificado=cod_ascii-cantidad
            if caracter_codificado<ascii_inicio_mayuscula:
                caracter_codificado = buscar_caracter_descifrado(caracter_codificado,ascii_inicio_mayuscula,ascii_fin_mayuscula)           
        elif (cod_ascii>=ascii_inicio_numero and cod_ascii<=ascii_fin_numero):#numeros
            caracter_codificado = cod_ascii-cantidad
            if caracter_codificado<=ascii_inicio_numero:
                caracter_codificado = buscar_caracter_descifrado(caracter_codificado,ascii_inicio_numero,ascii_fin_numero)
        caracteres = caracteres+ chr(caracter_codificado)
    return caracteres

def prueba():
    cantidad_desplazamiento=False
    mensaje="Ingrese un texto válido"
    texto=""
    while not texto:
        try:
            texto=input("Ingrese un texto que contenga letras A-Za-z o números 0 a 9:")
            if(verificar_texto(texto)):
                break
            else:
                print(mensaje)
                texto=False
        except:
            print(mensaje)
            continue
    while not cantidad_desplazamiento:
        try:
            cantidad_desplazamiento = int(input("Ingrese un numero entero >0:"))
            if cantidad_desplazamiento==0:
                print("El número ingresado no es correcto, intente nuevamente")
                cantidad_desplazamiento=False
        except:
            print("No es un número válido, intente nuevamente")
            continue
    texto_cifrado=cifrado_del_cesar(texto,cantidad_desplazamiento)
    print(f"El texto {texto} cifrado es {texto_cifrado}")
    texto_descifrado= descifrado_del_cesar(texto_cifrado,cantidad_desplazamiento)
    print(f"El texto cifrado {texto_cifrado} descifrado es {texto_descifrado}")
 
if __name__ == "__main__":
    prueba()  