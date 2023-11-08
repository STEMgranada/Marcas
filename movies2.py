# Crea un script de python que muestre por pantalla: 
#    1.- La película más larga.
#    2.- La película más corta.
#    3.- La duración media de las películas.
#    4.- Ten en cuenta que no todas las películas disponen 
#        del dato de duración.
#
# Además, el script debe solicitar por pantalla el nombre de una película
# y mostrar por pantalla si está por encima o por debajo de la media.
#
# Si la película solicitada no tiene duración, 
# debe solicitar una película nueva hasta que sea válida.

from lxml import etree

def listaStringAListaInt(listaString):
    listaInt = []

    for numeroString in listaString:
        listaInt.append(int(numeroString))
    
    return listaInt

def calcularMediaLista (listaNumeros):
    sumatorioDuracion = 0 # Aqui va sumando lo que duran todas y cada una de las pelis, en total
    numeroPelis = len(listaDuraciones)
    for numero in listaNumeros:
        sumatorioDuracion+=numero
    
    media = sumatorioDuracion / numeroPelis # Media de duracion = lo que duran todas las pelis entre el numero de pelis que hay

    return media

# ===================== MAIN ===================== #

# Cargar el archivo XML
tree = etree.parse("movies.xml")
root = tree.getroot()

listaDuraciones = root.xpath(f"Movie/Title/@runtime") # Aqui, esta pillando con el metodo xpath, una lista de todos los elementos pelicula y de cada uno solo se guarda el valor del atributo @duracion
listaDuraciones = listaStringAListaInt(listaDuraciones) # Aqui simplemente, como el xpath solo te devuelve una lista de strings, y a nosotros nos interesa que la duracion de las pelis sean numeros para poder hacer comparaciones y
                                                        #operaciones con esos numeros, pues utiliza un metodo que convierte los strings de una lista a numeros enteros, y los guarda en una lista diferente

minimaDuracion = min(listaDuraciones) # Metodo min saca el numero mas pequeño que hay dentro de una lista en python
maximaDuracion = max(listaDuraciones) # Lo mismo pero al reves, saca el maximo
mediaDuracion = calcularMediaLista(listaDuraciones)

# IMPORTANTE, en xpath si te fijas, las condiciones para buscar algo en especifico se ponen entre corchetes, por ejemplo Titulo[@duracion = 10]
# y ademas, los atributos se indican con un @, por ejemplo, Pelicula/Titulo/@duracion (osea, el atributo duracion del elemento titulo)

tituloPeliMinima = root.xpath(f"Movie/Title[@runtime={minimaDuracion}]/text()")[0] # ahora que sabemos cuanto duran las pelis mas cortas y las mas largas, podemos hacer un xpath que diga: de los elementos pelicula, queremos de su elemento
                                                                                    #titulo cuyo atributo duracion sea igual a tatata, su valor text() (osea, el texto del titulo) y lo del [0] ni puta idea de que es pero tu ponlo a ver que hace
tituloPeliMaxima = root.xpath(f"Movie/Title[@runtime={maximaDuracion}]/text()")[0] # esto hace mas de lo mismo, pero en vez de buscar la peli mas corta, busca la peli mas larga, y saca el texto

print(f"La película de duración mínima ({minimaDuracion}) es: {tituloPeliMinima}")
print(f"La película de duración máxima ({maximaDuracion}) es: {tituloPeliMaxima}")
print(f"La duración media de las películas es: {mediaDuracion}")

duracionPeliculaBuscada = []

while len(duracionPeliculaBuscada) == 0: # como puede darse el caso de que una peli no tenga un atributo duracion, con este bucle lo que hacemos es comprobar si la pelicula que nos dice el usuario tiene el atributo duracion, y en caso de que no lo tenga, el bucle se repite hasta que el usuario nos de una peli con duracion, osea, que este correcta
    nombrePelicula = input("Introduce el nombre de la película a buscar: ") # le pedimos primero una pelicua al usuario
    duracionPeliculaBuscada = root.xpath(f"Movie[Title = '{nombrePelicula}']/Title/@runtime") # una vez pedida la pelicula, vamos a buscar cuanto dura esa pelicula
                                    # lo que dice este xpath es: del elemento pelicula, quiero aquella peli cuyo elemento titulo sea igual que el titulo que ha escrito el usuario, y en caso de que exista, del elemento titulo de esa pelicula, dame el atributo duracion
                                    # una vez mas, si te fijas, para poder comprobar algo concreto en xpath, pone una condicion como si fuese un if entre corchetes, y el atributo lo indica con un @
duracionPeliculaBuscada = int(duracionPeliculaBuscada[0])

if duracionPeliculaBuscada > mediaDuracion:
    print("Duración por encima de la media")
else:
    print("Duración por debajo de la media")