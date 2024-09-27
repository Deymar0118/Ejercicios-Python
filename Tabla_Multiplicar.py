num = int (input("escriba el numero de la tabla: "))
cant = int(input("¿Cuantas veces se va a multiplicar?: "))
i =1
Resultado =0

for i in range(1,cant+1):
    Resultado = num *i
    print(num, " * ", i, " = ", Resultado)