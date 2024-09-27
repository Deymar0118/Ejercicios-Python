Nombre = input("Ingrese su nombre: ")
Apellido = input("Ingrese su apellido: ")
Edad = int(input("Ingrese su edad: "))

Opcion = int(input('¿Tiene cédula? 1. Sí, 2. No: '))

if Edad >= 18 and Opcion == 1:
    print(f"¡Bienvenido {Nombre} {Apellido}!")
else:
    print(f"Lo siento. No puede entrar")