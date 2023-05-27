cadena = "Hola esta es una cadena"

print(cadena[0 : 10])
print(cadena[-10])

# Manipular mayus y minus
print(cadena.lower())
print(cadena.upper())
print(cadena.capitalize())
print(cadena.title())
print(cadena.swapcase())

# Ejercicios
# Imprimir los primero tres caracteres
print(cadena[0 : 2])
# Imprimir los ultimos tres caracteres
print(cadena[-3 : ])

# Remplazar la palabra "Separado" por "S,e,p,a,r,a,d,o"
palabra = "eparado"
resultado = palabra.replace("",",")
print("S"+resultado)