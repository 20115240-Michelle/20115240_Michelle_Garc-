#Pedir dos número al usuario 
numero1 = float(input("Ingresa el primer número:"))
numero2 = float(input("Ingresa el segundo número:"))
#Comparar y mostrar el menor
if numero1<numero2:
    print("El número menor es:", numero1)
elif numero2<numero1:
    print("El número menor es:", numero2)
else:
    print("Ambos números son iguales") 