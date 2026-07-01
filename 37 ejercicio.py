#Pedir al usuario un número
numero = float(input("Ingresa un número:"))
#Determinar si es divisible entre 2 y 3
if numero %2 ==0 and numero %3==0:
    print(f"{numero} SI es divisible entre 2 y 3")
else:
    print(f"{numero} NO es divisible entre 2 y 3")