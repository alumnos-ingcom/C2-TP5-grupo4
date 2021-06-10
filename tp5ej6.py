################
# Walter Ulises Ayllapan - @ulisesbrc
# Ejercicio 6. Parentesis balanceados
# UNRN Andina - Introducción a la Ingenieria en Computación
################
def parentesis_balanciado(texto,caracter_apertura="[",caracter_cierre="]"):
    """
    Esta funcion verifica si el texto pasado con sus caracteres de apertura
    y cierre esta balanceado
    """
    estructura=""
    if caracter_apertura in texto:
        for c in texto:
            if c==caracter_apertura:
                estructura=estructura +"1"
            if c==caracter_cierre:
                estructura=estructura +"0"
        cantidad = len(estructura)
        if cantidad%2==0:
            mitad = int(cantidad/2)
            estructura_a = estructura[0:mitad]
            estructura_b = estructura[mitad:cantidad]
            if estructura_a[0]=="1":
                for i in range(0,mitad):
                    if estructura_a[i] and not (estructura_b[i]):
                        return False
                return True
            else:
                return False
        else:
            return False    
    else:
        return False
def prueba():
    caracter_apertura = input("Ingrese un caracter de apertura ejemplo [:")
    caracter_cierre = input("Ingrese un caracter de cierre, ejemplo ]:")
    texto = input(f"Ingrese un texto:")
    if parentesis_balanciado(texto,caracter_apertura,caracter_cierre):     
        print(f"El texto {texto} está balanceado")
    else:
        print(f"El texto {texto} no está balanceado")
if __name__ == "__main__":
    prueba()  