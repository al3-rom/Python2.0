"""
BUSCANDO EN PI
Busca si tu fecha de nacimiento esta en los primeros 10000 digitos de pi (y
en que posición. Puedes usar find()).
Puedes usar el archivo pi_10000.txt

"""
def buscar_en_pi(filename, string):
    """Busca la fecha de nacimiento dentro del
    el archivo de la 10000 primeras cifras pi"""
# abrir el archivo del pi
    with open(filename, 'r') as file:
        # leer el contenido
        digitos = file.read()
        # encontrar la posicion de el string dentro de digitos
        posicion = digitos.find(string)
        # devolver la posicion
        return(posicion)
# Ejemplo de us
filename = 'numero_pi/pi_10000.txt'
fecha = '270497'
# Preguntamos la posicion de la fecha en el archivo
posicion = buscar_en_pi(filename, fecha)
# Se ha encontrado
if posicion != -1:
 print(f'Tu fecha de nacimiento {fecha} se encontro en la posicion {posicion}')
else:
 print(f"Tu fecha de nacimiento es {fecha} no se encontro en los primeros 10000 digitos del pi")