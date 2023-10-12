"""
Imagina que estás desarrollando un sistema de reservas de vuelos para una
aerolínea. Crea un sistema de clases que permita a los usuarios realizar
reservas de vuelos. Aquí tienes una posible estructura:
- Clase base: `Vuelo`
 - Atributos: número de vuelo, origen, destino, capacidad máxima, lista de
pasajeros
 - Métodos: agregar pasajero, verificar disponibilidad de asientos
- Clase derivada: `VueloEspecial` (hereda de `Vuelo`)
 - Atributos adicionales: motivo del vuelo especial (por ejemplo, vacaciones,
trabajo)
Resuelve el problema creando instancias de estas clases y realizando
reservas para diferentes vuelos y tipos de vuelos especiales.

"""

class Vuelo:
    def __init__(self,numero_vuelo,origen,destino,capacidad_max):
        self.numero_vuelo = numero_vuelo
        self.origen = origen
        self.destino = destino
        self.capacidad_max = capacidad_max
        self.lista_pasajeros = []

    def agregar_pasajero(self,pasajero):

        if len(self.lista_pasajeros) < self.capacidad_max:
            print(f"Has agregado el pasajero: {pasajero} con exito!")
            self.lista_pasajeros.append(pasajero)
        else:
            print(f"Lo sentimos {pasajero}, no hay asientos disponibles!")


    def verificar_asientos(self):
       print("Quedan: ",self.capacidad_max - len(self.lista_pasajeros),"asientos!")

class VueloEspecial(Vuelo):
    def __init__(self, numero_vuelo, origen, destino, capacidad_max,motivo):
        super().__init__(numero_vuelo, origen, destino, capacidad_max)
        self.motivo = motivo
            

vuelo1 = Vuelo(1,"España","Francia",2)
vuelo2 = VueloEspecial(2,"Alemania", "Londres",2,"Vacaciones")

vuelo1.agregar_pasajero("Alejandro")
vuelo1.verificar_asientos()
vuelo1.agregar_pasajero("Alex")
vuelo1.verificar_asientos()
vuelo1.agregar_pasajero("Alvaro")

vuelo2.verificar_asientos()
vuelo2.agregar_pasajero("Laura")
vuelo2.verificar_asientos()
vuelo2.agregar_pasajero("Consuelo")
vuelo2.verificar_asientos()
vuelo2.agregar_pasajero("Angel")



