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

# Pedimos numero favotiro del usuario
numero_favorito = input("Pon tu numero favotiro: ")

# Sacamos ruta del archivo
num_favorito = "Python2/numero.txt"

# Utilizamos json.dump() para almacenar este numero en un archivo

with open(num_favorito, 'w') as nf:
    json.dump(int(numero_favorito), nf)

print("SEPARAMOS PROGRAMA EN PONER NUMERO Y LEERLO")

archivo = "Python2/numero.txt"

with open(archivo) as arch:
    numero = json.load(arch)
    print("Sé cuál es tu número favorito… Es..."+(str(numero)))
    


