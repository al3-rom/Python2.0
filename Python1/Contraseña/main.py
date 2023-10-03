"""
CONTRASENA SEGURA
Crea un script que solicite una contraseña, analice si es segura y si no lo es
sugiera una nueva contraseña. Para ello puedes crear un script validador.py
que contenga una funcion validar_contrasena que reciba una cadena y
verifique si cumple con los requisitos mínimos de una contraseña segura
(por ejemplo, longitud mínima, presencia de letras mayúsculas, letras
minúsculas, números y caracteres especiales). La función debe devolver un
valor booleano que indique si la contraseña es válida o no. Por otro lado
puedes crear otro script creador.py con una función llamada
generar_contrasena que genere contraseñas seguras de forma aleatoria. La
función debe permitir especificar la longitud de la contraseña y qué tipos de
caracteres deben incluirse (por ejemplo, letras mayúsculas, letras
minúsculas, números y caracteres especiales).
(Para el generador de contraseñas puedes probar a usar los modulos
random y string)

"""

# solicitar una contraseña
# validar la contraseña
##contraseña no valida --> seguir nueva contraseña

from validador import validar_contrasena # para enseñar 2 imports diferentes
import generador

def solicitar_contrasena_segura():
    contrasena = input("Ingrese una contraseña: ")
    valida = validar_contrasena(contrasena)

    if valida:
        print("Contraseña segura")
    else:
        print("La contraseña no es segura. Se sugiere una nueva contraseña")
        sugerencia = generador.generar_contrasena_segura(9)
        print("Sugerencia de contraseña: ", sugerencia)

solicitar_contrasena_segura()