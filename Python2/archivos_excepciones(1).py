"""
SUMA Y VALUEERROR
Un problema común al solicitar una entrada numérica ocurre cuando las
personas ingresan texto en lugar de números. Cuando intentas convertir la
entrada a un entero (int), obtendrás un ValueError. Escribe un programa que
solicite dos números. Suma los números y muestra el resultado. Captura el
ValueError si alguno de los valores de entrada no es un número e imprime un
mensaje de error amigable. Prueba tu programa ingresando dos números y
luego ingresando texto en lugar de un número. Envuelve tu código del en un
bucle while para que el usuario pueda continuar ingresando números incluso
si comete un error ingresando texto en lugar de un número.

"""

print("Vamos a sumar los numeros!")

# Si el usuario quiere salir del bucle:
print("Introduce 's' para salir!")
# El bucle es infinito hasta que el usuario no salga
while True:
    # Pedimos los numeros al usuario
    numero1 = input("\nPrimer numero: ")
    # Si el usuario quiere salir del bucle:
    if numero1 == 's':
        break
    numero2 = input("Segundo numero: ")
    
    if numero2 == 's':
        break
    try:
    # Intentamos dar el resultado de la suma de los numeros
        resultado = int(numero1) + int(numero2)
    # Imprimimos el error amigable si el usuario introducido una letra en vez de un numero
    except ValueError:
        print("Has puesto una letra, introduce los numeros de nuevo!")
    # Imprimimos el resultado si no falla nada
    else:
        print(resultado)


 
    

