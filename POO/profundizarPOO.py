class FabricaTelefonos():
    # Puedo usar this en vez de self
    # Puedo usar * para representar una tupla
    # Puedo usar ** para representar un diccionario
    def __init__(this, marca, *colores, **modelos) -> None:
        this.marca = marca
        this.colores = colores
        this.modelos = modelos
    
telefono = FabricaTelefonos("Motorola", "Azul", "Negro", "Blanco", mod_1 = 'motoE5', mod_2 = 'motoE5 plus')
print(telefono.marca)
print(telefono.colores) #('Azul','Negro','Blanco')
print(telefono.modelos)
# se agrega un nuevo atributo a la clase
telefono.memoria = 500
print(telefono.memoria)
