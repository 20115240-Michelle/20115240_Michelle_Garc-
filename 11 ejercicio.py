import math
 #Pedimos al usuario un número 
numero = float(input("Ingresa un número para calcular su raiz cuadrada:"))
#Verificar que el número no sea negativo
if numero >=0:
    raiz = math.sqrt(numero)
    print("La raiz cuadrada de",numero, "es.", raiz)
else:
    print("Error:No se puede calcular la raiz cuadrada de un número negativo")