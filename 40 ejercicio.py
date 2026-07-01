#Pedir un número al usuario
numero = int(input("Ingresa un número:"))
#Determinar si es par y mayor que 50
if numero %2==0 and numero >50:
    print("El número es par y mayor que 50")
else:
    print("El número no cumple las dos condiciones")