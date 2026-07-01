#Pedir la edad al usuario
edad= int(input("Por favor, Ingrese su edad:"))
#Clasificarla según la edad del usuario
if 0<=edad<=12:
    print("Eres un niño/a")
elif 13<=edad<=17:
    print("Eres un adolescente")
elif 18<=edad<=59:
    print("Eres un adulto")
elif edad>=60:
    print("Eres un adulto mayor")
