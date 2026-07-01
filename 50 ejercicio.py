#calculamos una calculadora básica
#Pedimos dos números
numero1= float(input("Ingresa el primer número:"))
numero2= float(input("Ingresa el segundo número:"))
#Pedimos la operación
operacion= input("Ingresa la operación (+,-,*,/):")
if operacion =="+":
    print(numero1,"+",numero2, "=",numero1+numero2)
elif operacion =="-":
    print(numero1, "-",numero2, "=",numero1-numero2)
elif operacion == "*":
    print(numero1, "*", numero2, "=",numero1*numero2)
elif operacion =="/":
  print(numero1, "/", numero2, "=", numero1/numero2)
else:
    print("Operación no válida")