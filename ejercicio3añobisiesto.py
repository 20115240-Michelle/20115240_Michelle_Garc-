#Determinar si un año es bisiesto 
año = 2024
if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print(f"{año} es un año bisiesto")
else:
    print(f"{año} no es bisiesto")