#Pedimos al usuario el número 
numero = float(input("Ingresar un numero para calcular su cubo:"))
#Calculamos el cubo usandopow()
cubo = pow(numero,3)
#Mostramos el resultado 
print(f"El cubo de {numero} es:{cubo}")