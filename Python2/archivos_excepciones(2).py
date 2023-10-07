"""
MANIPULACION DE ARCHIVOS Y FILENOTFOUNDERROR
Crea dos archivos, cats.txt y dogs.txt. Almacena al menos tres nombres de
gatos en el primer archivo y tres nombres de perros en el segundo archivo.
Escribe un programa que intente leer estos archivos e imprima el contenido
de cada archivo en la pantalla. Envuelve tu código en un bloque try-except
para capturar el error de FileNotFoundError, e imprime un mensaje amigable
si falta algún archivo. Mueve uno de los archivos a una ubicación diferente
en tu sistema y asegúrate de que el código en el bloque except se ejecute
correctamente. Modifica tu bloque except para que falle en silencio si falta
alguno de los archivos.

"""
# Sacamos la ruta de los archivos
file1 = "Python2\cats.txt"
file2 = "Python2\dogs.txt"
# Leemos los archivos cats y dogs
# # Envolvemos el codigo en un bloque
# Try-except para capturar el error de FileNotFoundError
try:
 with open(file1) as f1:
    contenido1 = f1.read()
 with open(file2) as f2:
    contenido2 = f2.read()
# Imprimimos el mensaje amigable si falta algun archivo
except FileNotFoundError:
    print("El archivo no existe!")

# Imprimimos el contenido de cada archivo en la pantalla
# Aseguremos de que el codigo en el bloque except se ejecute correctamente
# Modificamos el bloque except para que falle en silencio si falta alguno de los archivos
try:
    print(contenido1)
    print(".....")
    print(contenido2)

except FileNotFoundError:
    print("El archivo no existe!")

#### No me sale el ejercicio



