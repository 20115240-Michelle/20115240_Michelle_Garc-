#Pedir un número al usuario
numero = float(input("Por favor, Ingresar un número:"))
#Mostrar si es negativo, positivo o cero
if numero>0:
    print("El número es positivo.")
elif numero<0:
    print("El número es negativo.")
else:
    print("El número es cero.")