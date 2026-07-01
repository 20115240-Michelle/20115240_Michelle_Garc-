#Pedir un número al usuario 
numero = int(input("Ingresa un número:"))
if 1 <= numero <= 10:
    print("El número esta en el rango 1-10")
elif 11<=numero <=20:
    print("El número esta en el rango 11-20")
elif numero > 20:
    print("El número es mayor de 20")
else:
    print("El número es menor que 1")