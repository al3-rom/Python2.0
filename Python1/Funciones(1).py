# Define una función llamada "saludar" que tome un parámetro "nombre"
# y muestre un saludo personalizado

def saludar(nombre):
    print(f"Bienvenido {nombre}!")

saludar("Alejandro")

# Crea una función llamada "suma" que tome dos parámetros "a" y "b" e
# imprima la suma de ambos

def suma(a,b):
    print(a+b)

suma(2,6)

# Escribe una función llamada "calcular_area_rectangulo" que tome dos
# parámetros "base" y "altura" y calcule el área de un rectángulo.

def calcular_area_rectangulo(base,altura):
    print(base * altura)

calcular_area_rectangulo(2,6)

# Define una función llamada "imprimir_lista" que tome una lista como
# parámetro y la imprima en la consola.
def imprimir_lista(lista):
    print(lista)
# No se si esta bien!
imprimir_lista([2,4,5])

# Crea una función llamada "es_par" que tome un número como
# parámetro e imprima True si es par, o False si es impar.

def es_par(numero):
    if numero % 2 == 0:
        print("True")
    else:
        print("Falce")

es_par(3)

# Escribe una función llamada "concatenar_strings" que tome dos
# parámetros "cadena1" y “cadena2" e imprima la concatenación de
# ambas cadenas.

def concatenar_strings(cadena1,cadena2):
    print(cadena1 + " " + cadena2)

concatenar_strings("Hola", "Amigos")

# Define una función llamada "obtener_maximo" que tome una lista de
# números como parámetro y devuelva el número máximo de la lista.

def obtener_maximo(lista):
    print(max(lista))

obtener_maximo([2,4,6,9])

# Crea una función llamada "convertir_fahrenheit_a_celsius" que tome un
# parámetro "fahrenheit" y devuelva su equivalente en grados Celsius.

def convertir_fahrenheit_a_celsius(fahrenheit):
    print("La conversion a grados Celsius es:", fahrenheit-32*(5/9))

convertir_fahrenheit_a_celsius(20)

# Escribe una función llamada "calcular_edad" que tome dos parámetros:
# "año_actual" y "año_nacimiento" y calcule la edad de una persona.

def calcular_edad(año_actual,año_nacimiento):
    print("Tu edad es:", año_actual-año_nacimiento)

calcular_edad(2023,2003)

# Define una función llamada "es_divisible" que tome dos parámetros
# "num" y "divisor" e imprima True si "num" es divisible por "divisor", o
# False si no lo es.

def es_divisible(num,divisor):
    if num % divisor == 0:
        print("True")
        print(num%divisor)
    else:
        print("Falce")
        print(num%divisor)

es_divisible(4,2)

# Crea una función llamada "mostrar_info_persona" que tome tres
# argumentos de palabra clave: "nombre", "edad" y "ciudad". La función
# debe imprimir en la consola la información de una persona en un
# formato legible.

def mostrar_info_persona(nombre,edad,ciudad):
    print("El nombre es: ", nombre)
    print("Su edad es: ",edad)
    print("Su ciudad es: ", ciudad)

mostrar_info_persona("Alejandro",19,"Coma-Ruga")

# Escribe una función llamada "calcular_promedio" que tome una lista de
# números como parámetro y calcule el promedio de esos números. Si no
# se proporciona una lista, debe usar una lista vacía por defecto

def calcular_promedio(numeros):
    print("Promedio de los numeros:", numeros, "es:", sum(numeros)/len(numeros))

calcular_promedio([2,3,3,5,7,10])

# Crea una función llamada "calcular_potencia" que tome dos
# parámetros "base" y "exponente", y calcule la potencia de la base
# elevada al exponente. Utiliza 2 como valor por defecto para el
# exponente

def calcular_potencia(base, exponente = 2):
    print("La potencia de la base es:", base*exponente)

calcular_potencia(3)

# Define una función llamada "imprimir_info_alumno" que tome un
# argumento posicional “nombre”(y sin valor por defecto) y varios
# argumentos de palabra clave: "edad", "curso" y “promedio" (puedes
# ponerles como valor por defecto None). La función debe imprimir la
# información del alumno en un formato legible.

def imprimir_info_alumno(nombre, edad = None, curso = None, promedio = None):
    print("Info sobre un alumno")
    print(f"Su nombre: {nombre}, su edad: {edad}, su curso: {curso} y su promedio es: {promedio}")

imprimir_info_alumno("Alejandro", 19, "ConquerBlocks", 6)
