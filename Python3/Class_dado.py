"""
DADO
Crea una clase "Dado" que simule el lanzamiento de un dado de 6 caras.
Implementa un método para lanzar el dado y mostrar el resultado (quizás te
convenga usar el modulo random).

"""

import random 

class dado:

    def __init__(self):
        pass

    def hacer_tirada(self): 
        lanzamiento = random.randint(1,6)
        print("El resultado del lanzamiento es...", lanzamiento)
   
mi_dado = dado()

mi_dado.hacer_tirada()


    