opcion =0
while opcion == 0:
    Texto = str(input("ingrese una palabra: "))
    cant = int (len(Texto))
    print("hay una cantidad de ",cant, " letras en la palabra ",Texto)
    print("¿Que accion desea realizar?")
    print("_________________________")
    print("1. Escribir palabra")
    print("2. Salir")
    opcion= int (input("elija una opcion: "))