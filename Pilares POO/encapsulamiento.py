class ContadorA():
    def __init__(self) -> None:
        self.contador = 0
        
    def incrementar(self):
        self.contador += 1
    
    def cuenta(self):
        return self.contador
# Para encapsular un atriuto de una clase se coloca __
class ContadorB():
    def __init__(self) -> None:
        self.__contador = 0
        
    def incrementar(self):
        self.__contador += 1
    
    def cuenta(self):
        return self.__contador

print("Objeto 1")
contador1 = ContadorA()
print(contador1.cuenta())
contador1.incrementar()
print(contador1.cuenta())
print(contador1.contador)

print("Objeto 2")
contador2 = ContadorB()
print(contador2.cuenta())