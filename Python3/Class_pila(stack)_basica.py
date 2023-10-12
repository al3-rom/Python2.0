"""
PILA (STACK) BÁSICA
En programación, un "stack" es una estructura de datos que sigue el
principio de LIFO (Last In, First Out), lo que significa que el último elemento
agregado a la pila es el primero en ser retirado. Imagina una pila de platos:
cuando apilas un nuevo plato, este se coloca en la parte superior de la pila,
y cuando retiras un plato, siempre tomas el de arriba primero.
En Python, puedes implementar un stack utilizando una lista. Puedes
agregar elementos a la pila utilizando el método `append()`, y puedes retirar
elementos de la pila utilizando el método `pop()` sin ningún índice
especificado, ya que `pop()` por defecto elimina y devuelve el último
elemento de la lista.
Los stacks son útiles en muchas situaciones, como algoritmos de búsqueda
y recorrido, manejo de llamadas a funciones (con la pila de llamadas),
manejos de historial y navegación y más.

Crea una clase "Pila" que represente una pila (stack) básica. Implementa
métodos para agregar elementos a la pila, quitar elementos y mostrar el
contenido actual.
Por supuesto, estaré encantado de explicarte qué es un "stack" en el
contexto de la programación y cómo se utiliza en Python.

"""

class Pila:
    def __init__(self,nombre_pila,cantidad):
        self.nombre_pila = nombre_pila
        self.cantidad = cantidad
    
    def mostrar_contenido(self):
        print(f"La cantidad de pila {self.nombre_pila} actual es: {self.cantidad}")
    
    def agregar_elementos(self,nombre_pila,cantidad):
        
        if self.nombre_pila == nombre_pila:
            self.cantidad += cantidad

        print("Has añadido con exito!")
        print(f"La cantidad de pila {self.nombre_pila} actual es: {self.cantidad}")

    def quitar_elementos(self,nombre_pila,cantidad):
        if self.nombre_pila == nombre_pila:
            self.cantidad -= cantidad
        print(f"Has quitado una cantidad de: {cantidad} productos de tu pila con exito!")
        print(f"La cantidad de pila {self.nombre_pila} actual es: {self.cantidad}")

pila1 = Pila("Platos", 15)
pila2 = Pila("Vasos", 10)

pila1.mostrar_contenido()
pila2.mostrar_contenido()


pila1.agregar_elementos("Platos",15)
pila2.agregar_elementos("Vasos",10)

pila1.quitar_elementos("Platos",3)
pila2.quitar_elementos("Vasos",5)

