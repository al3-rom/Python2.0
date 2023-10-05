"""
FACTORIAL
Implementa una función recursiva llamada factorial que calcule el factorial de
un número entero positivo. El factorial de un número no se define como el
producto de todos los números enteros positivos desde 1 hasta n.
(El factorial de 0 y de 1 es igual a 1)

"""

import time

def factorial(numero):
    if(numero) == 0:
        return 1
    return numero * factorial(numero - 1)
    

print(factorial(5))
