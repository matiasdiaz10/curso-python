# Self sirve para englobar un atributo a toda una clase
class FabricaTelefonos():

    def __init__(self,marca,color):
        self.marca = marca
        self.color = color

    def ElaborarHuawei(self):
        self.marca = "Samsung"
    
telefono = FabricaTelefonos("Huawei","negro")
print("Este es un telefono: {} de color: {}".format(telefono.marca,telefono.marca))
telefono.ElaborarHuawei()
print("Este es un telefono: {} de color: {}".format(telefono.marca,telefono.marca))
