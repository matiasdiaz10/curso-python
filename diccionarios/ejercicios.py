boquita = {
    1: "Romero", 2:"Figal",
    3:"Colo Barco",4:"Weigant",
    5:"Alan Varela",6:"Marcos Rojo",
    7:"Langoni",8:"Equi Fernandez",
    9:"BeneDios",10:"Medina",
    11:"Oscar Romero"
}

seleccionJugador = int(input("Selecciona un jugador de boquita: "))

if seleccionJugador in boquita:
    print(boquita[seleccionJugador])
else:
    print("No existe el jugador")