"""
POTENCIA
Implementa una función recursiva llamada potencia que calcule el resultado
de elevar un número a una potencia dada. Puedes asumir que tanto el
número como la potencia son enteros no negativos

"""

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)
    
base = int(input("Base "))
exponente = int(input("Exponente "))

resultado = potencia(base, exponente)
print(resultado)
    

