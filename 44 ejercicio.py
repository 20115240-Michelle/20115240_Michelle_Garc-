#Pedir un número del 1 al 7 al usuario
numero = int(input("Ingresar un número del 1 al 7:"))
#Mostrar el dia de la semana
if numero ==1:
    print("Lunes")
elif numero ==2:
    print("Martes")
elif numero ==3:
    print("Miércoles")
elif numero ==4:
    print("Jueves")
elif numero ==5:
    print("Viernes")
elif numero ==6:
    print("Sabado")
elif numero ==7:
    print("Domingo")
else:
    print("Número inválido. Tiene que ser entre 1 y 7.")