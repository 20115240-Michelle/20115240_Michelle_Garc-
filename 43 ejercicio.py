#Pedir un número al usuario
numero = float(input("Ingresar un número:"))
#Determinar si es menor que 10,entre 10 y 50, o mayor que 50
if numero < 10:
    print("El número es menor que 10.")
elif 10<=numero <=50:
    print("El número está entre 10 y 50.")
else:
    print("El número es mayor que 50.")