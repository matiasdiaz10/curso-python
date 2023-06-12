tupla = (1, 2, 3, 4, 5)
tupla2 = (6, 7, 8)

print(tupla)
print(tupla2)
print(type(tupla))
print(tupla[1])
print(tupla + tupla2)
# No se puede modificar los valores
""" tupla2[2] = 10
print(tupla2) """

# Ejercicios

#Escribir una tupla con los meses del año, luego el usuario ingresa un numero y debe decir que mes escogio

meses = ('ene','feb','mar','abr','may','jun','jul','ago','sep','oct','nov','dic')
selected = int(input("Ingrese el numero del mes: "))
selected -= 1
print(meses[selected])


# RANGOS

for i in range(1, 10):
    print(i)

# Imprime de dos en dos
for i in range(1, 11, 2):
    print(i)
