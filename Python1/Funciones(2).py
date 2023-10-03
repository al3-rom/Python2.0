"""
Crea un programa que valide un formulario de registro. Crea una función
llamada validar_formulario que reciba diferentes campos de un formulario
(nombre, correo electrónico y número de teléfono) y verifique si los valores
ingresados cumplen con los requisitos especificados, siendo estos:
1. Que el nombre tenga una longitud minima de 3 caracteres
2. Que el teléfono este conformado por dígitos y tenga una longitud de 9
caracteres
3. Que el email contenga un “@“ y un “.”

"""

# funcion para validar formularios
def validar_formulario(nombre, email, telefono):
    """ Esta funcion valida si los datos ingresados
    tienen el formato correcto"""
    # INPUT
    # - Nombre: str
    # - Email: str
    # - Telefono: str de digitos

    # Comprobamos las condiciones
    if len(nombre) < 3:
        return False

    if "@" not in email or "." not in email:
        return False

    if len(telefono) !=9 or not telefono.isdigit():
        return False

    return True



# pedir informacion al usuario
nombre = input("Nombre: " )
email = input("@mail: " )
telefono = input("Numero de telefono: " )

# validamos el formulario llamando a la 
# funcion de validacion
valido = validar_formulario(nombre, email, telefono)

# comprobamos el resultado de la validacion
if valido:
    print("Formulario valido")
else: 
    print("Formulario no valido")

""" 
Crea un programa que permita gestionar las ventas de una tienda. Utiliza una
estructura de datos adecuada para almacenar la información de las ventas
(por ejemplo, una lista de diccionarios). Implementa dos funciones, una para
agregar el producto vendido con su precio y otro para mostrar las ventas de
productos con sus respectivos precios.
(La base de datos puede tener la forma [{“Producto”: producto1, “Precio”:
precio1}, {“Producto”: producto2, “Precio”: precio2}…])

"""

productos = {}

print("_______________")
def agregar_producto(producto, precio):
    productos[producto] = precio

def mostrar_ventas():
    for producto, precio in productos.items():
        print(producto, precio)


agregar_producto("Manzana", 1.40)
agregar_producto("Mango", 2.60)
mostrar_ventas()  





