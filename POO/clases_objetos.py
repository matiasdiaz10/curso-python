from pprint import pprint

class FabricaTelefonos():
    marca = "Huawi"
    color = "Negro"
    memoriaRam = 2
    almacenamiento = 32

    def llamar(self, mensaje):
        pprint(mensaje)
        return mensaje
    
    def queEscuchas(self):
        print("Estas escuchando coldplay")

print(type(FabricaTelefonos))

celular = FabricaTelefonos()
print(type(celular))
pprint(celular)

celular.llamar("boquita muy grande")
celular.queEscuchas()