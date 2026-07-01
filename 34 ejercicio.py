#Pedir dos números al usuario
numero1 = float(input("Ingrese el primer número:"))
numero2 = float(input("Ingrese el segundo número:"))
#Compara los números
if numero1>numero2:
    print("El primer número es mayor.")
elif numero2>numero1:
    print("El segundo número es mayor.")
else:
    print("Los dos números son iguales.")