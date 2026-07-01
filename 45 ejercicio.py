#Pedir que el usuario ingrese una letra
letra = input("Ingresar una letra:")
#Verificar si es una vocal o una consonante 
if letra in "a,e,i,o,u":
    print("Es una vocal")
elif letra in "b,c,d,f,g,h,j,k,l,m,n,ñ,p,q,r,s,t,v,w,x,y,z":
    print("Es una consonante")
else:
    print("No ingresaste letra.")