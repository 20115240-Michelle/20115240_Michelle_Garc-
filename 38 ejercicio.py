#Pedir un número al usuario
numero = int(input("Ingresar un número:"))
#Determinar si terminan en 0
if numero %10==0:
    print("SI, termina en 0.")
else:
    print("NO, termina en 0.")