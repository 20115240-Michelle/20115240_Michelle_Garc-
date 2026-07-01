#Pedir al usuario tres números
numero1 = float(input("Ingresar el primer número:"))
numero2 = float(input("Ingresar el segundo número:"))
numero3 = float(input("Ingresar el tercer número:"))
#Realizar la multiplicación de tres números 
multiplicacion =numero1 * numero2 * numero3
#Calcular la raiz cúbica (exponente 1/3)
raiz_cubica =multiplicacion **(1/3)
#Mostrar el resultado 
print(f"La raiz cúbica de la multiplicación es:{raiz_cubica}")
