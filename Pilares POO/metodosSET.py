class A():
    def __init__(self) -> None:
        self._cuenta = 0
        self._contador = 0
    # Sirve para no utilizar el get sin parentesis
    # metodo GET
    @property
    def cuenta(self):
        return self._cuenta
    
    # metodo SET
    @cuenta.setter
    def cuenta(self, cuenta):
        self._cuenta = cuenta
        
    # metodo GET
    @property
    def contador(self):
        return self._contador
    
    # metodo SET
    @contador.setter
    def contador(self, contador):
        self._contador = contador
    
a = A()
#print(a._contador)
print(a.cuenta)
a.cuenta = 20
print(a.cuenta)
print(a.contador)
a.contador = 10
print(a.contador)