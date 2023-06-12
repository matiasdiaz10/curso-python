class FabricaTelefono():
    def __init__(self,marca,color) -> None:
        self.marca = marca
        self.color = color
        print("El objeto {} ha sido creado".format(self.marca))
    
    def __str__(self) -> str:
        return "El objeto es {}".format(self.marca)

    # elimina el objeto
    def __del__(self):
        print("El objeto {} ha sido destruido".format(self.marca))

tel = FabricaTelefono("Motorola","Gris")
print(tel.marca)
print(tel)
