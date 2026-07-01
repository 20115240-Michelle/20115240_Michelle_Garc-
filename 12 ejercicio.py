 #Pedimos el número al usuario
numero = float(input("Ingresa un número para calcular su raiz cuabica:"))
#Calculamos la raiz cúbica usando el exponenete(1/3)
if numero >=0:
    raiz_cubica = numero **(1/3)
else:
    #Para negativos, la raiz cúbica si existe (resultado negativo)
    raiz_cubica = -((-numero)**(1/3))
    print(f"La raiz cúbica de (número) es:{raiz_cubica}")