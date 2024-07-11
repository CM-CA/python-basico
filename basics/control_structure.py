# Estructuras de control. 
# Se utilizan para ejecutar bloques de código según que condiciones se cumplen. 
# la sentencia es if - else

# ejemplo: Si a es igual a 1 imprime true, si es distinto de 1 imprime false

a = int(input("mete numero: "))

if a == 1:
    print(True)
elif a != 1:
    print (False)
else:
    print("Eres tontisimo")