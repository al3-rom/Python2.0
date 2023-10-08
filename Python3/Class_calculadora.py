"""
CALCULADORA BÁSICA
Crea una clase llamada "Calculadora" con métodos para sumar, restar,
multiplicar y dividir. Crea objetos de esta clase y realiza algunas operaciones
básicas.

"""

class calculadora():
    def __init__(self,numero1,numero2):
        self.numero1 = numero1
        self.numero2 = numero2
    
    def sumar(self):
        resultado = self.numero1 + self.numero2
        print(resultado)
    
    def restar(self):
        resultado = self.numero1 - self.numero2
        print(resultado)

    def multiplicar(self):
        resultado = self.numero1 * self.numero2
        print(resultado)

    def dividir(self):
        resultado = self.numero1 / self.numero2
        print(resultado)
    
numeros = calculadora(2,4)
numeros.sumar()
numeros.restar()
numeros.multiplicar()
numeros.dividir()
