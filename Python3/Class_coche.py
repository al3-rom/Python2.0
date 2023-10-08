"""
COCHE
Crea una clase "Coche" con atributos como marca, modelo y año.
Implementa un método para encender el coche y otro para apagarlo (puedes
simulae el encendido y apagado con una variable booleana).

"""

class coche:
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
    
    def encender_apagar(self):
        while True:
            print(f"La marca es: {self.marca}, el modelo es: {self.modelo}, es año del coche es: {self.anio}")
            arrancar = input("Quieres arrancar el coche?")
            if arrancar == "si".lower():
                apagar = input("El coche esta arrancado! Quieres apagarlo?")
                if apagar == "si".lower():
                    print("El coche esta apagado!")
                    break
                else:
                    print("El coche sigue encendido!")
                    break
            else:
                print("El coche sigue apagado!")
                break

bmw = coche("BMW", "M8", 2023)
bmw.encender_apagar()