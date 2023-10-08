"""
CLASE PERSONA
Define una clase Persona con atributos como nombre, edad y profesión.
Luego, crea varios objetos de esta clase y muestra su información.

"""

class persona:
    def __init__(self, nombre, edad, profesion):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion
    
    def detalles(self):
        print("Soy:"+self.nombre +
              ",tengo: "+self.edad +
              " y soy: "+self.profesion)
    

Alejandro = persona("Alejandro", "19", "Desarollador Full_Stack, desarollador Blockchain")
Alejandro.detalles()

Alex = persona("Alex", "22", "Full_stack developer")
Alex.detalles()