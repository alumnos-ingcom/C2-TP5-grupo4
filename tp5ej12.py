################
# Walter Ulises Ayllapan - @ulisesbrc
# Ejercicio 12. Comparación de listas
# UNRN Andina - Introducción a la Ingenieria en Computación
################
# Reemplazar por las funciones del ejercicio
def listas_con_mismos_elementos(lista_uno,lista_dos):
    """
    Esta funcion verifica si dos listas tienen los mismos elementos
    """
    if len(lista_uno) != len(lista_dos):
        return False
    encontrados=0
    for i in lista_uno:
        if i in lista_dos:
            encontrados=encontrados+1
    return len(lista_uno)==encontrados
def prueba():
    lista_1=[1,"k",3,5]
    lista_2=[5,1,3,"k"]
    tienen_mismo_elementos= listas_con_mismos_elementos(lista_1,lista_2)
    print(f"{tienen_mismo_elementos}")
    
if __name__ == "__main__":
    prueba()  