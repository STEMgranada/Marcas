from lxml import etree

# Cargar el archivo XML
tree = etree.parse("biblioteca.xml")
root = tree.getroot()

# 1. Selección de elementos con XPath

# Selección de la lista de autores | text() nos muestra el contenido de los elementos
print(root.xpath('libro/autor/text()'))

# Selección del título del primer libro

print(root.xpath("libro[1]/titulo/text()")) # OJO! En Xpath, la lista de nodos comienza por 1

# Selección del título del último libro

print(root.xpath("libro[last()]/titulo/text()"))

# Selección del título del penúltimo libro

print(root.xpath("libro[last()-1]/titulo/text()"))

# Selección del título de los tres primeros libros

print(root.xpath("libro[position()<=3]/titulo/text()"))

# Selección de la lista de títitulos para el autor 'George Orwell'
# /text() nos muestra el contenido de los elementos

print(root.xpath("libro[autor = 'George Orwell']/titulo/text()"))

# Selección de títulos del género 'Novela distópica'

print(root.xpath("libro[genero = 'Novela distópica']/titulo/text()"))

# Selección de títulos del género 'Novela distópica' anteriores al 2000

print(root.xpath("libro[genero = 'Novela distópica' and año<2000]/titulo/text()"))

# EJ1 ¿Qué autores han escrito libros de género 'Novela'?

print(root.xpath("libro[genero = 'Novela']/autor/text()"))

# EJ2 ¿Qué autores han escrito libros de género 'Novela'? Muestra los 5 primeros

print(root.xpath("libro[genero = 'Novela'][position()<=5]/autor/text()"))

# EJ3 ¿Cuántos libros de género 'Novela' posteriores al año 2000 hay?

print(len(root.xpath("libro[genero = 'Novela' and año>2000]/autor/text()")))

# EJ4 Muestra todos los libros del autor del primer libro de la lista de 'Novela'

autor = root.xpath("libro[genero = 'Novela']/autor/text()")[0]
print(root.xpath(f"libro[autor = '{autor}']/titulo/text()"))

# EJ5 Muestra todos los libros escritos entre 1950 y 1980

print(root.xpath("libro[año>=1950 and año <=1980]/titulo/text()"))