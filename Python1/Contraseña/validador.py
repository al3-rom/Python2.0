def validar_contrasena(contrasena):
    """ Esta funcion valida la contraseña dada como argumento"""


    longitud_minima = 8
    tiene_mayuscula = False
    tiene_minuscula = False
    tiene_numero = False
    tiene_caracter_especial = False

    if len(contrasena) < longitud_minima:
        return False

    for caracter in contrasena:
        if caracter.isupper():
            tiene_mayuscula = True
        elif caracter.islower():
            tiene_minuscula = True
        elif caracter.isdigit():
            tiene_numero = True
        else:
            tiene_caracter_especial = True

    return tiene_mayuscula and tiene_minuscula and tiene_numero and tiene_caracter_especial