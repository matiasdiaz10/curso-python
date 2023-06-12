from faker import Faker
import random
fake = Faker()


listaNombres = []
listaNumeros = []
num = 0
name = ''
pares = []
impares = []

def crearListaDeNombres():
    i = 0
    while i <= 5:
        name = fake.name()
        listaNombres.append(name)
        i += 1
    print("La lista de nombres es: {}".format(listaNombres))

def solicitarListaDeNumeros():
    i = 0
    while i <= 5:
        #num = float(input("Ingrese un numero: "))
        num = random.randint(1,100)
        listaNumeros.append(num)
        i += 1
    print("La lista de numeros es: {}".format(listaNumeros))

def ordenarLista(lista):
    lista.sort()
    print("Lista ordenada: {}".format(lista))


def determinarParidad():
    for i in listaNumeros:
        #Modulo
        if i % 2 == 0:
            pares.append(i)
        else:
            impares.append(i)
    print("Lista de pares: {}".format(pares))
    print("Lista de impares: {}".format(impares))

#Funciones para lista de nombres
crearListaDeNombres()
ordenarLista(listaNombres)
#Funciones para lista de numeros
solicitarListaDeNumeros()
ordenarLista(listaNumeros)
determinarParidad()

def generarTiposArchivos():
    typeArchive = []
    for _ in range(5):
        typeArchive.append(fake.file_extension(category='image'))
    return typeArchive

print(generarTiposArchivos())