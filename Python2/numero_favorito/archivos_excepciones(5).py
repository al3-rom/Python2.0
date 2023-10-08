"""
NUMERO FAVORITO
Escribe un programa que solicite al usuario su número favorito. Utiliza
json.dump() para almacenar este número en un archivo. Escribe un
programa separado que lea este valor e imprima el mensaje: "Sé cuál es tu
número favorito… Es ____.” Combina ambos programas en un solo archivo
(puedes crear tantas funciones como necesites). Si el número ya está
almacenado, muestra el número favorito al usuario. Si no lo está, solicita al
usuario su número favorito y guárdalo en un archivo. Ejecuta el programa al
menos dos veces para asegurarte de que funciona correctamente.

"""
# Importamos JSON
import json

def comprobar_num_fav():
    """ Comprobar si existe un archivo con el 
    numero favorito 
    y si existe va a devolver dicho numero """
    try:
     with open("numero_favorito/numero_fav.json", 'r') as file:
        num_fav = json.load(file)
        return(num_fav)

    except FileNotFoundError:
       return None

def guardar_numero_fav(numero_favorito):
    """ Guarda el numero favorito """
    # Abrimos archivo
    with open("numero_favorito/numero_fav.json", 'w') as file:
        # Guardamos numero favorito en file
        json.dump(numero_favorito, file)

def preguntar_numero_fav():
    """ Preguntamos el numero favorito """
    num_fav = int(input("Introduce tu numero favorito: "))
    guardar_numero_fav(num_fav)
    return(num_fav)

def print_num_fav(numero_favorito):
   """ Imprime el numero favorito """
   print(f"Se cual es tu numero favorito... es {numero_favorito}")

# Programa principal

numero_favorito = comprobar_num_fav()

if numero_favorito:
   print_num_fav(numero_favorito)
else:
   numero_favorito = preguntar_numero_fav()
   print(numero_favorito)



