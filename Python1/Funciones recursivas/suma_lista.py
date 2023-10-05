"""
SUMA ELEMENTOS DE UNA LISTA
Crea una función recursiva llamada suma_lista que calcule la suma de todos
los elementos de una lista de enteros. Puedes asumir que la lista no está
vacía
"""

def suma_lista(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return lista[0] + suma_lista(lista[1:])

""" 
1 + suma_lista([2,3,4,5])
1 + 2 + suma_lista([3,4,5])
1 + 2 + 3 + suma_Lista([4,5])
1 + 2 + 3 + 4 + suma_lista([5])
1 + 2 + 3 + 4 + 5
"""
print(suma_lista([1,2,3,4,5]))

