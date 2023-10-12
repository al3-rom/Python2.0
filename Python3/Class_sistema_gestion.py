"""
SISTEMA DE GESTION DE BIBLIOTECA
Crea un sistema de gestión de una biblioteca utilizando clases en Python.
Debes implementar las siguientes clases:
1. “Libro”: Representa un libro con atributos como título, autor y número de
ejemplares disponibles.

2. “Usuario”: Representa a un usuario de la biblioteca con atributos como
nombre, número de identificación y lista de libros prestados.

3. “Biblioteca”: Representa la biblioteca en sí, con métodos para agregar
libros, prestar libros a usuarios, devolver libros y mostrar el inventario.
"""

class Libro:
    def __init__(self,titulo,autor,ejemplares_disponibles):
        self.titulo = titulo
        self.autor = autor
        self.ejemplares_disponibles = ejemplares_disponibles

class Usuario:
    def __init__(self,nombre,identificacion):
        self.nombre = nombre
        self.identificacion = identificacion
        self.libros_prestados = []

class Biblioteca:
    def __init__(self):
        self.libros = []
    
    def agregar_libro(self,libro):
        self.libros.append(libro)
    
    def prestar_libro(self,usuario,titulo):
        for libro in self.libros:
            if libro.titulo == titulo and libro.ejemplares_disponibles > 0:
                usuario.libros_prestados.append(libro)
                libro.ejemplares_disponibles -= 1
                print(f"El libro {titulo} ha sido prestado a {usuario.nombre}")
                
                return
        print("El ejemplar no esta disponible")\
        
    def mostrar_inventario(self):
        for libro in self.libros:
            print(f"{libro.titulo} de {libro.autor} - Disponibles {libro.ejemplares_disponibles}")
            
        
# Ejemplo de Uso

biblioteca = Biblioteca()

libro1 = Libro("El Gran Gatsby", "F.Scott",4)
libro2 = Libro("Dovakin", "Skyrim", 5)

biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

user1 = Usuario("Laura", "221")
user2 = Usuario("Alejandro", "533")

biblioteca.prestar_libro(user1,"Dovakin")
biblioteca.prestar_libro(user2, "El Gran Gatsby")

biblioteca.mostrar_inventario()