filas = int (input("ingrese el numeo de filas"))
i=0
j=0
coef =0

for i in range (0,filas-1,+1):
    coef = 1
    for j in range(0,filas-1,+1):
        print ("")
    for j in range(0,i +1):
        print (coef, " ")
        coef = coef * (i - j) / (1 + j)
    print("")
