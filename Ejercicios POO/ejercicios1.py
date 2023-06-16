""" Realizar un programa que conste de una clase llamada Alumno que tenga como atributos el nombre y la nota del alumno. 
Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.
 """

class Estudiantes():
    def __init__(self,nombre,nota) -> None:
        self._nombre = nombre
        self._nota = nota
    # GET
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def nota(self):
        return self._nota
    
    #SET
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    
    @nota.setter
    def nota(self, nota):
        self._nota = nota
    
    def imprimirDatosAlumno(self):
        print("Nombre: {} \nNota: {}".format(self.nombre,self.nota))

    def imprimiResultados(self):
        if self._nota < 7:
            print("Alumno desaprobado")
        else:
            print("Alumno aprobado")

estudiante1 = Estudiantes("Matias",10)
estudiante1.imprimirDatosAlumno()
estudiante1.imprimiResultados()

estudiante2 = Estudiantes("Carla",3)
estudiante2.imprimirDatosAlumno()
estudiante2.imprimiResultados()


""" Escribir una clase en python que calcule pow(x, n)
x = es la base
n = es el exponente """