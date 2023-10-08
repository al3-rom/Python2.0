"""
PALABRAS COMUNES
Encuentra o crea algunos textos que te gustaría analizar (puedes visitar
Project Gutenberg (http://gutenberg.org/) o crear textos usando ChatGPT).
Copia el texto sin formato desde tu navegador en un archivo de texto en tu
computadora (o descarga los archivos). Averigua cuántas veces aparece una
palabra o frase en el texto (puedes usar el método count()).

"""




# Importamos la ruta del archivo
texto = "palabras_comunes/texto.txt"
# Leemos el archivo
with open(texto) as tx1:
    text = tx1.read()
# guardamos el numero de apareciones de las palabras
contador = text.lower().count("repeticiones")
# imprimimos el resultado
print(contador)



