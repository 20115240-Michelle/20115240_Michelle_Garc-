#Pedir al usuario un número
numero = float(input("Ingresa un número:"))
#Determinar si es múltiplo de 5
if numero %5==0:
    print(f"{numero} es múltiplo de 5")
else:
    print(f"{numero} no es múltiplo de 5")