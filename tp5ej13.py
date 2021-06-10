################
# Walter Ulises Ayllapan - @ulisesbrc
# Ejercicio 13. Búsqueda de palabras
# UNRN Andina - Introducción a la Ingenieria en Computación
################
# Reemplazar por las funciones del ejercicio
class No_se_encuentra(Exception):
    pass
def ubicacion_de_la_palabra_en_el_texto(palabra,texto):
    """
    Esta funcion devuelve la ubicación de la palabra en el texto si existe la palabra en el texto sino devuelve una excepcion
    """
    cantidad_caracteres_palabra=len(palabra)
    cantidad_caracteres_texto=len(texto)
    caracter_inicio=0
    while caracter_inicio<cantidad_caracteres_texto:
        texto_auxiliar =texto[caracter_inicio:cantidad_caracteres_palabra]
        if palabra==texto_auxiliar:
            return caracter_inicio+1
        else:
            caracter_inicio=caracter_inicio+1
            cantidad_caracteres_palabra=cantidad_caracteres_palabra+1
            
    raise No_se_encuentra("La palabra no forma parte del texto")
def prueba():
    palabra=input("Ingrese una palabra:")
    texto=input("Ingrese un texto:")
    ubicacion= ubicacion_de_la_palabra_en_el_texto(palabra,texto)
    print(f"La palabra {palabra} se encuentra en la ubicación {ubicacion} del texto \"{texto}\"")
    
if __name__ == "__main__":
    prueba()  