################
# Walter Ulises Ayllapan - @ulisesbrc
# Ejercicio 11. Promedio móvil
# UNRN Andina - Introducción a la Ingenieria en Computación
################
# Reemplazar por las funciones del ejercicio
def promedio_movil(lista,terminos):
    """
    Esta funcion devuelve una lista con los valores promedio movil de acuerdo al número termino
    """
    lista_promedio=[]
    cantidad = len(lista)
    inicio=0
    suma=0
    final=terminos+inicio
    while final<=cantidad:
        for i in range(inicio,final):
            suma = suma+lista[i]
        promedio = suma/terminos
        suma=0
        lista_promedio.append(promedio)
        inicio=inicio+1
        final=final+1
    return lista_promedio
def prueba():
    lista = []
    solicitar_numero=True
    mensaje="Ingrese numeros enteros, o una letra para salir #"
    while solicitar_numero:
        try:
            numero=int(input(mensaje))
            lista.append(numero)
        except:
            if len(lista) > 0:
                solicitar_numero=False
            else:
                mensaje="Ingrese otro número o una letra para salir:"
                continue
    solicitar_numero=True
    limite = len(lista)
    while solicitar_numero:
        try:
            numero_dos=int(input(f"Ingrese un numero entero positivo menor a {limite} #"))
            if numero_dos>0 and numero_dos<limite:
                solicitar_numero=False
        except:
            print("Ingrese un número válido")
            continue
    print(f"La lista contiene los valores {lista}")
    lista_promedio = promedio_movil(lista,numero_dos)
    print(f"La lista promedio movil con valores contiguos {numero_dos} es {lista_promedio}")
if __name__ == "__main__":
    prueba()  