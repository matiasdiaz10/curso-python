class A():
    def __init__(self) -> None:
        self._cuenta = 0
        self._contador = 0
    # Sirve para no utilizar el get sin parentesis
    @property
    def cuenta(self):
        return self._cuenta
    
    @property
    def contador(self):
        return self._contador

a = A()
#print(a._contador)
print(a.cuenta)
print(a.contador)
