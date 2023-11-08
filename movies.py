# Crea un script de python que solicite por pantalla al usuario:
# - Un rating de edad
# - Un género
# - Una duración mínima
# Muestre las películas que cumplen esos requisitos utilizando xpath

from lxml import etree

# Cargar el archivo XML
tree = etree.parse("movies.xml")
root = tree.getroot()

restriccionEdad = input("Introduce una restricción de edad (R G PG PG-13): ")
genero = input("Introduce un género de película (Crime Drama, Drama, Action-Advneture, Romantic Drama, Action Drama, Epic Sports-Drama, Biographical Drama, Indian Drama, Patriotic): ")
duracion = input("Introduce una duración mínima (en minutos): ")

print(
    # OJO, tu profe aqui ha hecho el XPATH desde la variable root (la raiz) osea que, como lo hace desde la raiz
    # no hace falta indicar en el XPATH el elemento raiz desde el que comienza el path / camino / url / ruta o llamlo como quieras
    root.xpath(f"Movie[@rating = '{restriccionEdad}' and Genre='{genero}']/Title[@runtime>{duracion}]/text()")
)