"""
LIBRO
Crea una clase "Libro" con atributos como título, autor y año de publicación.
Luego, crea varios objetos Libro y muestra su información.

"""

class libro:
    def __init__(self, titulo,autor,ano_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacion = ano_publicacion
    
    def info(self):
        print(f"El titulo del libro es: {self.titulo}, su autor es: {self.autor}, y se publico en: {self.ano_publicacion} ")

Libro1 = libro("Batalla de dragones", "Jose Virgen", "2002")
Libro2 = libro("Como ganar amigos", "Dale Carnegie", "1945" )

Libro1.info()
Libro2.info()