#Pedir dos números al usuario y mostrar el mayor
numero1 = float(input("Ingresa el primer número:"))
numero2 = float(input("Ingresa el segundo número:"))
#Comparar y mostrar el mayor
if numero1 >numero2:
    print("El número mayor es:", numero1)
elif numero2 > numero1:
    print("El número mayor es:", numero2)
else:
    print("Los dos números son iguales")