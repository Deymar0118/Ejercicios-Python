Cant_Par =0
Cant_Impar =0

num = int (input("Ingrese el numero (negativo para terminar): "))

while num >= 0:
    if num%2 ==0:
        Cant_Par = Cant_Par +1
    if num%2 !=0:
        Cant_Impar = Cant_Impar +1
    num = int (input("Ingrese otro numero (negativo para terminar): "))
    
print("hay una cantidad de ",Cant_Impar," de numeros impares.")
print("hay una cantidad de ",Cant_Par," de numeros pares.")