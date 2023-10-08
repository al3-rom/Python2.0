"""
RECTÁNGULO
Crea una clase "Rectangulo" con atributos de longitud y ancho. Implementa
un método para calcular el área y el perímetro del rectángulo.

"""

class rectangulo:
    def __init__(self, longitud, ancho):
        self.longitud = longitud
        self.ancho = ancho
    
    def area(self):
        resultado = self.longitud * self.ancho
        return resultado
    
    def perimetro(self):
        resultado = 2 * (self.longitud + self.ancho)
        return resultado

mi_rectangulo = rectangulo(12,10)

print("El area del rectangulo es:",mi_rectangulo.area())
print("El perimetro del rectangulo es:",mi_rectangulo.perimetro())