#Pedir al usuario una letra para ver el significado
Calificacion = input("Ingresa tu calificación (A,B,C,D,F):")
#Verificar el significado
if Calificacion =="A":
    print("Excelente")
elif Calificacion=="B":
    print("Bueno")
elif Calificacion =="C":
    print("Regular")
elif Calificacion == "D":
    print("Deficiente")
elif Calificacion == "F":
    print("Reprobado")
else:
    print("Calificación no válida.")