#Pedir al usuario la nota 
nota = float(input("Ingresar la nota entre 0 y 10:"))
#Clasificar las notas 
if nota>=0 and nota<=5:
    print("Reprobado")
elif nota>=6 and nota<=7:
    print("Suficiente")
elif nota>=8 and nota <=9:
    print("Notable")
elif nota ==10:
    print("Excelente")
else:
    print("Nota fuera del rango")